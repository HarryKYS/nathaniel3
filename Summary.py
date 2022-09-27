from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import pyautogui
import time
options = Options()
# browser = webdriver.Chrome("/Users/harry/Desktop/OneMinPython/Python & Ruby/chromedriver")
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
browser.get("https://mos.coupang.com/login")
time.sleep(1)

options.add_argument('--kiosk')
options.add_argument('--start-fullscreen')
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="okta-second-btn-span"]').click()
    # browser.find_element(By.XPATH, '//*[@id="loginInputInnerId"]').click()
time.sleep(2)
pyautogui.write("nathaniel3")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("dufrhd3304!@")
pyautogui.press("enter")
time.sleep(2)
# KPIs_Logistics 클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[9]/a/span[2]').click()
time.sleep(2)
    # browser.switch_to.frame('iframeResult')
# Delivery Status 클릭
browser.find_element(By.LINK_TEXT, 'Delivery Status').click()
time.sleep(2)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
browser.find_element(By.LINK_TEXT, 'Camp Delivery Summary V2').click()
time.sleep(2)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[1]/div/div[1]/input').click()
time.sleep(2)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}']".format(ctime.strftime("%d"))).click()
# time.sleep(2)
# 캠프칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(2)
# Deselect All 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/div/div[1]/div/button[2]').click()
time.sleep(2)
# 구리2 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/div/div[2]/ul/li[40]/a').click()
time.sleep(2)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
