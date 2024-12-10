import pandas as pd
import os
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
import argparse

processed_data_path = "./artifacts/data/processed_data/"
model_path = "./artifacts/models/raw_model/"


def find_latest_model(model_path):
    files = os.listdir(model_path)
    temp = [float(file.split("_")[0]) for file in files]
    return files[temp.index(max(temp))]

def model_evalaution(processed_data_path,model_path):
    X_test = pd.read_csv(os.path.join(processed_data_path,"X_test.csv"))
    y_test = pd.read_csv(os.path.join(processed_data_path,"y_test.csv"))

    raw_model = find_latest_model(model_path)
    model = pickle.load(open(os.path.join(model_path,raw_model),"rb"))

    y_pred = model.predict(X_test)

    r_score = r2_score(y_test,y_pred)
    MAE = mean_absolute_error(y_test,y_pred)
    MSE = mean_squared_error(y_test,y_pred)
    print(f"r_score = {r_score} MAE = {MAE} MSE = {MSE}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path",default=model_path)
    parser.add_argument("--processed_data_path",default=processed_data_path)
    args = parser.parse_args()
    model_evalaution(args.processed_data_path,args.model_path)