from bs4 import BeautifulSoup
import requests
from lxml import html
import re
import json

def get_city(href,headers,tr='citytr'):
    base_href="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"
    url=base_href+href
    response= requests.get(url,allow_redirects=False,headers=headers)
    bsobj=BeautifulSoup(response.content,'lxml')
    tr_list=bsobj.find_all(class_=tr)
    city_list=[]
    for row in tr_list:
        a_list=row.find_all('a')
        value=a_list[0].text
        city=a_list[1].text
        matchobj=re.search('直辖',city)
        if matchobj:
            href=a_list[1].get('href')
            city_list=city_list+get_city(href,headers,tr='countytr')
        else:
            city_list.append({"value":value,"text":city})
    return city_list
    

link="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html"
# link='http://www.baidu.com/'
#s = requests.Session()
headers={
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Upgrade-Insecure-Requests": "1"
        } 
response = requests.get(link,allow_redirects=False,headers=headers)
#response.enconding ='gb2312'
#print(response.encoding)
print(response.status_code)
#print(response.request.headers)
str=response.content.decode('gb2312')
#print(str)
bsobj=BeautifulSoup(response.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
a_list=bsobj.find(class_='provincetable').find_all('a')
province=[]
for a in a_list:
    href=a.get('href')
    name=a.text
    id=href.split('.')[0]
    matchobj=re.search('市',name)
    if matchobj:
        href=id+'/'+id+'01.html'
        city_list=get_city(href,headers,tr='countytr')
    else:
        city_list=get_city(href,headers)
    province.append({"id":id,"name":name,"children":city_list})
with open('city.json','w') as fp:
    json.dump(province,fp,ensure_ascii=False) #需要在open时加上encoding=‘utf-8'
    