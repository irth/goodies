#!/usr/bin/env python3
import pathlib
import shlex
import sys
goodie_path = pathlib.Path(sys.argv[1])
goodie_name = goodie_path.name
print(goodie_name)

install_path='~/.local/bin'
raw_url = f"https://raw.githubusercontent.com/irth/goodies/refs/heads/main/bin/{goodie_name}"
tmp_path = '/tmp/goodie_'+goodie_name
command = "( " + " \\\n && ".join([
    shlex.join(['curl', raw_url, '-o', tmp_path]),
    "echo Press ENTER to read the code. You will be asked for confirmation afterwards.",
    "read",
    " ".join(['${PAGER:-less}', shlex.quote(tmp_path)]),
    "echo Type yes to confirm installation into ~/.local/bin",
    "read",
    'if [[ "$REPLY" != "yes" ]] then; echo Aborting installation; exit 1; fi',
    'mkdir -p ~/.local/bin',
    shlex.join(['chmod', '+x', tmp_path]),
    'mv ' + shlex.quote(tmp_path) + ' ~/.local/bin/' + shlex.quote(goodie_name),
    shlex.join(['echo', 'installed into', '~/.local/bin/' + goodie_name]),
    shlex.join(['echo', 'Make sure ~/.local/bin is in your $PATH'])
]) + " )"
print(command)
