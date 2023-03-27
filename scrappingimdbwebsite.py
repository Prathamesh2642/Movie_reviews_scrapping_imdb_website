from bs4 import BeautifulSoup
import requests


link=requests.get("https://www.imdb.com/title/tt6710474/reviews?ref_=tt_urv").text
soup=BeautifulSoup(link,'html.parser')
# print(soup.prettify())
print(soup.find('div',class_="review-container"))

maincont=soup.find('div',class_="review-container")
print(maincont.span.text)
print(soup.find("div",class_="text show-more__control").text)
