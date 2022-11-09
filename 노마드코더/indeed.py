# from optparse import Option
from urllib import response
from requests import get
from bs4 import BeautifulSoup
# from wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
def get_page_count():
    browser = webdriver.Chrome("./chromedriver")
    browser.get("https://kr.indeed.com/jobs?q=python&l&from=searchOnHP&vjk=cb7f5860d7ca04e3")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        return 1
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count
print(get_page_count())
def extract_indeed_jobs():
# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev=shm-usage")

# # browser = webdriver.Chrome("/Users/harry/Desktop/OneMinPython/Python & Ruby/chromedriver")
# browser = webdriver.Chrome(options=options)
    pages = get_page_count()
    results = []
    for page in range(pages):
        browser = webdriver.Chrome("./chromedriver")
        browser.get(f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&start={page*10}&vjk=8a0f5a8857c12e2e")

        # base_url = "https://kr.indeed.com/jobs?q="
        # search_term = "python"
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        job_list = soup.find('ul', class_="jobsearch-ResultsList css-0")
        jobs = job_list.find_all('li', recursive = False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_date = {
                            'link' : f"https://kr.indeed.com{link}",
                            'company' : company.string.replace(",", " "),
                            'location' : location.string.replace(",", " "),
                            'position' : title.replace(",", " ")
                        }
                results.append(job_date)
    return results

jobs = extract_indeed_jobs()
print(len(jobs))
        # if response.status_code != 200:
        #     print("Can't request website")
        # else:
        #     soup = BeautifulSoup(response.text,"html.parser")
        #     job_list = soup.find('ul', class_="jobsearch-ResultsList")
        #     jobs = job_list.find_all('li')
        #     print(len(jobs))
