from mudarWallpaper import mudarWallpaper
from tamanhoLista import tamanhoLista
from os.path import isfile, join
from time import sleep
from os import listdir


def slideWallpaper(pathPasta):

    wallpapers = [w for w in listdir(pathPasta) if isfile(join(pathPasta, w))]
    wallpaperIndice = 0

    while True:
        wallpaperAtivo = wallpapers[wallpaperIndice]
        mudarWallpaper(f'{pathPasta}/{wallpaperAtivo}')

        if wallpaperIndice < tamanhoLista(wallpapers)-1:
            wallpaperIndice += 1
        else:
            wallpaperIndice = 0

        sleep(300)

if __name__ == "__main__":
    exit()
