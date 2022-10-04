import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult') # frame 전환
elem = browser.find_element(By.XPATH, '//*[@id="html"]')
# elem.click()
# browser.switch_to.default_content() # 상위로 빠져 나옴
# 선택이 안되어 있으면 선택하기 
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면 석택하기 
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("선택 되어 있으므로 아무것도 안함")
time.sleep(5)
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면 석택하기 
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("선택 되어 있으므로 아무것도 안함")