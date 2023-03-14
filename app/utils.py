import pickle
import json
import numpy as np
import pandas as pd
import os
import CONFIG

class Prediction():
    def __init__(self):
        print(os.getcwd())

    def load_raw(self):
        with open(CONFIG.MODEL_PATH, "rb") as model_file:
            self.model = pickle.load(model_file)

        with open(CONFIG.COL_NAMES) as col_file:
            self.column_names = json.load(col_file)

    print("we are in load data")

    def predict_specie(self, data):
        self.load_raw()
        self.data = data
        user_input = np.zeros(len(self.column_names["column_names"]))
        sepal_length = self.data['html_sep_length']
        sepal_width = self.data['html_sep_width']
        petal_length = self.data['html_pet_length']
        petal_width = self.data['html_pet_width']

        user_input[0] = sepal_length
        user_input[1] = sepal_width
        user_input[2] = petal_length
        user_input[3] = petal_width

        print(f"{user_input=}")

        result = self.model.predict([user_input])

        if result == [0]:
            return "predicted specie is SETOSA"
        elif result == [1]:
            return "predicted specie is VERGINICA"
        elif result == [2]:
            return "predicted specie is VERCICOLOR"
        else:
            return "enter proper dimentions"


if __name__ == "__main__":
    pred_obj = Prediction()
    pred_obj.load_raw()



