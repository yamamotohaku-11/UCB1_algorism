from beta_distribution import create_distribution
from pull_arms import pull_slot
from max_UCBi import random_max_index
def main():
    k = 4 #スロットの数
    distribution = create_distribution(k)
    each_attempts = [1 for i in range(k)]
    each_UCBi = [0 for i in range(k)]
    each_sum = [0 for i in range(k)]

    for i in range(k):
        result = pull_slot[distribution[i]]
        each_UCBi[i] = result
        each_sum = result


    for i in range(1000-k):
        max_UCBi = random_max_index(each_UCBi,k)
        

if __name__ == "__main__":
    main()
