import random 
def pull_slot(A):
    coin = random.random()
    if coin >= A:
        return 1
    else:
        return 0