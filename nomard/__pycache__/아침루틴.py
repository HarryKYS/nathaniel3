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

time.sleep(1)
pyautogui.write("nathaniel3")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("dufrhd3304!@")
pyautogui.press("enter")
time.sleep(2)
# KPIs 클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[2]/a').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Order/Shipped Status 클릭
browser.find_element(By.LINK_TEXT, 'Order/Shipped Status').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Camp Order Status 클릭
browser.find_element(By.LINK_TEXT, 'Camp Order Status').click()
time.sleep(0.5)
# 날짜칸 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[1]/div/div[1]/input').click()
time.sleep(0.5)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
ftime = datetime.timedelta(days=1)
ntime = ctime - ftime
if ntime.strftime("%d") == "1":
    browser.find_element(By.XPATH, "//td[text()='{}']".format(ntime.strftime("%-d"))).click()
else:
    browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ntime.strftime("%-d"))).click()
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
# browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ntime.strftime("%d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 

# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(2)

# pacel칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/button/div').click()
time.sleep(0.5)
# pacel 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/div/div/ul/li[1]/a/span[2]').click()
time.sleep(0.5)
# #셀렉트 칸 클릭
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/button').click()
# time.sleep(2)
# #셀렉트 올  클ㅣ
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
# time.sleep(2)

# 캠프칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div[1]/div/button').click()
time.sleep(0.5)
# 구리2 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div[1]/div/div/div[3]/ul/li[72]/a').click()
time.sleep(0.5)
# 쉬핑타입 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[5]/div/div[1]/button/div/div').click()
time.sleep(0.5)

# 당일배송 클릭
browser.find_element(By.LINK_TEXT, '일반배송 (Standard)').click()
browser.find_element(By.LINK_TEXT, '간선배송 (TrunkRoad)').click()
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[5]/div/div[1]/div/div[2]/ul/li[6]/a/span[2]').click()
time.sleep(0.5)


# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(1)

# # 엑셀 다운로드

# browser.find_element(By.XPATH, '//*[@id="excel-download"]').click()
# time.sleep(3)

# browser.find_element(By.XPATH, '//*[@id="downloadExportedExcelLink"]').click()
###########################################
###########################################
###########################################
###########################################
# 당일배송

# browser.execute_script('window.open("https://mos.coupang.com/login");')
browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])
# KPIs

browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[2]/a/span[2]').click()
    # browser.find_element(By.XPATH, '//*[@id="loginInputInnerId"]').click()
# browser.find_element(By.LINK_TEXT, 'KPIs').click()

# browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[2]/a').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Order/Shipped Status 클릭
browser.find_element(By.LINK_TEXT, 'Order/Shipped Status').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Camp Order Status 클릭
browser.find_element(By.LINK_TEXT, 'Camp Order Status').click()
time.sleep(0.5)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[1]/div/div[1]/input').click()
time.sleep(0.5)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 

# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(2)

# pacel칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/button/div').click()
time.sleep(0.5)
# pacel 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/div/div/ul/li[1]/a/span[2]').click()
time.sleep(0.5)
# #셀렉트 칸 클릭
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/button').click()
# time.sleep(2)
# #셀렉트 올  클ㅣ
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
# time.sleep(2)

# # 캠프칸 클릭
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div[1]/div/button').click()
# time.sleep(2)
# # 구리2 클릭
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div[1]/div/div/div[3]/ul/li[72]/a').click()
# time.sleep(2)
# 쉬핑타입 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[5]/div/div[1]/button/div/div').click()
time.sleep(0.5)
# 당일배송 클릭
browser.find_element(By.LINK_TEXT, '당일배송 (Sameday)').click()
time.sleep(0.5)


# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(1)

# # 엑셀 다운로드

# browser.find_element(By.XPATH, '//*[@id="excel-download"]').click()
# time.sleep(3)

# browser.find_element(By.XPATH, '//*[@id="downloadExportedExcelLink"]').click()

###########################################
###########################################
###########################################
###########################################
# 오더 
browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[2])
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[9]/a/span[2]').click()
time.sleep(1)
    # browser.switch_to.frame('iframeResult')
# Delivery Status 클릭
browser.find_element(By.LINK_TEXT, 'Delivery Status').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
browser.find_element(By.LINK_TEXT, 'Camp Delivery Summary V2').click()
time.sleep(0.5)
# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[1]/div/div[1]/input').click()
time.sleep(0.5)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 
 
# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(2)
# 캠프칸 클릭
time.sleep(0.5)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/button').click()
# browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/form/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(0.5)
# Deselect All 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/div/div[1]/div/button[2]').click()
time.sleep(0.5)
# 구리2 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div[1]/div/div/div[2]/ul/li[40]/a').click()
time.sleep(0.5)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(1)

############
###########



#######가공 나게 
#######가공 나게 
#######가공 나게 
#######가공 나게 
#######가공 나게 
browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[3])

# Logistic Aashboard 클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[8]/a/span[2]').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Order/Shipped Status 클릭
browser.find_element(By.LINK_TEXT, 'Worker Level').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')

# 날짜칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[1]/div/div/input').click()
time.sleep(0.5)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 

# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(2)

# #셀렉트 칸 클릭
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/button').click()
# time.sleep(2)
# #셀렉트 올  클ㅣ
# browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
# time.sleep(2)

# 캠프칸 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/button').click()
time.sleep(0.5)
# 구리2 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[2]/div/div/div[1]/div/ul/li[74]/a').click()
time.sleep(0.5)
# 쉬핑타입 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[3]/div/div/button/div').click()
time.sleep(0.5)
# CPF 클릭
browser.find_element(By.LINK_TEXT, 'CPF').click()

# 배송타입 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div/div/button').click()
time.sleep(0.5)
# 셀렉트 올 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[4]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.5)
# wave 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[5]/div/div/button').click()
time.sleep(0.5)

# 셀렉트 올 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[5]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.5)

# 그룹 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[6]/div/div/button').click()
time.sleep(0.5)
# 셀렉트 올 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[6]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.5)

# 배송대상 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[7]/div/div/button').click()
time.sleep(0.5)

# 셀렉트 올 선택
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div[1]/div/div[7]/div/div/div[1]/div[1]/div/button[1]').click()
time.sleep(0.5)
# 배송 성과 보기
browser.find_element(By.XPATH, '//*[@id="columnFilterForm"]/div[1]/span').click()
time.sleep(0.5)

# 배송 시간 보기
browser.find_element(By.XPATH, '//*[@id="columnFilterForm"]/div[3]/span').click()
time.sleep(1)




# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()

time.sleep(1.5)

browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[4])
time.sleep(1.5)


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
time.sleep(1)

browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[5])
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
time.sleep(1)

browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[6])
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

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/button[1]').click()
time.sleep(0.9)

# 캠푸 유형 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/button').click()
time.sleep(0.7)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/div[3]/div/div/div/div[1]/div/button[1]').click()
time.sleep(0.7)
# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(1)

# 노멀 다운 받아 붙이기 
browser.execute_script('window.open("https://mos.coupang.com");')
time.sleep(2)
browser.switch_to.window(browser.window_handles[7])

# Logistics Dashboard  클릭
browser.find_element(By.XPATH, '//*[@id="m_ver_menu"]/ul/li[8]/a/span[2]').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Delivery List by PDD 클릭
browser.find_element(By.LINK_TEXT, 'Delivery List by PDD').click()
time.sleep(0.5)
    # browser.switch_to.frame('iframeResult')
# Camp Delivery Summary V2 클릭
time.sleep(2)
# 날짜칸 클릭

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div/div/div[1]/div/div[1]/input').click()
time.sleep(0.5)
# 날자 클릭 이전 날짜 
ctime = datetime.datetime.now()
# ftime = datetime.timedelta(days=1)
# ntime = ctime - ftime
# # browser.find_element(By.XPATH, "//td[text()='26']").click()
browser.find_element(By.XPATH, "//td[text()='{}'][not(contains(@class,'old day'))]".format(ctime.strftime("%-d"))).click()
# browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/[td/@class='today active day']/td[text()='{}']".format(ctime.strftime("%d"))).click()

# browser.find_element(By.XPATH, "//td[@class='today active day']").click()  # today day 
 
# browser.find_element(By.XPATH, "//td[@class='today day']").click()
# time.sleep(2)
# 캠프칸 클릭
time.sleep(0.5)

browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div/div/div[2]/div/div/button').click()
# browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[1]/div/form/div[1]/div/div[2]/div[1]/div/button').click()
time.sleep(0.5)
# Deselect All 클릭
# 구리2 클릭
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div/div/div[2]/div/div[1]/div/div/ul/li[67]/a').click()
time.sleep(0.5)
browser.find_element(By.XPATH, '//*[@id="searchForm"]/div/div/div/div[3]/div[2]/div/button').click()
time.sleep(0.5)


browser.find_element(By.LINK_TEXT, 'NORMAL').click()
time.sleep(0.5)



# 서치바 클릭
browser.find_element(By.XPATH, '//*[@id="search"]').click()
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="download-excel"]').click()
time.sleep(5)
browser.find_element(By.XPATH,'//*[@id="downloadExportedExcelLink"]').click()
