import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousKNNClasifire(DataPath):
    Border = "-"*40
    
    print(Border)
    print("Step 1 : Load the dataset from csv file")
    print(Border)
    
    df =  pd.read_csv(DataPath)
    
    print(Border)
    print("some entris from Dataset ")
    print(df.head())
    print(Border)

#Step 2 : clean the Dataset

    print(Border)
    print("Step 2 : clean the Dataset")
    print(Border)

    df.dropna(inplace=True)
    print("Total records :",df.shape[0])
    print("Total Coloumn :",df.shape[1])
    print(Border)

#Step 3 : Seprate Independent and dependend Variable

    print(Border)
    print("Step 3 : Seprate Independent and dependend Variable")
    print(Border)
    
    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    print("Shape of X:", X.shape)
    print("Shape of Y:", Y.shape)
    
    print(Border)
    print("Input coloumn :", X.columns.tolist())
    print("Output Column:  Class")

def main():
    
    MarvellousKNNClasifire("WinePredictor.csv")
    
    
if __name__ == "__main__":
    main()