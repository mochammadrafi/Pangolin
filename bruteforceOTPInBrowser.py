import os
import time
from os import system 
import pyperclip
import pyautogui

def clear_console(): 
    clear = system('clear' if os.name =='posix' else 'cls') 

def send_key():
    for i in range(0, 9999):
        time.sleep(0.50)
        pyperclip.copy(str(i + 1).zfill(4))
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

clear_console()
send_key()