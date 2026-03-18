from UCB1_algorism.UCB1algorism import UCB1algorism
from UCB1_algorism.roundrobin  import roundrobin
from UCB1_algorism.random import random_pull
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def standard_deviation():
    N = 10
    n = 1000
    k = 4
    distribution = (0.3,0.5,0.45,0.7)
    UCB1_rewards = [0 for i in range(N)]
    roundrobin_rewards = [0 for i in range(N)]
    random_rewards = [0 for i in range(N)]
    for i in range(N):
        UCB1_rewards[i],_ = UCB1algorism(k,n,distribution)
        roundrobin_rewards[i],_ = roundrobin(k,n,distribution)
        random_rewards[i],_ = random_pull(k,n,distribution)
    
    UCB1_average = np.average(UCB1_rewards)
    roundrobin_average = np.average(roundrobin_rewards)
    randam_average = np.average(random_rewards)

    UCB1_std = np.std(UCB1_rewards)
    roundrobin_std = np.std(roundrobin_rewards)
    random_std = np.std(random_rewards)

    ax = plt.gca()
    ax.set_box_aspect(1)

    x = [1,2,3]
    plt.errorbar(
        x,
        [UCB1_average,roundrobin_average,randam_average],
        yerr = [UCB1_std,roundrobin_std,random_std],
        fmt = "o",
        capsize = 3,
        color = "black" 

    )
    plt.xticks(x,["UCB1","RoundRobin","random"])
    plt.xlabel("Methods")
    plt.ylabel("Value")
    plt.xlim(0, 4)
    plt.ylim(400, 800)
    
    plt.savefig("graphs/standard_deviation.png",dpi = 600,bbox_inches = "tight")

if __name__ == "__main__":
    standard_deviation()