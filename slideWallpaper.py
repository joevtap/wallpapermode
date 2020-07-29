from mudarWallpaper import mudarWallpaper
from os.path import isfile, join
from time import sleep
from os import listdir


def slideWallpaper(pathPasta):

    wallpapers = [w for w in listdir(pathPasta) if isfile(join(pathPasta, w))]
    wallpaperIndice = 0

    while True:
        wallpaperAtivo = wallpapers[wallpaperIndice]
        mudarWallpaper(f'{pathPasta}/{wallpaperAtivo}')

        if wallpaperIndice < len(wallpapers)-1:
            wallpaperIndice += 1
        else:
            wallpaperIndice = 0
        
        print(f'O wallpaper ativo é "{wallpaperAtivo}"')
        sleep(300)

if __name__ == "__main__":
    exit()
