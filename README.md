# goodies

Drop-in to bin goodies. Usually zero-dependency, except for the language it's
written in.

<!-- START GOODIES SECTION -->
## [`bin/telegram_macos_copy_fix`](./bin/telegram_macos_copy_fix)

**Monitors and automatically fixes Mac version of Telegram's image copy bug
that causes double-paste in iMessage**

Requires: `swiftc`.

**Disclaimer: this was vibe-coded. I don't want to do macOS dev.**

When you copy an image from full screen view in Telegram, it creates 2
separate pasteboard items instead of 1 item with multiple representations.
This causes images to paste twice in iMessage.

This tool monitors your clipboard and automatically fixes it when the bug
is detected.

**Usage:**

- Add `telegram_macos_copy_fix` to autostart somehow. E.g. put it in
  [AeroSpace](https://github.com/nikitabobko/aerospace)'s
  `after-startup-command` setting. The script has a `#!` line so as long as
  you have `swiftc` it should work.


### Screencasts

![telegram_macos_copy_fix.gif](./media/telegram_macos_copy_fix.gif)



### Installation

**Install via [chezmoi](https://www.chezmoi.io/):**

In `~/.local/share/chezmoi/.chezmoiexternal.toml`

```toml
[".local/bin/telegram_macos_copy_fix"]
type = "file"
url = "https://raw.githubusercontent.com/irth/goodies/4b14056611b06c5f9e493078d70825909b450416/bin/telegram_macos_copy_fix"
executable = true
```

**Install via shell:**

```bash
( echo \
 && echo Ensuring '~/.local/bin' exists... \
 && mkdir -p '~/.local/bin' \
 && echo Downloading... \
 && curl -s https://raw.githubusercontent.com/irth/goodies/4b14056611b06c5f9e493078d70825909b450416/bin/telegram_macos_copy_fix -o '~/.local/bin/telegram_macos_copy_fix' \
 && chmod +x '~/.local/bin/telegram_macos_copy_fix' \
 && echo 'Installed into' '~/.local/bin/telegram_macos_copy_fix' \
 && echo 'Make sure ~/.local/bin is in your $PATH' )
```


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

![chrome_to_cookiejar_1.gif](./media/chrome_to_cookiejar_1.gif)



### Installation

**Install via [chezmoi](https://www.chezmoi.io/):**

In `~/.local/share/chezmoi/.chezmoiexternal.toml`

```toml
[".local/bin/chrome_to_cookiejar"]
type = "file"
url = "https://raw.githubusercontent.com/irth/goodies/4b14056611b06c5f9e493078d70825909b450416/bin/chrome_to_cookiejar"
executable = true
```

**Install via shell:**

```bash
( echo \
 && echo Ensuring '~/.local/bin' exists... \
 && mkdir -p '~/.local/bin' \
 && echo Downloading... \
 && curl -s https://raw.githubusercontent.com/irth/goodies/4b14056611b06c5f9e493078d70825909b450416/bin/chrome_to_cookiejar -o '~/.local/bin/chrome_to_cookiejar' \
 && chmod +x '~/.local/bin/chrome_to_cookiejar' \
 && echo 'Installed into' '~/.local/bin/chrome_to_cookiejar' \
 && echo 'Make sure ~/.local/bin is in your $PATH' )
```


<!-- END GOODIES SECTION -->
