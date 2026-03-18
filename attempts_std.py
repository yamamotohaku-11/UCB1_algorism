from UCB1_algorism.distribution import distribution as make
import scipy.stats as stats
import UCB1_algorism.return_result as f
def attempt_std():
    UCB = [[]for i in range(10)]
    roundrobin = [[]for i in range(10)]
    random = [[]for i in range(10)]
    methods = [UCB,roundrobin,random]
    functions = [f.result_UCB1,f.result_roundrobin,f.result_random]
    for i in range(10):
        k = 4
        distribution = make.distribution(k,True)
        slot = [stats.bernoulli(i for i in distribution)]
        for j in range(3):
            each_attempts = [1 for i in range(k)]
            each_results = [0 for i in range(k)]
            for l in range(k):
                result = slot[l].rvs(1)[0]
                each_results += result
            
            for l in range(k,1000):
                methods[j][i].append(functions[j](each_attempts,each_results,slot,l))
    f


        

if __name__ == "__main__":
    attempt_std()