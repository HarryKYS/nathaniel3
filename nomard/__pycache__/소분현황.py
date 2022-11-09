from datetime import datetime
from pickle import TRUE
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
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Delivery Status 클릭
browser.find_element(By.LINK_TEXT, 'Delivery Status').click()
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
browser.find_element(By.LINK_TEXT, 'Camp Arrival Status').click()
time.sleep(0.7)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[1]/div/input').click()
time.sleep(0.7)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 
 
# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(0.7)
# 캠프칸 클릭
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div/div/button').click()
# browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/form/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(0.7)
# select All 클릭
# Wave 2 클릭
browser.find_element(By.LINK_TEXT, 'Wave2').click()

# 캠푸 유형 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/button').click()
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.7)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()


browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])
# KPIs_Logistics 클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[9]/a/span[2]').click()
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Delivery Status 클릭
browser.find_element(By.LINK_TEXT, 'Delivery Status').click()
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
browser.find_element(By.LINK_TEXT, 'Camp Arrival Status').click()
time.sleep(0.7)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[1]/div/input').click()
time.sleep(0.7)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 
 
# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(0.7)
# 캠프칸 클릭
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div/div/button').click()
# browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/form/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(0.7)
# select All 클릭
# Wave 2 클릭

browser.find_element(By.LINK_TEXT, 'Sameday').click()
# 캠푸 유형 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/button').click()
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.7)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(2)

browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[2])
# KPIs_Logistics 클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[9]/a/span[2]').click()
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Delivery Status 클릭
browser.find_element(By.LINK_TEXT, 'Delivery Status').click()
time.sleep(0.7)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
browser.find_element(By.LINK_TEXT, 'Camp Arrival Status').click()
time.sleep(0.7)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[1]/div/input').click()
time.sleep(0.7)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 
 
# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(0.7)
# 캠프칸 클릭
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div/div/button').click()
# browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/form/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(1.5)
# select All 클릭
# Wave 2 클릭

# browser.find_element(By.LINK_TEXT, 'Select All').click()
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/button[1]').click()
time.sleep(0.7)

# 캠푸 유형 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/button').click()
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.7)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()




