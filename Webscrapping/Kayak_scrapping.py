import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chromedriver_path = "C:/Users/elisa/Projet Python/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)

depart = ["PAR"]
destination = ["LON"]
date_aller = ["2022-04-01"]
date_retour = ["2022-04-08"]


def get_airlines(soup):
    airline = []
    airlines = soup.find_all('span', class_='codeshares-airline-names', text=True)
    for i in airlines:
        airline.append(i.text)
    return airline


def get_total_stops(soup):
    stops_list = []
    stops = soup.find_all('div', class_='section stops')

    for i in stops:
        for j in i.find_all('span', class_='stops-text'):
            stops_list.append(j.text)
    return stops_list


def get_price(soup):
    prices = []
    price = soup.find_all('div', class_='Flights-Results-FlightPriceSection right-alignment sleek')

    for i in price:
        for j in i.find_all('span', class_='price-text'):
            prices.append(j.text)
    return prices


def get_duration(soup):
    duration_list = []
    duration = soup.find_all('div', class_='section duration allow-multi-modal-icons')
    for i in duration:
        for j in i.find_all('div', class_='top'):
            duration_list.append(j.text)
    return duration_list

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

def remanier_2(prix):
    liste = []
    for i in range(len(prix)):
        liste.append(prix[i])
        liste.append(prix[i])
    return liste


for k in range(len(date_aller)):
    url = f"https://www.kayak.fr/flights/{depart[0]}-{destination[0]}/{date_aller[k]}/{date_retour[k]}"
    driver.get(url)

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
    #date = [date_aller[k] - date_retour[k]]* len(duree)
    df = pd.DataFrame({'Compagnie': compagnie, "Total d'escales": total_escales, 'Prix': prix, 'Duree': duree},
                      columns=['Compagnie', "Total d'escales", 'Prix', 'Duree'])
    df.to_excel(f'{depart[k]}_{destination[k]}.xlsx', index=False)