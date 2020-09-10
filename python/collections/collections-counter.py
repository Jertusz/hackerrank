from collections import Counter

x = int(input())
shoe_size = Counter(map(int, input().split()))
earned = 0

for _ in range(int(input())):
    s, p = input().split()
    s = int(s)
    p = int(p)
    if s in shoe_size:
        shoe_size[s] -= 1
        if shoe_size[s] == 0:
            del shoe_size[s]
        earned += p
print(earned)
