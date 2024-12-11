import pandas as pd
from sklearn.model_selection import train_test_split
import os
import argparse
import mlflow

test_size = 0.20
Target = "price"
clean_data_path = "./../artifacts/data/cleaned_data/cleaned_data.csv"
processed_data_path = "./../artifacts/data/processed_data/"


def processed_data(clean_data_path,Target,test_size,processed_data_path):
    print("############## Data Processing Started ###################")
    print(f"Target = {Target} || Testing Size = {test_size}")
    df = pd.read_csv(clean_data_path)

    Y = df[[Target]]
    X = df.drop(columns=[Target])

    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=float(test_size))

    """
    You can write some proprocessing steps here
    """
    mlflow.log_param("test_size",test_size)
    mlflow.log_param("Target",Target)
    X_train.to_csv(os.path.join(processed_data_path,"X_train.csv"),index=False)
    X_test.to_csv(os.path.join(processed_data_path,"X_test.csv"),index=False)
    y_train.to_csv(os.path.join(processed_data_path,"y_train.csv"),index=False)
    y_test.to_csv(os.path.join(processed_data_path,"y_test.csv"),index=False)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean_data_path",default=clean_data_path)
    parser.add_argument("--Target",default=Target)
    parser.add_argument("--test_size",default=test_size)
    parser.add_argument("--processed_data_path",default=processed_data_path)
    args = parser.parse_args()
    processed_data(args.clean_data_path,args.Target,args.test_size,args.processed_data_path) 


