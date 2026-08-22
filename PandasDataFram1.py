#DataFarame = 2D Array
import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [27,28,25],
        "City": ["PUNE","KOlhapur","Satara"]
          
        
        }
    print(Data)
    print(type(Data))
    
    print(Data["Name"])
    
    
if __name__ == "__main__":
    main()