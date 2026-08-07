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

##################################################
## Step 2 : Data Analysis(EDA)
##################################################

print(Border)
print("Step 2 : Data Analysis(EDA)")
print(Border)

print("Shape of DataSet :", df.shape) #

print("Colum name :",list(df.columns))  #column name 

print("MIssing Values per Column :")
print(df.isnull().sum())                #null value cell cont and sum

print("Class DIstribution (Species Count)")
print(df["species"].value_counts())

print("Statical report of Dataset :")
print(df.describe())                        #
