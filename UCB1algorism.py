from beta_distribution import create_distribution
from pull_arms import pull_slot
from max_UCBi import random_max_index
from UCBi import UCBi
import random
def UCB1algorism(k,n):
    distribution = create_distribution(k)#分布
    each_attempts = [1 for i in range(k)]#それぞれのスロットの試行回数
    each_UCBi = [0 for i in range(k)]
    each_sum = [0 for i in range(k)]#それぞれのスロットのresultの和
    reward = 0 #累積報酬

    for i in range(k):
        result = pull_slot(distribution[i])
        each_sum[i] += result
        reward += result
    
        for j in range(k):
            each_UCBi[j] = UCBi(each_sum[j],k,each_attempts[j])
        
    for i in range(k,n):
        max_UCBi_index = random_max_index(each_UCBi,k)
        result = pull_slot(distribution[max_UCBi_index])
        each_attempts[max_UCBi_index] += 1
        each_sum[max_UCBi_index] += result
        reward += result
        for j in range(k):
            each_UCBi[j] = UCBi(each_sum[j],i,each_attempts[j])

    return reward,each_UCBi

print(UCB1algorism(4,10000))