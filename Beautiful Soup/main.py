from bs4 import BeautifulSoup
import requests
import lxml

response=requests.get("https://news.ycombinator.com/news")

contents=response.text

soup=BeautifulSoup(contents,"lxml")
print(soup.title)


name_text=[]
name_link=[]

names = soup.find_all(name="a", class_="storylink")
for name in names:
    txt = name.text
    link = name.get("href")
    name_text.append(txt)
    name_link.append(link)

name_score=[]
sub_score=[]
scores = soup.find_all(name="span", class_="score")
for score in scores:
    name_score.append(score.text.split()[0])
for i in name_score:
    sub_score.append(int(i))

largest=max(sub_score)
sub=sub_score.index(largest)

print(name_text[sub])
print(name_link[sub])
print(sub_score[sub])
print(largest)
print(sub)
