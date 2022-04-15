
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

page = requests.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1245")

page

print(page)

soup = bs(page.content, 'html.parser')

print(soup)