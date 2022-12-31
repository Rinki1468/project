import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
s=Session()
s.headers['User-Agent']= "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0" 
urls='https://www.jiomart.com/c/groceries/fruits-vegetables/219?prod_mart_groceries_products_popularity%5Bpage%5D={}'
l=[]
for page in range(1,4):
    print('page',page)
    url=urls.format(page)
    r=s.get(url)
    listsoup=bs(r.text,"html.parser")
    #print(r)
    item=listsoup.find_all('div','col-md-3 p-0')
    for i in item:
        name=i.find('span','clsgetname').text
        price=i.find('span',{'id':'final_price'}).text
        img_link=i.find('span','cat-img').find('img',attrs={'data-sizes':'auto'}).get('data-src')
        link=i.find('a','category_name prod-name').get('href')
        r_link=s.get('https://www.jiomart.com'+link)
        soup=bs(r_link.text,"html.parser")
        stock=soup.find('div',{'id':'is_in_stock'}).text
        seller=soup.find('div','seller_details').text
        brand_name=soup.find('div','brand_name').text
        icons=soup.find('span','food_icons') 
       #raiting=soup.find('div','').find('').
        #print(name)
        #print(price)
        data={'name': name,
           'price': price,
           'img_link' :img_link, 
           'link' :link ,
           'seller':seller,
           'brand_name' :brand_name,
           'icons' :icons,
           'stock':stock
    }
    l.append(data)
    print(l)    
df = pd.DataFrame(l)
df.to_excel('jio_pagi.xlsx')