from  selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
url='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=webdriver.Chrome('chromedriver.exe')
browser.get(url)
time.sleep(1)

def scrape():
    headers=['name','light_year_from_earth','planet_mass','stellar_magnitude','discovery_date']
    planet_data=[]
    for i in range(0,222):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for ul in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags=ul.find_all('li')
            temp_list=[]
            for index,li  in enumerate(li_tags):
                if index==0:
                    temp_list.append(li.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li.contents[0])
                    except:
                        temp_list.append('')
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrap.csv','w') as f:
        csvwrite=csv.writer(f)
        csvwrite.writerow(headers)
        csvwrite.writerows(planet_data)

           
            

scrape()
