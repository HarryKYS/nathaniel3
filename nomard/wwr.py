from requests import get
from bs4 import BeautifulSoup
def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# at = input("입력")
# search_term = at
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text,"html.parser")
        jobs = soup.find_all('section', class_="jobs")
        #  print(response.text )
        # print(len(jobs))
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            # 마지막을 제거해주거는것
            job_posts.pop(-1)
            for post in job_posts:
                # print(post)
                # print("///////////")
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, region = anchor.find_all('span', class_='company')
                title = anchor.find('span', class_='title')
                # string을 쓰면 HTML 테그 나오지 않고 글자만 나온다
                # print(company.string, kind.string, region.string, title.string)
                # print("---------------------")
                job_date = {
                    'link' : f"https://weworkremotely.com/{link}",
                    'company' : company.string,
                    'kind' : kind.string,
                    'region' : region.string,
                }
        return results
