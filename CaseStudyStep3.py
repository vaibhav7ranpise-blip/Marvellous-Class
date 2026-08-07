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
print(df.describe())   
'''
------------------------------
Step 2 : Data Analysis(EDA)
------------------------------
Shape of DataSet : (150, 5)
Colum name : ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']
MIssing Values per Column :
sepal length (cm)    0
sepal width (cm)     0
petal length (cm)    0
petal width (cm)     0
species              0
dtype: int64
Class DIstribution (Species Count)
species
setosa        50
versicolor    50
virginica     50
Name: count, dtype: int64
Statical report of Dataset :
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.057333           3.758000          1.199333
std             0.828066          0.435866           1.765298          0.762238
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000'''
##################################################
## Step 3 : Decide Independent and Dependent Variable 
##################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variable")
print(Border)

# X : Independent Variable -> Feture
# Y : Dependent Variables  -> Lables

feture_col = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]
#--Data Frame 2D Array
X = df[feture_col]
Y = df["species"] 

#Display Shape

print('X Shape :', X.shape)
print('Y Shape :', Y.shape)

'''
------------------------------
Step 3 : Decide Independent and Dependent Variable
------------------------------
X Shape : (150, 4)
Y Shape : (150,)
'''