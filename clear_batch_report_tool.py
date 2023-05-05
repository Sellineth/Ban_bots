import pyautogui
import time
import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

timer = 0.5

for i in range(10,-1,-1):
    print (" Starting in ", i, " ", end="\r")
    time.sleep(1)

coords_image = pyautogui.locateOnScreen("batch_thing.png", region=(0, 492, 66, 536 - 492))# 65, 538, 66, 492
coords_image1 = pyautogui.locateOnScreen("batch_thing_empty.png", region=(0, 492, 66, 536 - 492))# 65, 538, 66, 492

while True:
    if coords_image is not None:
        x, y = pyautogui.center(coords_image)
        pyautogui.click(x, y)
        print(x, y)
        time.sleep(timer)
        break
    elif coords_image1 is not None:
        x, y = pyautogui.center(coords_image1)
        pyautogui.click(x, y)
        print(x, y)
        time.sleep(timer)
        break
    else:
        time.sleep(timer)

coords_image2 = pyautogui.locateOnScreen("increse_size.png", region=(291, 499, 330 - 291, 538 - 499))# 324, 538, 330, 499
while True:
    if coords_image2 is not None:
        x, y = pyautogui.center(coords_image2)
        pyautogui.click(x, y)
        print(x, y)
        time.sleep(timer)
        break
    else:
        time.sleep(timer)

while True:
    coords_image3 = pyautogui.locateOnScreen("remove.png", region=(722, 588, 768 - 722, 626 - 588))# 722, 588, 768, 626
    coords_image4 = pyautogui.locateOnScreen("remove_mouse.png", region=(722, 588, 768 - 722, 626 - 588))# 722, 588, 768, 626
    if coords_image3 is not None:
        x, y = pyautogui.center(coords_image3)
        time.sleep(0.5)
        pyautogui.click(x, y)
        print(x, y)
        pyautogui.screenshot("remove_mouse.png", region=(722, 588, 768 - 722, 626 - 588))# 722, 588, 768, 626
        break
    elif coords_image4 is not None:
        x, y = pyautogui.center(coords_image4)
        pyautogui.click(x, y)
        print(x, y)
        time.sleep(timer)