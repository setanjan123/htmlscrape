

import openpyxl 
from urllib.request import urlopen
from bs4 import BeautifulSoup

book = openpyxl.load_workbook('websites.xlsx')

sheet = book.active
google =sheet['A1']
facebook=sheet['A2'] 

page = urlopen(google.value)
soup =  BeautifulSoup(page, "html.parser" ).encode('UTF-8')
sheet['B1']=soup

page = urlopen(facebook.value)
soup =  BeautifulSoup(page, "html.parser" ).encode('UTF-8')
sheet['B2']=soup

book.save('websites.xlsx')



