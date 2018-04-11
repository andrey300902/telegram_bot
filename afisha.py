from bs4 import BeautifulSoup
import requests

def cinemastar(url):
    Films = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    name = soup.find_all('div', class_='film_name')
    for i in name:
        Films.append(i.get_text())
    return Films

def karofilm(url):
    Films = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    name = soup.find_all('div', class_='afisha-item is-visible col-lg-2 col-md-3 col-sm-3 col-xs-12')
    for i in name:
        Films.append(i.attrs["data-search"])
    return Films

def mirage(url):
    Films = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    films = soup.find_all('div', class_='item-film')
    for i in films:
        name = i.find('a', class_='red')
        Films.append(name.get_text())
    return Films

def kinomax(url):
    Films = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    films = soup.find_all('div', class_='fs-09 pt-2 post-slick-item')
    for i in films:
        Films.append(i.get_text())
    return Films

def cinemapark(url):
    Films = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    films = soup.find_all('div', class_='afisha-item afisha-film')
    for i in films:
        name = i.find('div', class_='film-title')
        Films.append(name.get_text())
    return Films