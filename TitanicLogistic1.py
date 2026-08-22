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
    
#---------------------------------------------------------------------
#       FUnction NAme : main
#       Description : Entry point
#       Input : None
#       OutPut : None
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#------------------------------------------------------------------------- 

def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()