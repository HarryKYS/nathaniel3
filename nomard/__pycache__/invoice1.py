import pyautogui
# pyautogui.mouseInfo()
import pyperclip
import sys
pyautogui.click(2199, 345, duration=1, button="left")
pyautogui.sleep(1)
con = pyautogui.confirm('계속 진행하시겠습니까?', buttons=['OK', 'Cancel'])

if con == 'OK':
    my_write = [1,2,3]
    for invoice in my_write:
        pyperclip.copy(invoice)
        pyautogui.click(2199, 345, button="left")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
    my_write(invoice)
   
else:
    sys.exit()