# import requests

# # data = requests.get("https://fakestoreapi.com/products")
# # for i in data.json():
# #     print(i['title'])


# city = input("enter city : ")
# geocode = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}&key=9bea174c9eea44ff847f3080219cd0b9")
# data = geocode.json()

# lat = data['results'][0]['geometry']['lat']
# lan = data['results'][0]['geometry']['lng']
# data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lan}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric")
# cdata = data.json()
# print("City : ",cdata['name'])
# print("Temp : ",cdata['main']['temp'])
# print("Pressure : ",cdata['main']['pressure'])
# print("Humidity : ",cdata['main']['humidity'])