"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import requests
from bs4 import BeautifulSoup

def get_so_last_page(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_so_job(html):
  title = html.find("h2", {"class": "mb4"}).find("a")["title"]
  company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive=False)
  company = company.get_text(strip=True)
  job_id = html["data-jobid"]
  return {
      "title": title,
      "company": company,
      "link": f"https://stackoverflow.com/jobs/{job_id}"
  }


def extract_so_jobs(last_page, URL):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_so_job(result)
      jobs.append(job)
  return jobs

def extract_wework_jobs(second_url):
  jobs = []
  result = requests.get(second_url)
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find("section", {"class":"jobs"}).find_all("li")[:-1]
  for result in results:
    link = 'https://weworkremotely.com/'+result.find("a", recursive = False)["href"]
    title = result.find("a", recursive = False).find("span",{"class":"title"}).string
    company = result.find("a", recursive = False).find("span",{"class":"company"}).string
    jobs.append({'title':title, 'company':company, "link":link})
  return jobs

def extract_remote_jobs(third_url):
  jobs=[]
  headers = {'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98\Safari/537.36'), } 
  result = requests.get(third_url, headers=headers)
  soup = BeautifulSoup(result.text, 'html.parser')
  tables = soup.find(id="jobsboard").find_all("tr")
  for table in tables:
    try:
      title = table.find("h2",{"itemprop":"title"}).get_text()
      company = table['data-company']
      link = 'https://remoteok.io'+table['data-href']
      jobs.append({'title': title, 'company':company, 'link':link})      
    except:
      pass
  return jobs

def get_jobs(word):
  first_url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  second_url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  third_url = f"https://remoteok.io/remote-dev+{word}-jobs"
  last_page = get_so_last_page(first_url)
  
  try : 
    so_job = []
    we_job = []
    re_job = []
    so_job += extract_so_jobs(last_page, first_url)
    we_job += extract_wework_jobs(second_url)
    re_job += extract_remote_jobs(third_url)
  except:
    pass

  jobs = so_job + we_job + re_job

  return jobs

