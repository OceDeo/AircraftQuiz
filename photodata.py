import requests
import random
from bs4 import BeautifulSoup
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
 
def find_match():
    pass
 
def scrap_data(list_of_models, special_cases, q_number=10, query_limit=50):
    # counter to limit the number of questions to 10
    i = 0
    # counter to limit the number of queries to 40
    query_counter = 0
 
    # init questions list
    questions = []
 
    while i < q_number:
        number = random.randint(1,9223337)
        page = requests.get('http://jetphotos.com/photo/' + str(number))
        query_counter += 1
        #print('Number of queries: ' + str(query_counter))
        soup = BeautifulSoup(page.content, 'html.parser')
        if query_counter >= query_limit:
            break
        # if photo was removed it redirects to .../new
        if 'new' in page.url:
            pass
 
        # check if manufacturer is in the page
        elif any(manufacturer in soup.text[0:100] for manufacturer in list_of_models):
            aircraft = soup.text[0:100].split('| ')[1].split(' ')
            # extract manufacturer and model, special case for manufacturers with spaces
            if any(manufacturer in soup.text[0:100] for manufacturer in special_cases):
                manufacturer = str(aircraft[0]) + ' ' + str(aircraft[1])
                model = aircraft[2]
            else:
                manufacturer = aircraft[0]
                model = aircraft[1]
 
            # extract photo url
            url_start_index = str(page.content).find('https://cdn.jetphotos.com/full/')
            url = page.content[url_start_index-42:url_start_index+11]
            if url.startswith(b'https://') and url.endswith(b'.jpg'):
                prediction = process.extractOne(model, list_of_models[manufacturer], scorer=fuzz.partial_ratio)
                if prediction[1] < 75:
                    continue
                print(str(manufacturer) + ', ' + str(model) + ', ' + 'I think it\'s: ' + prediction[0] + ', ' 
                      'and I\'m ' + str(prediction[1]) + '% certain, ' + str(url))
                i += 1
                questions.append([manufacturer, model, url])
            else:
                #print('Passing: ' + str(url))
                pass
    print('Total queries: ' + str(query_counter))
    return questions
 
if __name__ == "__main__":
    list_of_models = {
        'Airbus': ['A300', 'A310', 'A318', 'A319', 'A320', 'A321', 'A330', 'A340', 'A350', 'A380'],
        'Boeing': ['717', '727', '737-1', '737-2', '737-3', '737-4', '737-5', '737-6', '737-7', '737-8',
                   '737-9', '737-8 MAX', '747-1', '747-2', '747SP', '747-3', '747-4', '747-8', '757-2',
                   '757-3',
                   '767-2', '767-3', '767-4', '777-2', '777-3', '787-8', '787-9'],
        'Embraer': ['E170', 'E175', 'E190', 'E195', 'ERJ-145', 'EMB-120'],
        'Antonov': ['AN-124', 'AN-225'],
        'ATR': ['ATR-42', 'ATR-72'],
        'Bombardier': ['Q400', 'CRJ-200', 'CRJ-900', 'CRJ-700' 'Global'],
        'Cessna': ['152', '172', '182', 'Citation'],
        'Fokker': ['50', '70', '100'],
        'Tupolev': ['134'],
        'Ilyushin': ['62'],
        # 'McDonnell Douglas': ['1'],
        # 'General Dynamics': ['1'],
        # 'Lockheed Martin': ['1'],
        # 'British Aerospace': ['1'],
    }
 
    # special cases - space in the manufacturer name
    special_cases = ['McDonnell Douglas', 'General Dynamics', 'Lockheed Martin', 'British Aerospace']
 
    questions = scrap_data(list_of_models, special_cases, q_number=10, query_limit=80)
    print('k')