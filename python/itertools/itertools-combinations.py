from itertools import combinations

ls = input().split()
ls[0] = list(ls[0])
ls[1] = int(ls[1])
for i in range(1, ls[1]+1):
    for x in combinations(sorted(ls[0]), i):
        print(''.join(x))
