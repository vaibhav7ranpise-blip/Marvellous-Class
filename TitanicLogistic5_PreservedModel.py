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
  
  
  # step 3 : Split Dta 
#---------------------------------------------------------------------
#       FUnction NAme : Split data
#       Description : It perform Spliting Data
#       Input : Data Fram
#       OutPut : 4 Sub sets for training and testing 
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#-------------------------------------------------------------------------
def SplitData(df):
    X= df.drop("Survived",axis =1)
    Y = df["Survived"]
    
    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        
    )   
    
    print("Data Set Spliting Successfully")
    return X_train,X_test,Y_train,Y_test

#---------------------------------------------------------------------
#       FUnction NAme : Train model
#       Description : it perfoms train model
#       Input : Training Feature and label
#       OutPut : Trained Model
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#------------------------------------------------------------------------- 
def TrainModel(X_train,Y_train):
    model = logisticRegration()



#---------------------------------------------------------------------
#       FUnction NAme : Evaluate MOdel
#       Description : it perfoms model testing
#       Input : model,testing DATA(Feature and label)
#       OutPut : NOne
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#------------------------------------------------------------------------- 
def EvaluateMOdel(model , X_test, Y_test):
    Y_pred = model.predict(X_test)
    
    Accuracy = accuracy_score(Y_test,Y_pred)
    
    print("Accuracy is :", Accuracy)
    
    print(confusion_matrix(Y_test,Y_pred))
# step 6
#---------------------------------------------------------------------
#       FUnction NAme : Preserved MOdel
#       Description : it perfoms model Preservrtion into .plk file testing
#       Input : model,testing DATA(Feature and label)
#       OutPut : NOne
#       AUthor : VAIBHAV VITTHAL RANPISE
#       Date : 16/08/2026
#------------------------------------------------------------------------- 
def PreservedMOdel(model,filename):
    joblib.dump(model,filename)

    print("MOdel PResereved with name :",filename)

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
    
    # 3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    # 4 
    model = TrainModel(X_test,Y_test)
     # 5
     
    EvaluateMOdel(model , X_test.Y_test)
    
    # 6 
    PreservedMOdel(model,"MarvellousTitanic.pkl")
     

if __name__ == "__main__":
    main()