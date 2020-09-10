import sys
import time
import pyautogui
import pyperclip

targets = pyautogui.getWindowsWithTitle('Notepad')
if len(targets) < 1:
    print("No notepad windows open. Open an instance and try again. ")
    sys.exit()

npW = targets[0]
npW.activate()
pyautogui.click(npW.left + 50, npW.top + 80)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

test = pyperclip.paste()
print(test)

#npWindow.close()
