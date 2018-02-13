import requests

# sends request to get list of available rooms in the page
def request_room_list(url, page):
  data_to_send = {'ScrollPositionX': '0',
                  'pageNr': str(page), 'Sortering': 'Prijs'}
  re = requests.post(url, data=data_to_send)
  return re.text

# sends a basic get request to the passed url. Returns the result
def get_page(url):
  return requests.get(url).text
