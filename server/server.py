# from flask import Flask, request, jsonify
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import util
from fastapi.middleware.cors import CORSMiddleware


util.load_artifacts()

app = FastAPI()

class values(BaseModel):
    total_sqft: float
    bhk: int
    bath: int
    location: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers =["*"]
)
# @app.route('/get_location_names',methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add("Access-Control-Allow-Origin", "*")
#
#     return response
#
#
# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     bath = int(request.form['bath'])
#     bhk = int(request.form['bhk'])
#     location = request.form['location']
#
#     response = jsonify({
#         'estimated_price': util.predict_price(total_sqft, bath, bhk, location)
#     })
#     response.headers.add("Access-Control-Allow-Origin", "*")
#
#     return response




@app.get('/get_location_names')
async def get_location_names():
    return {'locations': util.get_location_names()}

@app.post('/predict')
async def predict(data:values):
    try:
        data = dict(data)
        total_sqft = data['total_sqft']
        bhk = data['bhk']
        bath = data['bath']
        location = data['location']
        price = util.predict_price(total_sqft,bath,bhk,location)
        return {'estimated_price': price}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    #     print("Running server for Bangalore Price Prediction")
    uvicorn.run(app,host='localhost', port=8000)
    # app.run()
