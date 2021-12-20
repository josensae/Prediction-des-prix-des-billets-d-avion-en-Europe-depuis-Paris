#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import numpy as np
import datetime
from time import sleep


# In[10]:



chromedriver_path = "C:/Users/bombi/Downloads/chromedriver_win32/chromedriver.exe"
#chromedriver_path = 'C:/Users/José/Documents/ENSAE Paris/2A/Python Pour le Data Scientist/chromedriver_win32/chromedriver.exe'


# In[20]:


driver = webdriver.Chrome(chromedriver_path)


# In[5]:


def get_airlines(soup):
    airline = []
    airlines = soup.find_all('span',class_='codeshares-airline-names',text=True)
    for i in airlines:
        airline.append(i.text)
    return airline
    
def get_total_stops(soup):
    stops_list = []
    stops = soup.find_all('div',class_='section stops')

    for i in stops:
        for j in i.find_all('span',class_='stops-text'):
               stops_list.append(j.text)
    return stops_list

def get_price(soup):
    prices = []
    price = soup.find_all('div',class_='Flights-Results-FlightPriceSection right-alignment sleek')

    for i in price:
        for j in i.find_all('span', class_='price-text'):
            prices.append(j.text)
    return prices

def get_duration(soup):
    duration_list = []
    duration = soup.find_all('div' , class_='section duration allow-multi-modal-icons')
    for i in duration:
        for j in i.find_all('div',class_='top'):
            duration_list.append(j.text)
    return duration_list


# In[6]:


def remanier(compagnie):
    liste = []
    for i in range(len(compagnie)):
        if  ',' in compagnie[i] : 
            j= 0
            while compagnie[i][j]!=',' :
                j+=1
            liste.append(compagnie[i][:j])
            liste.append(compagnie[i][j+1:])
        else :
            liste.append(compagnie[i])
            liste.append(compagnie[i])
    return liste


# In[7]:


def remanier_2(prix):
    liste = []
    for i in range(len(prix)):
        liste.append(prix[i])
        liste.append(prix[i])
    return liste


# In[21]:


depart = ["PAR"]
Destinations = ["OSL"]
date_aller = ["04/01/2022"]
date_retour = ["04/08/2022"]
date_a = pd.to_datetime(date_aller)
date_r = pd.to_datetime(date_retour)
result = pd.DataFrame([])

for k in range(1): 
    new_date_a = date_a + datetime.timedelta(days = 7*k)
    new_date_r = date_r + datetime.timedelta(days = 7*k)
    date_time_a = new_date_a.astype(str)
    date_time_r = new_date_r.astype(str)
    destination = ["OSL"]
    date_aller = [date_time_a]        
    date_retour = [date_time_r]
    url = f"https://www.kayak.fr/flights/{depart[0]}-{destination[0]}/{date_aller[0]}/{date_retour[0]}"
    driver.get(url)
    sleep(15)
    
    try:
        show_more_button = driver.find_element_by_xpath('//a[@class = "moreButton"]')
    except:
        input("Please solve the captcha then enter anything here to resume scraping.")

    while True:
        try:
            show_more_button.click()
            driver.implicitly_wait(10)
        except:
            break


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    compagnie = remanier(get_airlines(soup))
    total_escales = get_total_stops(soup)
    prix = remanier_2(get_price(soup))
    duree = get_duration(soup)
    df = pd.DataFrame({'Compagnie':compagnie, "Total d'escales":total_escales , 'Prix': prix, 'Duree': duree}, 
                        columns = ['Compagnie', "Total d'escales", 'Prix', 'Duree'])
    df["Destination"] = "Oslo"
    df["Distance"] = 1344
    df["Date_aller"] = 20220401
    df["Date_retour"] = 20220408
    df["Date_aller"] = pd.to_datetime(df["Date_aller"], format = '%Y%m%d') + datetime.timedelta(days = 7*k)
    df["Date_retour"] = pd.to_datetime(df["Date_retour"], format = '%Y%m%d') + datetime.timedelta(days = 7*k)
    result = pd.concat([result, df], axis = 0)


# In[19]:


df


# In[9]:


result.to_excel('oslo.xlsx', index = False) 
result


# In[28]:


fichiers = ["C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/oslo.xlsx", "C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/oslo_2.xlsx","C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/moscou.xlsx","C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/madrid.xlsx","C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/madrid_2.xlsx", "C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/londres.xlsx","C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/londres_1.xlsx", "C:/Users/bombi/OneDrive/Documents/Fichiers_Scrappes/athenes.xlsx"]
fichier_combine= pd.DataFrame()

for fichier in fichiers:
    df=pd.read_excel(fichier)
    fichier_combine= fichier_combine.append(df, ignore_index= True)


# In[30]:


fichier_combine


# In[27]:


#fichier_combine.to_excel('fich-comb.xlsx')


# In[31]:


df_final = fichier_combine


# In[32]:


df_final


# In[ ]:




