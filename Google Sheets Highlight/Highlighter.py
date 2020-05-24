from pynput import keyboard
import pyautogui as pyauto
import os


Comboz = [
    {keyboard.Key.esc},
    {keyboard.Key.esc}
]

current = set()

def execute():
    os.system("aplay Begin.wav&")
    pyauto.moveTo(x=709, y=209)
    pyauto.click()
    pyauto.moveTo(x=807, y=308)
    pyauto.click()
def on_press(key):
    if any ([key in Combo for Combo in Comboz]):
        current.add(key)
        if any(all(k in current for k in Combo) for Combo in Comboz):
            execute()

def on_release(key):
    if any([key in Combo for Combo in Comboz]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()