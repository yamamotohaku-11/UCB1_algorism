from UCB1_algorism.UCB1algorism import UCB1algorism
from UCB1_algorism.roundrobin  import roundrobin
from UCB1_algorism.random import random_pull
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
def main():
    distribution = (0.4,0.5,0.7,0.45)
    n = 1000
    k = 4
    x = range(n)
    reward_UCB1,y_UCB1 = UCB1algorism(k,n,distribution)
    reward_roundrobin,y_roundrobin = roundrobin(k,n,distribution)
    reward_random,y_random = random_pull(k,n,distribution)

    fig, ax = plt.subplots()

    ax.plot(x, y_UCB1, label="UCB1", color="black")
    ax.plot(x, y_roundrobin, label="RoundRobin", color="red")
    ax.plot(x, y_random, label="random", color="blue")

    ax.set_xlabel("attempt")
    ax.set_ylabel("reward")
    ax.legend()

    ax.text(
        0.5, -0.18,
        f"sums of rewards- UCB1:{reward_UCB1}, RoundRobin:{reward_roundrobin}, random:{reward_random}",
        transform=ax.transAxes,
        ha="center"
    )

    plt.subplots_adjust(bottom=0.25)
    plt.savefig("graph.png", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
