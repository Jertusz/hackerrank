k = int(input())
arr = list(map(int, input().split()))

s = set(arr)

res = sum(s)*k - sum(arr)
res = res // (k-1)
print(res)
