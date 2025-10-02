# goodies

Drop-in to bin goodies. Usually zero-dependency, except for the language it's
written in.

## [`bin/chrome_to_cookiejar`](./bin/chrome_to_cookiejar) - converts cookies
copied straight from the Chrome devtools UI into a yt-dlp compatible format
(Mozilla/Netscape cookies.txt)

- `chrome_to_cookiejar` - read from stdin
- `chrome_to_cookiejar -` - read from stdin
- `chrome_to_cookiejar clip` - read from clipboard (suports pbpaste, wl-paste,
  xclip and xsel, but only pbpaste was tested)
- `chrome_to_cookiejar ./path/to/file` - read from file

Outputs to stdout.

![screencast of chrome_to_cookiejar](./media/chrome_to_cookiejar_1.gif)

Install:
```bash
( curl https://raw.githubusercontent.com/irth/goodies/refs/heads/main/bin/chrome_to_cookiejar -o /tmp/goodie_chrome_to_cookiejar \
 && echo Press ENTER to read the code. You will be asked for confirmation afterwards. \
 && read \
 && ${PAGER:-less} /tmp/goodie_chrome_to_cookiejar \
 && echo Type yes to confirm installation into ~/.local/bin \
 && read \
 && if [[ "$REPLY" != "yes" ]] then; echo Aborting installation; exit 1; fi \
 && mkdir -p ~/.local/bin \
 && chmod +x /tmp/goodie_chrome_to_cookiejar \
 && mv /tmp/goodie_chrome_to_cookiejar ~/.local/bin/chrome_to_cookiejar \
 && echo 'installed into' '~/.local/bin/chrome_to_cookiejar' \
 && echo 'Make sure ~/.local/bin is in your $PATH' )
```
