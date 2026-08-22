import matplotlib.pyplot as plt

def main():
    language  = ["C","C++","JAVA","PYTHON"]
    Student=[30,40,35,55]
    
    plt.bar(
        language,
        Student,
        width=0.6,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.8 ,
        label = "Student"      #lagent text
    )
    
    plt.title("Marcvellous Bar plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of studnts")
    plt.legend()
    plt.show()
    
    
if __name__ =="__main__":
    main()