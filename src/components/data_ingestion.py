import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

class DataIngestion_config:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestion_config()
    def initiate_data_ingestion(self):
        df = pd.read_csv("/Users/oakinyemi/Downloads/StudentsPerformance.csv")
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
        df.to_csv(self.ingestion_config.raw_data_path, index=False, header = True)
        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
        train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
        test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
        return (self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()