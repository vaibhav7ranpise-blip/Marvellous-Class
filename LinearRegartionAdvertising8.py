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
    
    #STep 7 : Split the Dataset
    print(border)
    print("STep 7 : Split the Dataset")
    print(border)
    
    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        
    )
    
    print("Training data :",X_train.shape)
    print("Testing data :",X_test.shape)
    
    
    # Step 8 : Crwate and train the model
    print(border)
    print("Step 8 : Create and train the model")
    print(border)
    
    model = LinearRegression()
    
    model = model.fit(X_train,Y_train)
    print("Model Train SUccesfully")
    
    # STep 9 : TEst the model
    print(border)
    print("STep 9 : TEst the model")
    print(border)
    
    Y_pred = model.predict(X_test)
    print("Expected Ans :")
    print(Y_test[:3])       # pahile 5 record
    
    
    print("Predicted Ans :")
    print(Y_pred[:3])  
    
    
    #Step  10 : EValuated the Model
    print(border)
    print("Step  10 : EValuated the Model")
    print(border)
    
    MSE = mean_squared_error(Y_test,Y_pred)
    
    RMSE = np.sqrt(MSE)
    
    R2 = r2_score(Y_test,Y_pred)
    print("MSE :",MSE)
    print("RMSE :",RMSE)
    print("R2 :",R2)
    
    
    #Step 11 : Display Coefficient 
    print(border)
    print("Step 11 : Display Coefficient")
    print(border)
    
    print("TV Coefficient :",model.coef_[0])
    print("radio Coefficient :",model.coef_[1])
    print("Newspaper Coefficient :",model.coef_[2])
    print("INtercept :", model.intercept_)
    
def main():
    marvellousRegration("Advertising.csv")
    

if __name__ == "__main__":
    main()