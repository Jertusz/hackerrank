marks = []
for _ in range(int(input())):
    marks.append([input(), float(input())])

second_highest = sorted(list(set([m for n, m in marks])))[1]

print('\n'.join([a for a,b in sorted(marks) if b == second_highest]))
