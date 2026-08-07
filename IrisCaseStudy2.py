from sklearn.datasets import load_iris


def main():
    print("-"*30)
    print("Iris classification Case study")
    print("-"*30)
    
    Dataset = load_iris()
    
    #MetaData of the dataset
    
    print("Independent variable are :")
    print(Dataset.feature_names)


    print("Dependent Variable is :")
    print(Dataset.target_names)    
if __name__ == "__main__":
    main() 