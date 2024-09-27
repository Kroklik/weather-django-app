import pycountry
from pyowm import OWM
from concurrent.futures import ThreadPoolExecutor, as_completed
from parser_config import cities, weather_status_codes, country_codes

# Инициализация OWM
owm = OWM('7ccda81177fd5dccbe423584b59a92a7')
mgr = owm.weather_manager()


def fetch_weather(city_country):
    city, country = city_country
    observation = mgr.weather_at_place(f'{city}, {country}').to_dict()
    celsius_temp = str(observation['weather']['temperature']['temp'] - 273.15)[:5]
    return {
        'country': country_codes.get(country, 'Ошибка'),
        'city': observation['location']['name'],
        'temperature': celsius_temp,
        'wind': observation['weather']['wind']['speed'],
        'weather_status': weather_status_codes.get(observation['weather']['status'], 'Ошибка')
    }


def weather_parser() -> list:
    queryset_dict = []

    # Используем ThreadPoolExecutor для параллельных запросов
    with ThreadPoolExecutor(max_workers=15) as executor:
        future_to_city = {executor.submit(fetch_weather, city_country): city_country for city_country in cities}

        for future in as_completed(future_to_city):
            city_country = future_to_city[future]
            try:
                result = future.result()
                queryset_dict.append(result)
            except Exception as exc:
                print(f'{city_country} generated an exception: {exc}')

    return queryset_dict


# Вызов функции
weather_data = weather_parser()
