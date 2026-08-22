import pandas as pd

import joblib 

def LoadMOdel(FIlename):
    model = joblib.load(FIlename)
    
    
    print("Model loaded Successfully")
    
    print(model.feature_names_in_)
    
    return model
def predictPassenger(model):
    print("Enter infor ")
    
    Pclass = int(input("ENter Pclass (1/2/3)"))
    Sex = int(input("ENter Sex : (0 : F / 1 : M)"))
    Age = float(input("ENter Age :"))
    sibsp = int(input("Enter Sibsb :"))
    Parch =int(input("ENter Parch :"))
    Fare = float(input("ENter Fare :"))
    Embarked = float(input("Enter Embarked : (0/1/2)"))
    
    passenger = pd.DataFrame([{
       "Pclas" : Pclass,
        "Sex" : sex,
        "Age " : Age,
        "sibsp" : sibsp,
        "Parch" : Parch,
        "Fare" : Fare,
        "Embarked_1.0" =  1 if Embarked == 1 else 0:
        
    }])
    
    
    
def main():
    model = LoadMOdel("MarvellousTitanic.pkl")