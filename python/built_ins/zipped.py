n, x = map(int, input().split())
asub = []
for _ in range(x):
    sub = list(map(float, input().split()))
    asub.append(sub)
for t in zip(*asub):
    print(sum(t)/len(t))
