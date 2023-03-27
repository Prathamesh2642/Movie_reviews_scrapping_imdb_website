from bs4 import BeautifulSoup
import requests
import pandas as pd


link=requests.get("https://www.imdb.com/title/tt10366206/reviews?ref_=tt_urv").text
soup=BeautifulSoup(link,'html.parser')
# print(soup.prettify())
print(soup.find('div',class_="review-container"))

maincont=soup.find('div',class_="review-container")
print(maincont.span.text)
print(soup.find("div",class_="text show-more__control").text)

# print(soup.find("section",class_="article"))

mainreview=soup.find("section",class_="article")

# for i in soup.find_all("div",class_="review-container"):
#     print(len(soup.find_all("div",class_="review-container")))
#     mainreview=i.find("div",class_="review-container")
#     print(mainreview.find("div",class_="text show-more__control").text)
#     print("hello")


# print(reviewlist)

# for i in reviewlist:
    # print(i)
# reviewlist1=reviewlist.find_all("div",class_="text show-more__control")
# print(reviewlist1)

reviewlist=[]
for i in soup.find_all("div",class_="text show-more__control"):
    print(len(soup.find_all("div",class_="text show-more__control")))
    # print(i.find("div",class_="text show-more__control"))
    # print(i.text)
    reviewlist.append(i.text)
for i in reviewlist:
    print(i)

df=pd.DataFrame(reviewlist)
print(df)
df.to_csv('Moviereviews1.csv')