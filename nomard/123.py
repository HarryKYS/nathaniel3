from bs4 import BeautifulSoup
import requests

term = input("What do you want to search for?")
results = []
def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("h2",itemprop="title")
    for job in jobs:
       print(job.string)
    # write your ✨magical✨ code here
  else:
    print("Can't get jobs.")

extract_jobs(term)


# term = input("What do you want to search for?")
# results = []

# url = f"https://remoteok.com/remote-{term}-jobs"
# request = requests.get(url, headers={"User-Agent": "Kimchi"})
# if request.status_code == 200:
#   soup = BeautifulSoup(request.text, "html.parser")
#   jobs = soup.find_all("h2",itemprop="title")
#   for job in jobs:
#       print(job.string)
  
