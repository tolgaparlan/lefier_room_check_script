from bs4 import BeautifulSoup

# creates a soup object from given html


def create_soup(html):
  return BeautifulSoup(html, 'html.parser')

# extract links from the rooms page


def extract_links(baseUrl, soup):
  links = soup.find_all('a', {"class": "details"})
  return [baseUrl + link['href'] for link in links]

# returns the room info from the html


def get_room_name(soup,link):
  name = soup.find('h1').string
  return {'name':name, 'link':link}

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