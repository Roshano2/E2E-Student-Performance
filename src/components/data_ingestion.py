#components has all the modules
#which inludes data ingestion - #all the code related to reading the data

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass #create class variable in short

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass #automatically adds __init__ methods like thing
class DataIngestionConfig:  
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion: #class for main dataingestion with splitting of dataset
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #calls the above class to ensure the path of the dataset

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') #you can change this section to read it from monogodb or mysql
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #making directory 
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False, header = True)  #making raw data path
            logging.info('Train test split initiated')
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42) #spliting of dataset in df

            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)  #making raw data path
           
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)  #making raw data path

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion() #object creation
    train_data,test_data = obj.initiate_data_ingestion() #calling the function

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
