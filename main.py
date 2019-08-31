from pynput.keyboard import Key, Controller
import time
import win32gui


# Author: Prolasis 31 Aug 2019
# this scrip will focus on your window and type "/dance" every 30 seconds

def antiafk():

    whnd = win32gui.FindWindow('Notepad', None)
    print(whnd)
    time.sleep(2)
    win32gui.SetForegroundWindow(whnd)
    win32gui.SetActiveWindow(whnd)

    keyboard = Controller()

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press('/')
    keyboard.release('/')
    time.sleep(1)
    keyboard.press('d')
    keyboard.release('d')
    time.sleep(1)
    keyboard.press('a')
    keyboard.release('a')
    time.sleep(1)
    keyboard.press('n')
    keyboard.release('n')
    time.sleep(1)
    keyboard.press('c')
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('e')
    keyboard.release('e')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


while True:
    antiafk()
    time.sleep(30)  # make function to sleep for 30 seconds
