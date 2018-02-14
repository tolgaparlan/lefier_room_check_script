#!/usr/bin/env python3
# tolgaparlan@gmail.com 2017

from web_access import *
from data_handle import *
import os
import os.path

# arrays to hold suitable and non-suitable rooms
rooms = {}

lookUpUrl = 'https://woningen.lefier.nl/Groningen/Zoeken/Kamers'
baseUrl = 'https://woningen.lefier.nl'
fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
fileName = 'last_reading.txt'
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
    room_details = get_room_name(room_page_soup, link)
    rooms[room_details['name']] = room_details['link']

  pageNum += 1

if os.path.isfile(fileLocation+'/'+fileName):
  f = open(os.path.join(fileLocation, fileName),'r')
  raw_data = f.read()
  f.close()

  parsed_past_rooms = eval(raw_data)
  comparison = compare(rooms, parsed_past_rooms)
  if comparison['difference']:
    printPretty(comparison['newAddedRooms'])
  else:
    print("Nothing New")
else:
  print("Old rooms data not found")

# write all the room information to a file
f = open(os.path.join(fileLocation, fileName),'w')
f.write(str(rooms))
