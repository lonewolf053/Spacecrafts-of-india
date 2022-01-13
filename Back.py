from bs4 import BeautifulSoup as bs
import requests
import pickle
r=requests.get("https://www.isro.gov.in/all-missions-0")
soup=bs(r.content,'html.parser')
w=[]
m=soup.find('div',{'class':'view'}).parent.parent.find_all('div',{'class':'view'})
a=m[1].find_all("tr")
for g in range(1,len(a)):
  x=a[g].find_all('td')
  l=[]
  for i in x:
    y=i.text.replace('          ','')
    y=y.replace('\n','')
    y=y.replace('        ','')
    if y=='':
      l+=['no info']
    else:
      l+=[y]
  w.append(l)
with open('file1.bin', 'ab') as fp:
       pickle.dump(w, fp)
  
