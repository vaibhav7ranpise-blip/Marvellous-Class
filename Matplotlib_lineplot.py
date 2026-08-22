import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]
    Y = [10,25,18,35,30]
    
    plt.plot(
        X,                          #values of x axix
        Y,                          #values of x axix
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"

    )
    plt.title("Marvellous Line plot")
    plt.xlabel("Student number")
    plt.ylabel("marks")
    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ =="__main__":
    main()