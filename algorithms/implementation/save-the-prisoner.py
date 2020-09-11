def saveThePrisoner(n, m, s):
    t = s+m-1
    t = t%n
    if t == 0:
        t = n
    return t
