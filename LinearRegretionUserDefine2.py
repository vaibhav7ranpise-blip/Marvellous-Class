import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
        
    print("values of Independent Variables X :",X)
    print("values of Independent Variables Y :",Y)
    
    sum_X = 0
    sum_Y = 0
    
    for i in range(len(X)):
        sum_X = sum_X+X[i]
        sum_Y = sum_Y+Y[i]
        
    mean_X = sum_X/len(X)
    mean_Y = sum_Y/len(Y)
    
    print("Mean_X is ",mean_X)
    print("Mean_Y is ",mean_Y)
    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()