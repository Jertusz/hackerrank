a = set(input().split())
print(all(a.issuperset(set(input().split())) for _ in range(int(input()))))
