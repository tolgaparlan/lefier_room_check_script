import requests

#sends request to get list of rooms cheaper then 450 euros
def request_room_list():
    url = 'https://www.lefier.nl/Groningen/Zoeken/Kamers'
    data_to_send = {'ScrollPositionX':'168','KamerprijsFilterIds':'0','KamerprijsFilterIds':'1','KamerprijsFilterIds':'2','pageNr':'','Sortering':'Prijs'}
    re = requests.post(url,data=data_to_send) 
    return re.text

#sends a basic get request to the passed url. Returns the result
def get_page(url):
    return requests.get(url).text
