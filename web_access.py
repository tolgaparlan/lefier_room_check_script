import requests

#sends request to get list of rooms cheaper then 450 euros
def request_room_list(page):
    url = 'https://www.lefier.nl/Groningen/Zoeken/Kamers'
    data_to_send = {'ScrollPositionX':'0','pageNr':str(page),'Sortering':'Prijs'}
    re = requests.post(url,data=data_to_send) 
    if(page==2):
        #print(re.text)
        pass
    return re.text

#sends a basic get request to the passed url. Returns the result
def get_page(url):
    return requests.get(url).text
