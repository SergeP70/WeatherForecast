# Get data from the open weather map org
import requests

API_KEY = 'c132dc7b3fae3f9b558478477e0c8abd'


def get_data(place, days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()

    # 8 measurements per day, only collect the selected days
    data = response['list'][:days*8]

    # Make a list of dicts containing Date, Temperature and Kind, group by date
    conditions = []
    for index in data:
        conditions.append({'date': index['dt_txt'],
                           'temperature': index['main']['temp'],
                           'kind': index['weather'][0]['icon']})
    return conditions


if __name__ == '__main__':
    get_data('london', 1)