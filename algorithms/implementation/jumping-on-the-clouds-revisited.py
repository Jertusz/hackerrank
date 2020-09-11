def jumpingOnClouds(c, k):
    energy = 100 
    i = k % n 
    energy -= c[i] * 2 + 1 
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy
