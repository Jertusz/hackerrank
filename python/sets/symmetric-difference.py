m = input()
z = set(input().split())
y = input()
x = set(input().split())

diff = sorted([int(b) for b in z^x])
for x in diff:
    print(x)
