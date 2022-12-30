import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['User-Agent']= "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0" 
urls='https://www.thesecret.tv/the-secret-stories/page/{}/'
l =[]
for page in range(1,4):
    print(page)
    url = urls.format(page)
    r=s.get(url)
    #print(r)
    soup=bs(r.text,"html.parser")
    soup.find_all('div','post-story')
    #print(soup)
    #soup.find('div','date').text.strip()
    #print(soup.find('div','post-story').find('h2').find('a').text
    # print(soup.find('h4','author_name).text)
    story=soup.find_all('div','post-story')
    for i in story:
        name=i.find('h2').text
        date=i.find('div','date').text.strip()
        link=i.find('a').get('href')
        a_link=s.get(link)
        detail_soup=bs(a_link.text,'html.parser')
        submitted_by=detail_soup.find('h4','author_name').text
        author_location=detail_soup.find('span','author_location').text
        author=detail_soup.find('h2','mstory-title').text
        bio=detail_soup.find('p','author_bio').text
        description=detail_soup.find('div','mstory-content').text.strip()
        data ={
            'name':name,
            'date':date,
            'link':link,
            'subitted_by':submitted_by,
            'author_location':author_location,
            'bio':bio,
            'description':description
        }
        l.append(data)
        print(data)
    # print(date)
    # print(link)
    # print('')
    # print(submitted_by)
    # print(author)
    # print(author_location)
    # print(bio)
    # print(description)
    # print('')
    
    
df = pd.DataFrame(l)
df.to_excel('secrate.xlsx')
