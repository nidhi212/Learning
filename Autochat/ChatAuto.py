import pyautogui
import time
text="I love Rohu"
count=5
while count:
  time.sleep(2)
  pyautogui.typewrite(text)
  time.sleep(2)
  pyautogui.press("enter")
  count-=1