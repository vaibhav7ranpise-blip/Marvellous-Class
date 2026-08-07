import pandas as pd 
import matplotlib.pyplot as plt   # use in step 4
import seaborn as sns
from sklearn.model_selection import train_test_split

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

##################################################
## Step 4 : Visualisation OF DataSet
##################################################
#import matplotlib as plt
print(Border)
print("Step 4 : Visualisation OF DataSet")
print(Border)

#scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"],label = sp)
    
    plt.title("Marvellous Iris Case Study") 
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")
    
plt.legend()
plt.grid()
plt.show()

##################################################
## Step 5 : Split the Dataset for Training and testing
##################################################
#from sklearn.model_selection import train_test_split
print(Border)
print(" Step 5 : Split the Dataset for Training and testing")
print(Border)

X_tarin,X_test,Y_tarin,Y_test = train_test_split(X,Y, test_size=0.5,random_state=42)  #Suffeling in random state

print("Dataset Slipting Actiity DOne")

print("X :",X.shape)        #(150)
print("Y :",Y.shape)
print("X_train :", X_tarin.shape)       #(75,4)
print("X_test :", X_test.shape)          #(75,4)

print("Y_train :", Y_tarin.shape)           #(75,)
print("Y_test :", Y_test.shape)              #(75,)
