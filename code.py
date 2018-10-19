from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

link="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html"
# link='http://www.baidu.com/'
s = requests.Session()
headers={
"User-Agent" :"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Upgrade-Insecure-Requests": "1"
        }
response = s.get(link,allow_redirects=False,headers=headers)
print(response.status_code)
print(response.request.headers)
print(response.text)
text = BeautifulSoup(response.text,"lxml")

#tree = html.fromstring(page.text)
#soup = BeautifulSoup(open(link))
