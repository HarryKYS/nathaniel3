import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome("/Users/harry/Desktop/OneMinPython/Python & Ruby/chromedriver")
browser = webdriver.Chrome("./chromedriver")
browser.get("https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=")
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/input').send_keys("무선마우스")
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/button[2]').click()
# browser.execute_script('window.scrollTo(0, 500)') # 모니터 해상도 만큼
# # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 제일 마지막까지 내리기 
# 동적 페이지에 대해서 마지막까지 스크롤 내리기 
interval = 2 # 2초에 한번식 스크롤 내리기 
prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 모니터 해상도 만큼
    time.sleep(interval)
    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면
        break
    prev_height = curr_height
# 맨위로 올리기
browser.execute_script('window.scrollTo(0, 0)')
# time.sleep(5)
# browser.quit()