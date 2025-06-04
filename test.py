import pyautogui
import pygetwindow
windows = pygetwindow.getWindowsWithTitle("Tracking")
windows.activate()
x,y = windows.topleft
widhth , height = windows.size
screenshot = pyautogui.screenshot(region=(x, y, widhth, height))
screenshot.save("screenshot.png")
