a = input()
a_items = set(input().split())
n = int(input())
for i in range(n):
    x = input().split()
    y = set(input().split())
    if x[0] == 'intersection_update':
        a_items.intersection_update(y)
    elif x[0] == 'update':
        a_items.update(y)
    elif x[0] == 'difference_update':
        a_items.difference_update(y)
    elif x[0] == 'symmetric_difference_update':
        a_items.symmetric_difference_update(y)
a_items = [int(x) for x in a_items]
print(sum(a_items))
