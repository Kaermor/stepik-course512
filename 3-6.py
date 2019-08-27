# import requests
# # import json
#
# api_url = "http://api.openweathermap.org/data/2.5/weather"
#
# city = input("City? ")
#
# params = {
#     'q': city,
#     'appid': '11c0d3dc6093f7442898ee49d2430d20',
#     'units': 'metric'
# }
#
# res = requests.get(api_url, params=params)
# # print(res.status_code)
# # print(res.headers["Content-Type"])
# # print(res.json())
# data = res.json()
# template = 'Current temperature in {} is {}'
# print(template.format(city, data['main']['temp']))

# -----------------------------------------
import requests

template = 'http://numbersapi.com/{}/math?json=true'
with open('dataset_24476_3.txt', 'r') as f, open('output_3-6.txt', 'w') as fout:

    for line in f:
        api_url = template.format(line.strip())
        res = requests.get(api_url)
        # print(res.json())
        data = res.json()
        # print(data['found'])
        if data['found'] is True:
            print('Interesting')
            fout.write('Interesting\n')
        else:
            print('Boring')
            fout.write('Boring\n')