# 1. mac moseinfo RGB Color 나오지 않는거 해결 
# ㄴ 해결 후 답 적기 
# 2.mac 창 tex sizs 작게 하는거 확인해보기 

from selenium import webdriver
import time



browser = webdriver.Chrome("./chromedriver")
browser.set_window_size(1000, 1500)
browser.get("http://naver.com")

 

if __name__ == '__main__':
    main()