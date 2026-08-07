from sklearn.datasets import load_iris


def main():
    print("-"*30)
    print("Iris classification Case study")
    print("-"*30)
    
    Dataset = load_iris()
    
    for i in range(len(Dataset.target)):
        print("ID %d, Features %s, Lable %s" %(i,Dataset.data[i],Dataset.target[i]))  #Data Lodading
      
if __name__ == "__main__":
    main() 