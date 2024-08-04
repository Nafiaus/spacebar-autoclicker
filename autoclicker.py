# pip install pynput

import time

from pynput.keyboard import Key, Controller

running = True
count = 11700

keyboard = Controller()

while running:
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    if(count == 67000):
        running = False
