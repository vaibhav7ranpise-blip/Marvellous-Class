import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def marvellousRegration(DataPath):
    border="_"*60
    # Step 1 : Load the data
    print(border)
    print("Step 1 : Load the data")
    print(border)
    
    df = pd.read_csv(DataPath)
    print(df.head())
    
    # Step 2 : Removed Unwanted columns
    print(border)
    print("Step 2 : Removed Unwanted columns")
    print(border)
    
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    print(df.head())

    # step 3 : miossing value 
    print(border)
    print("step 3 : Check miossing value ")
    print(border)
    
    print("Toatal Miising values")
    print(border)
    print(df.isnull().sum())
    print(border)
    
    #step 4 : Statistical Summery
    print(border)
    print("step 4 : Statistical Summery")
    print(border)
    
    print(df.describe())
    
    #Step 5 : Correlation
    print(border)
    print("Step 5 : Correlation")
    print(border)
    
    print(df.corr())
    
    
    # step 6: Saperate independent and Dependent variable
    print(border)
    print("step 6: Saperate independent and Dependent variable")
    print(border)
    
    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]
    print("Independent Variable ")
    print(X.head())
    
    print("dependent Variable ")
    print(Y.head())
def main():
    marvellousRegration("Advertising.csv")
    
    

if __name__ == "__main__":
    main()