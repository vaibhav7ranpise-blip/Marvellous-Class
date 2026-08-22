import pandas as pd
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#step 1 : Load Data

#---------------------------------------------------------------------
#       FUnction NAme : Load DATA
#       Description : Load the datav fromm CSV
#       Input : Name of CSV file
#       OutPut : Data frame
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#-------------------------------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)
    
    print("Data loaded Succesfully")
    print(df.head())
    return df

# step 2 : Data Preprocessing
#---------------------------------------------------------------------
#       FUnction NAme : Preprod=cessDAta
#       Description : It perform data Analisys
#       Input : Data Fram
#       OutPut : Updated Data Frame
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#-------------------------------------------------------------------------
def preprocess(df):
      df = df.drop([
          "Passengerid",
          "zero",
          "Name"          
      ],
      errors = "ignore")
      
      # HAndel Missing VAlues
      df ["Age"] = df["Age"].fillna(df["Age"].median())
      df ["Fare"] = df["Fare"].fillna(df["Fare"].median())
      df ["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
      # Conver Catagorical to numeric
      df = pd.get_dummies(
          df,
          columns=["Embarked"],
          drop_first=True,
          dtype = int
      )
      
      print(df.head())
      
      
      print("Data preprocessing completed ")
      return df 
         
#---------------------------------------------------------------------
#       FUnction NAme : main
#       Description : Entry point
#       Input : None
#       OutPut : None
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#------------------------------------------------------------------------- 

def main():
    #step 1 : Load Data
    df = LoadData("MarvellousTitanicDataset.csv")
    
    #step 2
    df  = preprocess(df)
    

if __name__ == "__main__":
    main()