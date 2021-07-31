# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:53:12 2021

@author: Vaibhav
"""

from urllib.request import urlopen
url='https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films'
print(url)

data=urlopen(url)
print(data)

html=data.read()
print(html)
data.close()

from bs4 import BeautifulSoup as soup
aveng_soup=soup(html,'html.parser')
aveng_soup

aveng_soup.h1

aveng_soup.find_all('h1',{})

tables=aveng_soup.find_all('table',{'class':'wikitable' })
len(tables)