from itertools import product

a = map(int, input().split())
b = map(int, input().split())
res = list(product(a,b))
for x in res:
    print(x, end=' ')
