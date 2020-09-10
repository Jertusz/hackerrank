from itertools import permutations

s, k = input().split()
k = int(k)
s = list(s)
for x in list(permutations(s, k)):
    print(''.join(x))
