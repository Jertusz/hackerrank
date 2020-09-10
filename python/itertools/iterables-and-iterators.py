from itertools import combinations

n = int(input())
l = input().split()
k = int(input())
c = list(combinations(l, k))
f = filter(lambda d: 'a' in d, c)
print("{0:.3}".format(len(list(f))/len(c)))
