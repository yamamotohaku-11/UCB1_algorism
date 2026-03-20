from UCB1_algorism.distribution import distribution 
import scipy.stats as stats
import UCB1_algorism.return_result as f
import numpy as np
import matplotlib.pyplot as plt
def attempt_std():
    N = 50 
    UCB = [[]for i in range(N)]
    roundrobin = [[]for i in range(N)]
    random = [[]for i in range(N)]
    methods = [UCB,roundrobin,random]
    functions = [f.result_UCB,f.result_roundrobin,f.result_random]
    for i in range(N):
        k = 4
        distribution_slot = distribution(k,True)
        slot = [stats.bernoulli(i) for i in distribution_slot]
        for j in range(3):
            cumulative_results = 0
            each_attempts = [1 for i in range(k)]
            each_results = [0 for i in range(k)]
            for l in range(k):
                result = slot[l].rvs(1)[0]
                each_results[l] += result
                cumulative_results += result
                methods[j][i].append(cumulative_results)
            
            for l in range(k,1000):
                cumulative_results += functions[j](each_attempts,each_results,slot,l)
                methods[j][i].append(cumulative_results)
    average_UCB = []
    average_roundrobin = []
    average_random = []
    std_UCB = []    
    std_roundrobin = []
    std_random = []
    for j in range(1000):
        average_UCB.append(np.average([UCB[i][j] for i in range(N)]))
        average_roundrobin.append(np.average([roundrobin[i][j] for i in range(N)]))
        average_random.append(np.average([random[i][j] for i in range(N)]))
        std_UCB.append(np.std([UCB[i][j] for i in range(N)]))
        std_roundrobin.append(np.std([roundrobin[i][j] for i in range(N)]))
        std_random.append(np.std([random[i][j] for i in range(N)]))

    x = [i for i in range(1,1001)]
    average_UCB = np.array(average_UCB)
    std_UCB = np.array(std_UCB)
    average_roundrobin = np.array(average_roundrobin)
    std_roundrobin = np.array(std_roundrobin)
    average_random = np.array(average_random)
    std_random = np.array(std_random)
    
    plt.plot(x,average_UCB,label="UCB1",color="blue")
    plt.plot(x,average_roundrobin,label="roundrobin",color="green") 
    plt.plot(x,average_random,label="random",color="red")

    plt.fill_between(
        x,
        average_UCB - std_UCB,
        average_UCB + std_UCB,
        alpha=0.15,  
        color="blue"
        )
    plt.fill_between(
        x,
        average_roundrobin - std_roundrobin,
        average_roundrobin + std_roundrobin,
        alpha=0.15,  
        color="green"
        )
    plt.fill_between(
        x,
        average_random - std_random,
        average_random + std_random,
        alpha=0.15,  
        color="red"
        )
    print("UCB1の平均値:",average_UCB)
    plt.xlabel("x")
    plt.ylabel("value")
    plt.legend()
    plt.xlim(0,1000)
    plt.axis('equal')
    plt.savefig("graphs/attempt_std.png", dpi=600)
    plt.show()

if __name__ == "__main__":
    attempt_std()