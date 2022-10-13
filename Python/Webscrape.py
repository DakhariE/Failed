import requests
from bs4 import BeautifulSoup as bs

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = bs(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
  pub_date = job.find('span', class_ ='sim-posted').span.text
  if 'few' in pub_date:
    company = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
    skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
    print(f'Company name:{company}Required skills: {skills} {pub_date}')
