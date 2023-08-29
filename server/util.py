import json
import pickle
import numpy as np

__data_columns = None
__location = None
__model = None


def predict_price(sqft, bath, bhk, location):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __location


def load_artifacts():
    print("loading artifacts... start")
    global __data_columns
    global __location
    global __model

    with open(
            r"C:\Users\admin\Documents\Data_Science\Projects\Bangalore_Price_Prediction\server\artifacts\columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open(r"C:\Users\admin\Documents\Data_Science\Projects\Bangalore_Price_Prediction\server\artifacts\bangalore_price_prediction_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("loading artifacts... done")


if __name__ == "__main__":
    load_artifacts()
    print(__location)
    print(predict_price(1000, 3, 3, "1st Phase JP Nagar"))
