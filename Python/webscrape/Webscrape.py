import requests
from bs4 import BeautifulSoup as bs
import time

unskill = input('Put some skill that you dont know > ' )
print(f"filtering out {unskill}")

def find_jobs():
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
  soup = bs(html_text, 'lxml')
  jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
  for index, job in enumerate(jobs):
    pub_date = job.find('span', class_ ='sim-posted').span.text
    if 'few' in pub_date:
      company = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
      skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
      more_info = job.header.h2.a['href']
      if unskill not in skills:
        with open(f'index.txt', 'a') as f:
          f.write(f'Company name: {company.strip()} \n')
          f.write(f'Required skills: {skills.strip()} \n')
          f.write("Link: " + more_info + "\n")
        print(f'File saved: {index}')
if __name__=='__main__':
  while True:
    find_jobs()
    time_wait = 10
    print(f"Waiting {time_wait} minutes...")
    time.sleep(time_wait * 60)