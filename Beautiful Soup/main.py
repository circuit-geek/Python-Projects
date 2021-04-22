# import lxml


# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tags in all_anchor_tags:
#     print(tags.getText())


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page , "html.parser")
article_tag = soup.find(name="a", class_="storylink")
print(article_tag.getText)

