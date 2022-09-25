import pyautogui
import pyperclip
import sys
pyautogui.click(2199, 345, duration=1, button="left")
pyautogui.sleep(1)
con = pyautogui.confirm('계속 진행하시겠습니까?', buttons=['OK', 'Cancel'])

from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active
lst = []
for r in ws.rows:
    if r[0].value is None:
        continue
    lst.append([])
    for c in r:
        lst[-1].append(c.value)
    # print(lst[-1])
lst.pop(0)

if con == 'OK':
    for invoice in lst:
        pyperclip.copy(invoice[-1])
        pyautogui.click(2199, 345, button="left")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
    else:
        sys.exit()



