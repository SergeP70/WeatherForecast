# To collect the data
import requests
API_KEY = 'c132dc7b3fae3f9b558478477e0c8abd'


def get_data(place, forecast_days = None, type = None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)
    filtered_data = data['list']
    filtered_data = filtered_data[:8 * forecast_days]
    if type == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if type == "sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data('london', 3, "Temperature"))
