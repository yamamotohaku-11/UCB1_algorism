import random 
def create_distribution(A=False):
    slot_distribution = (0.4,0.5,0.7,0.45)
    random_distribution = A
    if random_distribution :
        n = 6
        slot_distribution = set([random.random() for i in range(n)])
    return slot_distribution
