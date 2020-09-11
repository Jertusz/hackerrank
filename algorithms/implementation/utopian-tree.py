def utopianTree(n):
    x = 1
    for i in range(n):
        if i%2 == 0:
            x *= 2
        else:
            x += 1
    return x
