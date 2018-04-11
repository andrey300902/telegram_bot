import requests


def search(coord):
    Cinemas = []
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "3c4a592e-c4c0-4949-85d1-97291c87825c"

    search_params = {
        "apikey": api_key,
        "text": "кинотеатр",
        "lang": "ru_RU",
        "ll": coord,
        "spn": "0.005,0.005",
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        # ...
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"]
    # Название организации.
    for i in organization:
        coords = i['geometries'][0]['coordinates']
        org = i["properties"]["CompanyMetaData"]
        org_name = org["name"]
        try:
            org_url = org["url"]
        except:
            org_url = 'Сайта нет'
        Cinemas.append([org_name, coords, org_url])

    # Получаем координаты ответа.
    return Cinemas
