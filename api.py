# Get data from the open weather map org
import requests

API_KEY = 'c132dc7b3fae3f9b558478477e0c8abd'


def get_data(place, days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    # 8 measurements per day, only collect days selected
    data = response['list'][:days*8]

    temperatures = []
    dates = []
    kinds = []
    for index in data:
        dates.append(index['dt_txt'])
        temperatures.append(index['main']['temp'])
        kinds.append(index['weather'][0]['icon'])

    return dates, temperatures, kinds



if __name__ == '__main__':
    get_data('london', 1)