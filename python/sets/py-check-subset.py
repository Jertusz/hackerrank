def subset(a, b):
    for item in a:
        if item not in b:
            return False
    return True


x = int(input())
for i in range(x):
    _, a = input(), input().split()
    _, b = input(), input().split()
    print(subset(a,b))
