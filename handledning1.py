import requests
import json

data = requests.get("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json")

data_json= data.json()

# print(data.status_code)
# print(data_json["timeSeries"][0]['parameters'])
number_of_observations = 0
for time in data_json['timeSeries']:
    for data_point in time['parameters']:
        if data_point['name']=='t':
            print(data_point['values'][0])
            number_of_observations +=1

print(f'Antal timmar är {number_of_observations}')
# for weather_point in data_json["timeSeries"][0]['parameters']:
#     if weather_point['name']=='t':
#         print(weather_point['values'][0])
# meny_val = "asdfasdfw"

# match meny_val:
#     case 1:
#         pass
#     case 2:
#         print('vi kör någon funktion')
#     case _  :
#         print('fel inmata')