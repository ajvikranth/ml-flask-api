import requests

BASE = 'http://127.0.0.1:5000/'

dataset = {
 "brand": "Datsun",
 "max_cost_price": 744000,
 "vehicle_age": 5,
 "km_driven": 40000,
 "seller_type": "Dealer",
 "fuel_type": "Petrol",
 "transmission_type": "Manual",
 "mileage": 20.63,
 "engine": 1198,
 "max_power": 67.0,
 "seats": 5 }


res = requests.post(url=BASE+'CarPricePridictor', json=dataset)
print(res)
print(res.json())











