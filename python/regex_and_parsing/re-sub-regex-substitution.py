import re
pattern1 = re.compile(r'\ \&\&\ ')
pattern2 = re.compile(r'\ \|\|\ ')
for _ in range(int(input())):
    x = input()
    while re.search(pattern1, x) or re.search(pattern2, x):
        x = re.sub(pattern1, " and ", x)
        x = re.sub(pattern2, " or ", x)
    print(x)
