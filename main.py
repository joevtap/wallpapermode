from time import sleep
from os import system

print(20*'#', 'Wallpaper Mode', 20*'#')
print('--- Escolha entre as opcoes abaixo ---')
while True:
    print('1 - Modo otaku')
    print('2 - Modo normal')

    modoEscolhido = input('>>> ')

    if '1' in modoEscolhido:
        system('python modo_otaku.pyw')
        break
    elif '2' in modoEscolhido:
        system('python modo_normal.pyw')
        break
    else:
        print('Voce deve escolher uma das opcoes abaixo')
        continue

exit()
