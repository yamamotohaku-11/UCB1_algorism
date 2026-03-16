from UCB1_algorism.UCB1algorism import UCB1algorism
import numpy 
import matplotlib.pyplot as plt
from tqdm import tqdm
def main():
    y = [0 for i in range(50)]
    Amax = 0
    summax = 0
    for i in tqdm(range(1,51)):
        n = i * 0.1
        sum = 0
        for j in range(500):
            sum += UCB1algorism(4,10000,n)
        y[i-1] = sum / 500
        if summax < sum:
            summax = sum
            Amax = i    
    x = [i for i in range(1,51)]
    
    plt.plot(x,y)
    plt.savefig("graph.png")
    plt.show()
    print(Amax)

    

if __name__ == "__main__":
    main()
