from UCB1_algorism.UCB1algorism import UCB1algorism
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from UCB1_algorism.beta_distribution import distribution
def main():
    D = distribution(4,True)
    print(D)
    y = [0 for i in range(50)]
    Amax = 0
    summax = 0
    for i in tqdm(range(1,51)):
        n = i * 0.1
        sum = 0
        for j in range(500):
            sum += UCB1algorism(4,10000,n,D)
        y[i-1] = sum / 500
        if summax < sum:
            summax = sum
            Amax = n
    x = [i for i in range(1,51)]
    variance = np.var(D)
    roundedD = [round(i,3) for i in D]
    plt.plot(x,y)
    plt.figtext(0.5, 0.01, f"distribution:{roundedD}", ha="center")
    plt.savefig("graph.png")
    plt.show()
    print(Amax)

    

if __name__ == "__main__":
    main()
