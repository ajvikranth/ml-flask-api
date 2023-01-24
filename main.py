from flask import Flask, request, jsonify 
from flask_restful import Api, Resource 
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)



pipe = joblib.load('pipeline1.pkl')


class Car_price_pridictor(Resource):
    def get(self):
        return {"about" : "this is an used car price pridiction api for more details please visit https://ajvikranth.vercel.app/"}

    def post(self):
        data = request.json
        print(data)
        try:
            seats_n = int(data["seats"])
            
            if seats_n not in range(2,10):
                return "invalid input value", 400

            if seats_n in [2,3,4]:
                seats_c = 'below_5' 
            elif seats_n in [5,6]:
                seats_c = '5_and_6'
            elif seats_n in [7,8,9]:
                seats_c = 'above_6'

            
            ar = [data["brand"],int(data["max_cost_price"]),int(data["vehicle_age"]),int(data["km_driven"]),data["seller_type"],data["fuel_type"],data["transmission_type"],float(data["mileage"]),float(data["engine"]),float(data["max_power"]),seats_c]
            
            ar= np.array([ar])
            ar = ar.reshape(1,11)
            
            prediction = pipe.predict(ar)
            print(prediction)
            
            return  jsonify({'prediction' : prediction[0]})

        except:
            return "invalid input value", 400

        
           
        
api.add_resource(Car_price_pridictor,"/CarPricePridictor/")

if __name__ == "__main__":
    app.run(debug=False)

# dataset = {
#  "brand": "Datsun",
#  "max_cost_price": 744000,
#  "vehicle_age": 5,
#  "km_driven": 40000,
#  "seller_type": "Dealer",
#  "fuel_type": "Petrol",
#  "transmission_type": "Manual",
#  "mileage": 20.63,
#  "engine": 1198,
#  "max_power": 67.0,
#  "seats": "5_and_6"}    