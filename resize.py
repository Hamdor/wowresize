# Disclaimer: Use this script at your own risk. I offer no guarantees regarding its functionality or safety.
# The script may be detected by anti-cheat systems, leading to potential account bans.
# I am not responsible for any damage or loss caused by its use.

import argparse
import win32gui

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="Resize a window", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--width", type=int, default=3246, help="Width to resize the window")
  parser.add_argument("--height", type=int, default=1392, help="Height to resize the window")
  parser.add_argument("--title", type=str, default="WORLD OF WARCRAFT", help="Title of the window to resize")
  args = parser.parse_args()

  hwnd = win32gui.FindWindow(None, args.title)
  if hwnd != 0:
    win32gui.SetWindowPos(hwnd, None, 0, 0, args.width, args.height, 0)