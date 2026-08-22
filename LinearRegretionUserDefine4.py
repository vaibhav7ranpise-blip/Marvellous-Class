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
    
    n = len(X)   #5
    numerator = 0
    denomerator = 0
    
    # m = sum(x-xbar) * sum (y - ybar) / sum(X-xbar) **2
    #calculate slop (i.e. m)
    for i in range(n):
        numerator= numerator+((X[i]-mean_X)*(Y[i]-mean_Y))
        denomerator = denomerator + ((X[i]-mean_X)**2)
        
    m = numerator /denomerator
    
    print("Slop of line ", m)
        
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()