import re
m = input()
k = input()
pattern = re.compile(k)
r = pattern.search(m)
if not r:
    print("(-1, -1)")
while r:
    print(f'({r.start()}, {r.end()-1})')
    r = pattern.search(m, r.start()+1)
