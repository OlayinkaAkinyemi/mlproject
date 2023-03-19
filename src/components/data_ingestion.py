import pandas as pd
import numpy as np
import os

class DataIngestion_config:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifact", "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestion_config()
    def initiate_data_ingestion(self):
        df = pd.read_csv("/Users/oakinyemi/Downloads/StudentsPerformance.csv")
        return df.head()
print(DataIngestion().initiate_data_ingestion())