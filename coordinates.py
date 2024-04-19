# Get screen region co-ordinate manually
import pyautogui
import time

# Get mouse position
while True:
    brk = input("Press Enter to get position or any other key to break: ")
    if(brk):
        break;
    x, y = pyautogui.position()
    print(f"Current mouse position: x={x}, y={y}")
    time.sleep(0.5)