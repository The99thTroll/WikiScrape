from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

startURL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/albrino/WikiScrape/chromedriver")
browser.get(startURL)

time.sleep(10)

def scrape():
    headers = ["Name", "Light-Years", "Mass", "Radius"]
    planetData = []
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr in soup.find_all("tr"):
        tdTags = tr.find_all("td")
        tempList = []
        for index, tdTag in enumerate(tdTags):
            if index == 1:
                try:
                    tempList.append(tdTag.find_all("a")[0].contents)
                except:
                    tempList.append(tdTag.contents[0])
            else:
                if index == 3 or index == 5 or index == 6:
                    try:
                        tempList.append(tdTag.contents[0])
                    except:
                        pass
        planetData.append(tempList)

    with open("scraper2.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planetData)
        
scrape()