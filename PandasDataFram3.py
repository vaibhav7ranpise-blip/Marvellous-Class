#DataFarame = 2D Array
import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [27,28,25],
        "City": ["PUNE","KOlhapur","Satara"]
          
        
        }
    dobj = pd.DataFrame(Data)
    
    # print(dobj[0]) not allowed
    
    print(dobj[["Name","Age"]])
    
if __name__ == "__main__":
    main()