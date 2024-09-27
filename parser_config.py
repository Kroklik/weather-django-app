import pycountry

# Получаем все страны и их русские названия
country_codes = {country.alpha_2: country.name for country in pycountry.countries}
weather_status_codes = {
    'Clear': 'Ясно☀️',
    'Clouds': 'Облачно☁️',
    'Rain': 'Дожди☔️',
    'Snow': 'Снег❄️',
    'Haze': 'Туман😶‍🌫️',
    'Drizzle': 'Морось'

}

cities = [
    ('Tashkent', 'UZ'),  # Узбекистан
    ('London', 'GB'),  # Великобритания
    ('Moscow', 'RU'),  # Россия
    ('New York', 'US'),  # США
    ('Berlin', 'DE'),  # Германия
    ('Paris', 'FR'),  # Франция
    ('Rome', 'IT'),  # Италия
    ('Madrid', 'ES'),  # Испания
    ('Tokyo', 'JP'),  # Япония
    ('Sydney', 'AU'),  # Австралия
    ('Canberra', 'AU'),  # Австралия
    ('Osaka', 'JP'),  # Япония
    ('New Delhi', 'IN'),  # Индия
    ('São Paulo', 'BR'),  # Бразилия
    ('Cape Town', 'ZA'),  # Южноафриканская Республика
    ('Kuala Lumpur', 'MY'),  # Малайзия
    ('Seoul', 'KR'),  # Южная Корея
    ('Cairo', 'EG'),  # Египет
    ('Buenos Aires', 'AR'),  # Аргентина
    ('Santiago', 'CL'),  # Чили
    ('Lima', 'PE'),  # Перу
    ('Hanoi', 'VN'),  # Вьетнам
    ('Dhaka', 'BD'),  # Бангладеш
    ('Bangkok', 'TH'),  # Таиланд
    ('Islamabad', 'PK'),  # Пакистан
    ('Brussels', 'BE'),  # Бельгия
    ('Athens', 'GR'),  # Греция
    ('Dublin', 'IE'),  # Ирландия
    ('Abu Dhabi', 'AE'),  # ОАЭ
    ('Jakarta', 'ID'),  # Индонезия
    ('Nairobi', 'KE'),  # Кения
    ('Casablanca', 'MA'),  # Марокко
    ('Reykjavik', 'IS'),  # Исландия
    ('Copenhagen', 'DK'),  # Дания
    ('Warsaw', 'PL'),  # Польша
    ('Stockholm', 'SE'),  # Швеция
    ('Lisbon', 'PT'),  # Португалия
    ('Budapest', 'HU'),  # Венгрия
    ('Prague', 'CZ'),
]