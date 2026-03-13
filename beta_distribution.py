import random 
def create_distribution(k = 4,A = False):
    slot_distribution = (0.4,0.5,0.7,0.45)
    random_distribution = A
    if random_distribution :
        k = 6
        slot_distribution = set([random.random() for i in range(k)])
    return slot_distribution
