import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launchmeme(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s b a r  M e m e')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("Meme", systemlevel, systempro, settingsdict)
