from collections import OrderedDict

od = OrderedDict()
for _ in range(int(input())):
    tmp = input().rsplit(' ', 1)
    if tmp[0] in od:
        od[tmp[0]] += int(tmp[1])
    else:
        od[tmp[0]] = int(tmp[1])
for x in od:
    print(x, od[x])
