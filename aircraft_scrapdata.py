import requests
import random
from bs4 import BeautifulSoup
import time


def findplane(aircraft_list):
    i = 0
    while i < 1:
        number = random.randint(1,9223337)
        page = requests.get(f'http://jetphotos.com/photo/{str(number)}') #
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('title')
        if 'new' in page.url:
            pass
        else:
            aircraft = title.string.split(' | ')[1:2]
            manufacturer = aircraft[0].split(' ')[0]
            try:
                model = aircraft[0].split(' ', 1)[1]
            except:
                model = None
            if manufacturer in aircraft_list:
                for model_check in aircraft_list[f'{manufacturer}']:
                    if model_check in model:
                        image = soup.find("img", class_ = "large-photo__img")
                        i += 1
                        return aircraft[0].split(' ', 1), image['srcset']
                    else:
                        pass
        time.sleep(.1)



'''def gen_question(aircraft_list):
    counter = 0
    lim = 100
    while counter < lim:
        aircraft, imagelink = findplane(aircraft_list)
        print(aircraft[0])
        print(aircraft[1])
        print(imagelink)
        counter +=1
        print(f'----------  {counter}  -------------------')
    

generate_question(aircraft_list)'''