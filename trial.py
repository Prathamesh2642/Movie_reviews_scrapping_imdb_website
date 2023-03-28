from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests


def clickloadmore():
    options = webdriver.ChromeOptions()
    # a=webdriver.Chrome()
    options.add_experimental_option("detach",True)
    options.headless = False
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\path\\to\\chromedriver.exe')
    driver.get('https://www.imdb.com/title/tt10366206/reviews?ref_=tt_urv')
    print ("Headless Chrome Initialized")
    button = driver.find_element(by=By.CLASS_NAME,value="ipl-load-more__button")
    count=0
    while(True):
        # button.click()
        # time.sleep(5)
        # button.click()
        # time.sleep(5)
        # button.click()
        try:
            while(True):
                count+=1
                time.sleep(2)
                button.click()
                print(count)
        except Exception as e:
            with open("D:\\Learning only\\Movie_reviews_scrapping_imdb_website\\movies.html","w",encoding='utf-8') as f:
                f.write(driver.page_source)
            
            print(driver.page_source)
            print(e)
            break
        print("done")
        

clickloadmore()