import pyautogui
import time

# time.sleep(18)


def Locate(image_name, left=0, top=0, width=1920, height=1080):
    a, b, c, d, = pyautogui.locateOnScreen(
        f'images/{image_name}.png',
        region=(left, top, width, height),
        grayscale=True,
        confidence=0.9)
    return a, b


try:
    Locate("dark_dimension")
    print('found')
except TypeError:
    print("wrong")