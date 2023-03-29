# from bs4 import BeautifulSoup
# import requests

# link=requests.get("https://www.imdb.com/title/tt13345606/?ref_=hm_tpks_tt_t_3_pd_tp1_pbr_ic")

# soup=BeautifulSoup(link.content,"html.parser")

# print(soup.prettify())
# rating=soup.find('h1')
# print(rating.text)





# # from bs4 import BeautifulSoup
# # import requests
# # link=requests.get(f"https://www.imdb.com/title/tt4425200/").text
# # bs = BeautifulSoup(link,"html.parser")

# # for movie in bs.findAll('td','title'):
# #     title = movie.find('a').contents[0]
# #     genres = movie.find('span','genre').findAll('a')
# #     genres = [g.contents[0] for g in genres]
# #     runtime = movie.find('span','runtime').contents[0]
# #     rating = movie.find('span','value').contents[0]
# #     year = movie.find('span','year_type').contents[0]
# #     imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
# #     print (title, genres,runtime, rating, year, imdbID)


# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.imdb.com/chart/top'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# titles = soup.select('td.titleColumn a')
# for title in titles:
#     print(title.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

movieslist=pd.read_csv('D:\\Learning only\\imdb_id_moviename__toprated.csv')
# print(movieslist.iloc[2,1])
list1=['tt0068646','tt0108052','tt0110912']
ratings=[]
for i in range(10):
        
    options = webdriver.ChromeOptions()
        # a=webdriver.Chrome()
    options.add_experimental_option("detach",True)
    options.headless = False
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\path\\to\\chromedriver.exe')
    driver.get(f'https://www.imdb.com/title/{movieslist.iloc[i][1]}/')
    print ("Headless Chrome Initialized")
    # button = driver.find_element(by=By.CLASS_NAME,value="sc-e457ee34-1 gvYTvP")
    # print(button)
    # elem=driver.find_element_by_class_name("sc-e457ee34-1 gvYTvP")
    # print(elem.text)
    # plants = driver.find_elements(By.TAG_NAME, "h1")
    # print(plants.text)
    # fruit = driver.find_element(By.CSS_SELECTOR,".sc-e457ee34-1 gvYTvP")
    # print(fruit)
    with open("ratings.html","w",encoding='utf-8') as f:
                    f.write(driver.page_source)
    with open("D:\\Learning only\\ratings.html",encoding="utf-8") as htmlfile:
            soup=BeautifulSoup(htmlfile,"html.parser")
            try:
                rating=soup.find("span",class_="sc-e457ee34-1 squoh") #sc-e457ee34-1 squoh
                print(rating.text)
                ratings.append(rating.text) 

            except AttributeError as e:
                rating=soup.find("span",class_="sc-e457ee34-1 gvYTvP") #sc-e457ee34-1 squoh
                print(rating.text)
                ratings.append(rating.text) 
    driver.close()
for i in range(10):
       print(movieslist.iloc[i][0],end=" ")
       print(ratings[i])
