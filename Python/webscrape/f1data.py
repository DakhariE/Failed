import requests
from bs4 import BeautifulSoup as bs
import time

url = 'https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020'

html = requests.get(url)
info = bs(html.text, 'lxml')
dchar = info.find('div', class_='sc-jTUlZf cXGqQC')
print(dchar)