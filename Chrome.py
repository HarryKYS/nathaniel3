# selenium 깔고 웹드라이버 깔기 크롬 드라이버 설치
# 주소창 -> chrome://version , 도움말 클릭
# chromedriver 설치 -> 다운후 워크스페이스에 붙이기



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome("/Users/harry/Desktop/OneMinPython/Python & Ruby/chromedriver")
browser = webdriver.Chrome("./chromedriver")
browser.get("http://daum.net")
# elem = browser.find_element("link text", "카페") # 중요
# # elem.get_attribute("class")
# browser.back() #뒤로가기
# browser.forward() # 앞으로 가
# browser.refresh() # 새로고침


# elem = browser.find_element(By.ID, "query")
# elem.click()
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements(By.TAG_NAME, "a")
# elem.get_attribute("href")
# for e in elem:
#     e.get_attirbute("href")

elem = browser.find_element(By.NAME, "q")
elem.click()
elem.send_keys("나도코딩")
elem.clear()
elem.send_keys("나도코딩")

elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()
browser.save_screenshot("지우기.png")
# browser.page_source
# browser.close() # 탭 1개 닫기 
# browser.quit() # 브라우저 전체 종료