import requests
import random
from bs4 import BeautifulSoup
import time

i = 0
limit = 10

while i < limit:
    number = random.randint(1,9223337)
    page = requests.get(f'http://jetphotos.com/photo/{str(number)}') 
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('title')
    if 'new' in page.url:
        print('photo removed')
        pass
    else:
        aircraft = title.string.split(' | ')[1:2]
        print(aircraft[0])
        i += 1
    time.sleep(1)

