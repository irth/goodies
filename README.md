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

![screencast of chrome_to_cookiejar](./media/chrome_to_cookiejar.gif)
