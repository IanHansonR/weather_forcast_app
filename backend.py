import requests

API_KEY = "cab39ae87f71239baecf4f77c8a06837"


def get_data(place, days=None, type=None):
    url = F"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    if type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type == "Sky Condition":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    test = get_data(place="Tokyo", days=3, type="Sky Condition")
    print(test)
    print(len(test))

