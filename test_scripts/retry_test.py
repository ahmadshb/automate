import pyautogui
import time


def Check(img):
    try:
        a, b, c, d = pyautogui.locateOnScreen(
            f'images/{img}.png',
            region=(1568, 926, 236, 81),
            grayscale=True,
            confidence=0.9)
    except:
        print(f'{img} not found')
    else:
        print(f'{img} found')


print('checking in 5 seconds')
time.sleep(5)

Check('retry_button')
Check('retry_button_dark')