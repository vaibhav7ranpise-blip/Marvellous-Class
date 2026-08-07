import pandas as pd 
Border = "-"*30
##################################################
## Step 1 : Load the DataSet
##################################################

print(Border)
print("Step 1 : Load the DataSet")
print(Border)

DataPath = "iris.csv"

df=pd.read_csv(DataPath) # Create dataframe in pandas
'''
        pandas
            |
   ----------------- 
   |        |       |    
Series DataFrame Panel
 1D        2D       3D  #Array
'''
print("Dataset Loaded Succesfully")

#Pandas Function - Haed(StartingData ) and Tail(Ending Data)

print("Initial entries from dataset are :")

print(df.head(5))   #load Start 5 data
