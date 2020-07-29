import ctypes
import sys


def mudarWallpaper(pathWallpaper):
    try:
        return ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{pathWallpaper}', 0)
    except:
        sys.exit()

if __name__ == "__main__":
    exit()
