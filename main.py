from colorama import Fore, Back, Style
import time
import os   
import keyboard
def showText(sentence):
    os.system('cls')

    for i in sentence:
        print(Fore.GREEN+i,end='',flush=True)
        time.sleep(.5)


showText('Wake up, Neo...')
keyboard.wait('ctrl')
showText('The matrix has you...')
keyboard.wait('ctrl')
showText('Follow the rabbit.')
keyboard.wait('ctrl')
showText('Knock, knock, Neo.')
time.sleep(5)
showText(' ')
input()
