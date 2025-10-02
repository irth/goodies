# goodies

Drop-in to bin goodies. Usually zero-dependency, except for the language it's
written in.

<!-- START GOODIES SECTION -->
## [`bin/chrome_to_cookiejar`](./bin/chrome_to_cookiejar)

**Converts cookies copied straight from the Chrome devtools UI into a yt-dlp
compatible format (Mozilla/Netscape cookies.txt)**

- `chrome_to_cookiejar` - read from stdin
- `chrome_to_cookiejar -` - read from stdin
- `chrome_to_cookiejar clip` - read from clipboard (suports pbpaste, wl-paste,
  xclip and xsel, but only pbpaste was tested)
- `chrome_to_cookiejar ./path/to/file` - read from file

Outputs to stdout.


### Screencasts

- ![chrome_to_cookiejar_1.gif](./media/chrome_to_cookiejar_1.gif)


### Installation

**Install via [chezmoi](https://www.chezmoi.io/):**

In `~/.local/share/chezmoi/.chezmoiexternal.toml

```toml
[".local/bin/chrome_to_cookiejar"]
type = "file"
url = "https://raw.githubusercontent.com/irth/goodies/8b98e101cb2931c6ad191f480a10454e5d559401/bin/chrome_to_cookiejar"
executable = true
```

**Install via shell:**

```bash
( echo \
 && echo Ensuring '~/.local/bin' exists... \
 && mkdir -p '~/.local/bin' \
 && echo Downloading... \
 && curl -s https://raw.githubusercontent.com/irth/goodies/8b98e101cb2931c6ad191f480a10454e5d559401/bin/chrome_to_cookiejar -o '~/.local/bin/chrome_to_cookiejar' \
 && chmod +x '~/.local/bin/chrome_to_cookiejar' \
 && echo 'Installed into' '~/.local/bin/chrome_to_cookiejar' \
 && echo 'Make sure ~/.local/bin is in your $PATH' )
```


<!-- END GOODIES SECTION -->
