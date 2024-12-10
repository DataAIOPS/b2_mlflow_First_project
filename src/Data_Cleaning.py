import pandas as pd
import argparse

raw_data_path = "./artifacts/data/raw_data/homeprices.csv"
clean_data_path = "./artifacts/data/cleaned_data/cleaned_data.csv"

def data_cleaning(raw_data_path,clean_data_path):
    df = pd.read_csv(raw_data_path)
    """"
    Data cleaning step will be added
    
    """
    df.to_csv(clean_data_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_data_path",default=raw_data_path)
    parser.add_argument("--clean_data_path",default=clean_data_path)
    args = parser.parse_args()
    data_cleaning(args.raw_data_path,args.clean_data_path)