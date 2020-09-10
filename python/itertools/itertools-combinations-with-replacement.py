from itertools import combinations_with_replacement
s, k = input().split()
s = sorted(list(s))
k = int(k)

for x in combinations_with_replacement(s, k):
    print(''.join(x))
