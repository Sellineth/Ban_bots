import pyautogui
import time
import win32gui
import win32con
import os

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

#time.sleep(5)

script_dir = os.path.dirname(os.path.abspath(__file__))
os.path.join(script_dir)
'''
pyautogui.screenshot("send_message.png", region=(1145, 954, 1273 - 1145, 997 - 954))# 1145, 954, 1273, 997
pyautogui.screenshot("batch_thing_empty.png", region=(0, 492, 66, 536 - 492))# 65, 538, 66, 492
pyautogui.screenshot("increse_size.png", region=(291, 499, 330 - 291, 538 - 499))# 324, 538, 330, 499
'''
#pyautogui.screenshot("batch_thing.png", region=(0, 492, 66, 536 - 492))# 65, 538, 66, 492
#pyautogui.screenshot("remove.png", region=(722, 588, 768 - 722, 626 - 588))# 722, 588, 768, 626
pyautogui.screenshot("remove_mouse.png", region=(722, 588, 768 - 722, 626 - 588))# 722, 588, 768, 626