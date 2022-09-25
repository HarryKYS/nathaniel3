import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome("/Users/harry/Desktop/OneMinPython/Python & Ruby/chromedriver")
browser = webdriver.Chrome("./chromedriver")
browser.get("https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=")
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/input').send_keys("무선마우스")
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/button[2]').click()
time.sleep(5)
browser.quit()