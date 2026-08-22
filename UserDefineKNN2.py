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

def main():
    
    MarvellousKNNClasifire()
    
if __name__ == "__main__":
    main()