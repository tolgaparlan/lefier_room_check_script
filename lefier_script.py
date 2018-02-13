#!/usr/bin/env python3
# tolgaparlan@gmail.com 2017

from web_access import *
from data_handle import *

# arrays to hold suitable and non-suitable rooms
rooms = []

lookUpUrl = 'https://woningen.lefier.nl/Groningen/Zoeken/Kamers'
baseUrl = 'https://woningen.lefier.nl'
pageNum = 1

while True:
  cheap_rooms_response = request_room_list(lookUpUrl, pageNum)
  soup_rooms = create_soup(cheap_rooms_response)

  # extract the links to the results
  room_links = extract_links(baseUrl, soup_rooms)
  if len(room_links) == 0:
    break

  # access all the links, parse the data
  for link in room_links:
    room_page = get_page(link)
    room_page_soup = create_soup(room_page)
    room_info = get_room_info(room_page_soup, link)
    rooms.append(room_info)

  pageNum += 1

# print everything
print(rooms)
