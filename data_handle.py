from bs4 import BeautifulSoup
import re

#creates a soup object from given html
def create_soup(html):
    return BeautifulSoup(html, 'html.parser')

#extract links from the rooms page
def extract_links(soup):
    link_reg = re.compile('\/Groningen\/Woning\/Studentenkamer')
    links = soup.find_all('a',{"class":"details"})
    page_base = 'https://www.lefier.nl'
    return [page_base+link['href'] for link in links]

#returns the room info from the html
def get_room_info(soup):
    info_table = soup.find_all('table',{'class':'info'})
    price = soup.find('h2',{'class':'price'})
    return [info_table[0],price]

#parses the room info into a dict, returns it with the price
def parse_room_info(info_table,price):
    i = 0
    room_dict = {}
    while i<len(info_table.find_all('td')):
        room_dict[info_table.find_all('td')[i].text]=info_table.find_all('td')[i+1].text
        i=i+2
    return [price.text.strip(),room_dict]

#check if the date is after august
def date_suitable(room_info,month):
    date = room_info['Te huur vanaf'].split('-')
    return int(date[1])>=month

#check if price is below the given 
def price_suitable(room_price,max_price):
    room_price = int(room_price.split()[1].split(',')[0])
    return room_price <= max_price

#print all rooms in the list with the price
def print_room_info(room_info):
    for room in room_info:
        print(room[0])
        for info in room[1]:
            print(info,' : ',room[1][info])
        print('\n')
