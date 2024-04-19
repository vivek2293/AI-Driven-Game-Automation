# Pattern detection
import time
import mss
import pyautogui

# aim_detect = pyautogui.locateOnScreen("./images/aim_complete.png", confidence=0.5)
# print(aim_detect)

aim_detect = pyautogui.locateCenterOnScreen("./images/aim_complete.png", confidence=0.6)
pyautogui.moveTo(aim_detect)