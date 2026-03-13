import math
def UCBi(sum,t,n_i):
    UCBi = sum/n_i + math.sqrt(math.log(t)/(2*(n_i)))
    return UCBi