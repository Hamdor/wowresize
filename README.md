# wowresize

**Disclaimer: Use this script at your own risk. I offer no guarantees regarding its functionality or safety. The script may be detected by anti-cheat systems, leading to potential account bans. I am not responsible for any damage or loss caused by its use.**

WoW Classic does not yet support resizing the game window to arbitrary aspect ratios, as the new retail client does. It always matches the aspect ratio of your monitor. This small script allows setting a custom window size using the Win32 API.

_Note: You only need to run the script once unless you want to change the window size again. The size will persist after restarts, but you'll need to manually reposition the window each time you launch the game._

## How to install
```bash
python -m virutalenv venv
venv\Scripts\activate
pip install pywin32
```

## How to use
```bash
py resize.py --help
usage: resize.py [-h] [--width WIDTH] [--height HEIGHT] [--title TITLE]

Resize a window

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    Width to resize the window (default: 3246)
  --height HEIGHT  Height to resize the window (default: 1392)
  --title TITLE    Title of the window to resize (default: WORLD OF WARCRAFT)
```