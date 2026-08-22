import numpy as np
import math


def MArvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) **2 + (P1['Y'] - P2['Y']) **2)
    return Ans

def MarvellousKNNClasifire():
    border ="-"*30
    Data = [
        {'point ': 'A', 'X':1 , 'Y': 2, 'lable': 'Red'},
        {'point ': 'B', 'X':2 , 'Y': 3, 'lable': 'Red'},
        {'point ': 'C', 'X':3 , 'Y': 1, 'lable': 'Blue'},
        {'point ': 'D', 'X':5 , 'Y': 6, 'lable': 'Blue'}
        
    ]
    print(border)
    print("Marvellous KNN Clasifire")
    print(border)
    
    for i in Data:
        print(i)
    
    print(border)
    
    new_point = {'X' : 3, 'Y':3}
    for d in Data:
        d['distance']=MArvellousEucDistance(d,new_point)
    
    for d in Data:
        print(d)
        
    sorted_data = sorted(Data, key= lambda item : item['distance'])
    print("Soredted data :")
    for d in sorted_data:
        print(d)
            
    k=3
    nearest = sorted_data[:k]
    print(border)
    print("Nerest 3 number are :")
    print(border)
    
    for i in nearest:
        print(d)
    
    
def main():
    
    MarvellousKNNClasifire()
    
if __name__ == "__main__":
    main()