import requests
url="https://twitter.com/narendramodi/with_replies"
page=requests.get(url)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.text,'html.parser')
containers=soup.findAll("div",{"class":"content"})
filename="tweets.csv"
f=open(filename,'w')
i=1
for container in containers:
    print(i)
    tiws=container.findAll("div",{"class":"js-tweet-text-container"})
    i=i+1
    tiws1=tiws[0].text
    print(tiws1)
    f.write(tiws1+"\n")
f.close()
