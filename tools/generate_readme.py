#!/usr/bin/env python3
import io
import pathlib
import shlex
import subprocess
import sys

import tomlkit

REPO_ROOT = pathlib.Path(__file__).parent.parent
MEDIA_PATH = REPO_ROOT / "media"
BIN_PATH = REPO_ROOT / "bin"

NEW_README = io.StringIO()


def print_to_buffer(*args, **kwargs):
    global NEW_README
    kwargs["file"] = NEW_README
    print(*args, **kwargs)


def print_header(goodie_name: str):
    print_to_buffer(f"## [`bin/{goodie_name}`](./bin/{goodie_name})")
    print_to_buffer()


def get_script_language(goodie_source: str):
    first_line = goodie_source.splitlines()[0]
    if first_line.strip() == "#!/usr/bin/env python3":
        return "python"
    raise RuntimeError(f"unknown shebang line for {goodie_source}: {first_line}")


def print_script_doc(goodie_path: pathlib.Path):
    p = subprocess.run(
        [str(goodie_path), "--help"], check=True, capture_output=True, text=True
    )
    print_to_buffer(p.stdout.strip())
    print_to_buffer()
    print_to_buffer()


def print_screencasts(goodie_name: str):
    screencasts = []
    default_screencast = MEDIA_PATH / f"{goodie_name}.gif"
    if default_screencast.exists():
        screencasts.append(default_screencast)

    screencasts += MEDIA_PATH.glob(f"{goodie_name}_*.gif")

    if not screencasts:
        return

    print_to_buffer("### Screencasts")
    print_to_buffer()

    for screencast in screencasts:
        print_to_buffer(f"![{screencast.name}](./media/{screencast.name})\n")

    print_to_buffer()
    print_to_buffer()


def print_install_guide(goodie_name: str):
    latest_commit_p = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=True,
        cwd=REPO_ROOT,
    )
    latest_commit_hash = latest_commit_p.stdout.strip()

    install_dir = "~/.local/bin"
    install_path = install_dir + "/" + goodie_name

    raw_url = f"https://raw.githubusercontent.com/irth/goodies/{latest_commit_hash}/bin/{goodie_name}"
    command = (
        "( "
        + " \\\n && ".join(
            [
                "echo",
                "echo Ensuring " + shlex.quote(install_dir) + " exists...",
                "mkdir -p " + shlex.quote(install_dir),
                "echo Downloading...",
                shlex.join(["curl", "-s", raw_url, "-o", install_path]),
                shlex.join(["chmod", "+x", install_path]),
                shlex.join(["echo", "Installed into", "~/.local/bin/" + goodie_name]),
                shlex.join(["echo", "Make sure ~/.local/bin is in your $PATH"]),
            ]
        )
        + " )"
    )

    chezmoi_config = tomlkit.document()
    goodie_table = tomlkit.table()
    goodie_table.add("type", "file")
    goodie_table.add("url", raw_url)
    goodie_table.add("executable", True)
    chezmoi_config.add(f".local/bin/{goodie_name}", goodie_table)

    print_to_buffer("### Installation")
    print_to_buffer()
    print_to_buffer("**Install via [chezmoi](https://www.chezmoi.io/):**")
    print_to_buffer()
    print_to_buffer("In `~/.local/share/chezmoi/.chezmoiexternal.toml`")
    print_to_buffer()
    print_to_buffer("```toml")
    print_to_buffer(tomlkit.dumps(chezmoi_config).strip())
    print_to_buffer("```")
    print_to_buffer()
    print_to_buffer("**Install via shell:**")
    print_to_buffer()
    print_to_buffer("```bash")
    print_to_buffer(command.strip())
    print_to_buffer("```")
    print_to_buffer()
    print_to_buffer()


def print_all_goodie_sections():
    for goodie_path in (BIN_PATH).glob("*"):
        goodie_path = pathlib.Path(goodie_path)
        goodie_name = goodie_path.name

        print_header(goodie_name)
        print_script_doc(goodie_path)
        print_screencasts(goodie_name)
        print_install_guide(goodie_name)


def regenerate_readme():
    with (REPO_ROOT / "README.md").open("r") as readme:
        in_goodies_section = False
        found_goodies_section = False
        found_goodies_section_end = False
        for line in readme:
            if not in_goodies_section:
                print_to_buffer(line, end="")
                if line.strip() == "<!-- START GOODIES SECTION -->":
                    in_goodies_section = True
                    found_goodies_section = True
                continue
            if line.strip() == "<!-- END GOODIES SECTION -->":
                in_goodies_section = False
                found_goodies_section_end = True
                print_all_goodie_sections()
                print_to_buffer(line, end="")

        if not found_goodies_section:
            print(
                "<!-- START GOODIES SECTION --> missing from README.md", file=sys.stderr
            )
        if not found_goodies_section_end:
            print("<!-- END_GOODIES_SECTION --> missing from README.md")

    with (REPO_ROOT / "README.md").open("w") as readme:
        readme.write(NEW_README.getvalue())


if __name__ == "__main__":
    regenerate_readme()
