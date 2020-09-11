lc = []
uc = []
even = []
uneven = []
s = input()
for l in s:
    if l.isnumeric() and int(l)%2 == 0:
        even.append(l)
    elif l.isnumeric():
        uneven.append(l)
    elif l.isupper():
        uc.append(l)
    else:
        lc.append(l)
lc.sort()
uc.sort()
even.sort()
uneven.sort()
print(''.join(lc+uc+uneven+even))
