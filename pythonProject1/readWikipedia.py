from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import pandas as pd


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
print(len(tags))

links=[]
dict={}
for tag in tags:
   print (tag)
   links.append(tag.text)

df=pd.DataFrame(links)
df.to_csv('Links.csv', index=False)