import random
def random_max_index(each_UCBi,k):
    max_UCBi = max(each_UCBi)
    amount_max = 0
    max_index = []
    for i in range(k):
        if each_UCBi[i] ==max_UCBi:
            amount_max +=1
            max_index.append(i)
    if amount_max > 1:
        return max_index[random.randint(0,len(max_index)-1)]
    else:
        return max_index[0]
