from bs4 import BeautifulSoup
import re

# creates a soup object from given html


def create_soup(html):
  return BeautifulSoup(html, 'html.parser')

# extract names with corresponding links from the soup of the rooms page


def extract_names_links(baseUrl, soup):
  room_links = {}
  all_links = soup.find_all('a', href=True)
  for link in all_links:
    if link['href'] and link.string and re.search("\w+\s[1-9]", link.string):
      room_links[link.string] = baseUrl + link['href']
  return room_links

# checks if everything in dict1 is also in dict2
def compare(dict1, dict2):
  diff = {}
  diff['difference'] = False
  diff['newAddedRooms'] = {}

  for item in dict1:
    if item not in dict2:
      diff['difference'] = True
      diff['newAddedRooms'][item] = dict1[item]
  return diff

def printPretty(dic):
  for item in dic:
    print(item + " : " + dic[item])