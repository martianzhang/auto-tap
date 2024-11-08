from pynput import mouse
import time

# 记录上一次点击的时间
last_click_time = None

def on_click(x, y, button, pressed):
    global last_click_time

    # 如果是右键点击，停止监听
    if button == mouse.Button.right:
        return False

    if pressed:
        # 计算时间间隔
        current_time = time.time()
        if last_click_time is not None:
            interval = current_time - last_click_time
            print("time.sleep(", round(interval, 2), ")")

        # 更新上一次点击的时间
        last_click_time = current_time
        print("pyautogui.click(", x, ",", y, ")")

# 开始监听鼠标事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
