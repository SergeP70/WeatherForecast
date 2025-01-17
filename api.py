# Get data from the open weather map org
import requests
from datetime import datetime

API_KEY = 'c132dc7b3fae3f9b558478477e0c8abd'
url2 = 'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c132dc7b3fae3f9b558478477e0c8abd'



def get_data(place, days, kind = None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    # 8 measurements per day, only collect days selected
    data = response['list'][:days*8]

    temperatures = []
    dates = []
    kinds = []
    for index in data:
        temperatures.append(index['main']['temp'])
        datum = datetime.fromtimestamp(index['dt']).strftime('%Y-%m-%d')
        dates.append(datum)
        kinds.append(index['weather'][0]['main'])

    print(kinds)
    return dates, temperatures, kinds



if __name__ == '__main__':
    get_data('london', 1)