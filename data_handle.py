from bs4 import BeautifulSoup

# creates a soup object from given html


def create_soup(html):
  return BeautifulSoup(html, 'html.parser')

# extract links from the rooms page


def extract_links(baseUrl, soup):
  links = soup.find_all('a', {"class": "details"})
  return [baseUrl + link['href'] for link in links]

# returns the room info from the html


def get_room_info(soup,link):
  info_table = soup.find_all('table', {'class': 'info'})
  name = soup.find('h1')
  return {name:link}

# parses the room info into a dict, returns it with the price
