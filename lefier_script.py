#!/usr/bin/env python3
#tolgaparlan@gmail.com 2017

from web_access import *
from data_handle import *
import requests

#Get the month number from the user
print('This script will give you rooms becoming available after (inclusive) your preferred month')
month_num = int(input('Enter the Closest Suitable Month NUMBER: '))

#request list of rooms cheaper than 450 euros, make a soup
cheap_rooms_response = request_room_list()
soup_rooms = create_soup(cheap_rooms_response)

#extract the links to the results
room_links = extract_links(soup_rooms)

#arrays to hold suitable and non-suitable rooms
suitable_rooms = []
non_suitable_rooms = []

#access all the links, parse the data 
for link in room_links:
    room_page = get_page(link)
    room_page_soup = create_soup(room_page)
    room_info = get_room_info(room_page_soup)
    parsed_room_info = parse_room_info(room_info[0],room_info[1])
    #check if the date is after august
    if date_suitable(parsed_room_info[1],month_num):
        suitable_rooms.append(parsed_room_info)
    else:
        non_suitable_rooms.append(parsed_room_info)

#check if there are any suitable rooms, if not so, print everything
if suitable_rooms:
    print(len(suitable_rooms), ' suitable room(s) are found. Details:\n')
    print_room_info(suitable_rooms)
else:
    print('No suitable rooms found. Printing all:\n')
    print_room_info(non_suitable_rooms)

