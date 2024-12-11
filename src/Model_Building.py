import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import pickle
import argparse
import time
import mlflow

ts = int(time.time())

processed_data_path = "./../artifacts/data/processed_data/"
model_path = "./../artifacts/models/raw_model/"

def model_building(processed_data_path,ts,model_path):
    X_train = pd.read_csv(os.path.join(processed_data_path,"X_train.csv"))
    y_train = pd.read_csv(os.path.join(processed_data_path,"y_train.csv"))
    shape = X_train.shape

    print("############ [INFO] Model building is started ############ ")

    model = LinearRegression()
    model.fit(X_train,y_train)

    pickle.dump(model,open(os.path.join(model_path,f"{ts}_model.pkl"),"wb"))
    mlflow.log_param("train_shape",shape)
    mlflow.sklearn.log_model(model, "Regression_Model")


    print("############ [INFO] Model Training Is Finished ############ ") 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path",default=model_path)
    parser.add_argument("--processed_data_path",default=processed_data_path)
    args = parser.parse_args()
    model_building(args.processed_data_path,ts,args.model_path)