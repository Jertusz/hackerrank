from collections import OrderedDict

od = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word in od:
        od[word] += 1
    else:
        od[word] = 1
print(len(od))
print(*(od.values()))
