import argparse
import mlflow
import os
import time


os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/DataAIOPS/b2_mlflow_First_project.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "DataAIOPS"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "9775fb6f18d752814f34587ba0e1e3d988a189e4"

mlflow.set_experiment("Training")
time=int(time.time())
def main():
    print("MLflow Pipeline is Triggeed")
    with mlflow.start_run(run_name=f"MLOPS_{time}") as run:
        mlflow.run("./src",entry_point="Data_Cleaning.py",env_manager="local",run_name="Data Cleaning")
        mlflow.run("./src",entry_point="Data_Preprocessing.py",env_manager="local",run_name="Data_Preprocessing")
        mlflow.run("./src",entry_point="Model_Building.py",env_manager="local",run_name="Model Building")
        mlflow.run("./src",entry_point="Model_Evaluation.py",env_manager="local",run_name="Model Evaluation")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main()
