import pyautogui
import cv2
import numpy as np
import time
import pyperclip
from paddleocr import PaddleOCR

def screenshot(x, y, width, height, path=""):
    image = pyautogui.screenshot(region=(x, y, width, height))
    if path != "":
        image.save(path)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image

def ocr(x, y, width, height, language="ch"):
    paddle = PaddleOCR(use_angle_cls=True, lang=language, show_log=False)
    image = screenshot(x, y, width, height)
    results = paddle.ocr(image)
    text = ""
    for result in results:
        if result is None:
            continue
        for word in result:
            text += word[-1][0] + " "
    return text.strip()

def paste(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    pyperclip.copy("")

def clear_input():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")

def study():
    while True:
        text = ocr(883, 704, 161, 35)
        print(text)
        if "继续学习" in text:
            pyautogui.click(960, 717)
            time.sleep(3)
            continue
        text = ocr(779, 547, 376, 143)
        print(text)
        if "防挂机" in text:
            pyautogui.click(934, 650)
        time.sleep(3)

if __name__ == "__main__":
    study()
