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
# file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file_location = "/usr/share/lefier_script"
fileName = 'last_reading.txt'
pageNum = 1

while True:
  cheap_rooms_response = request_room_list(lookUpUrl, pageNum)
  # print(cheap_rooms_response)
  # break
  soup_rooms = create_soup(cheap_rooms_response)

  # extract the room names and their links
  room_links = extract_names_links(baseUrl, soup_rooms)
  
  if len(room_links) == 0:
    break

  rooms.update(room_links)

  pageNum += 1

if os.path.isfile(file_location+'/'+fileName):
  f = open(os.path.join(file_location, fileName),'r')
  raw_data = f.read()
  f.close()

  parsed_past_rooms = eval(raw_data)
  comparison = compare(rooms, parsed_past_rooms)
  if comparison['difference']:
    printPretty(comparison['newAddedRooms'])
  else:
    print("Nothing New")
else:
  print("Old rooms data not found.\nCreated new file under " + file_location)

# write all the room information to a file
if(not os.path.exists(file_location)):
  os.mkdir(file_location)
f = open(os.path.join(file_location, fileName),'w')
f.write(str(rooms))
