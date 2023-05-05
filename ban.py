import pyautogui
import pyperclip
import time
import os
import win32gui
import win32con
from sys import exit


hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
bot_list = []

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "badbots.txt")

timer = 0.5

if os.path.isfile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        bot_list.extend(lines)
else:
    print(f"Error: {filename} not found.")
    exit()

#print(bot_list)
print("\n", len(bot_list))

for i in range(10,-1,-1):
            print (" Starting in: ", i, end="\r")
            time.sleep(1)

coords_image = pyautogui.locateOnScreen("send_message.png", region=(1145, 954, 1273 - 1145, 997 - 954))# 1145, 954, 1273, 997
k = 0
while True:
    if coords_image is None:
        time.sleep(timer)
    else:
        x, y = pyautogui.center(coords_image)
        pyautogui.click(x, y)
        print(x, y)
        for i in range(len(bot_list)):
            index = bot_list[i]
            pyperclip.copy(f"/ban {index} bot")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(0.5)
            print(index)
            time.sleep(timer)
        break
