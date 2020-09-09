n, m = map(int, input().split())

# Long version (textwise)
pattern = []
for i in range(n//2):
    line = '.|.' * (2*i + 1)
    line = line.center(m, '-')
    pattern.append(line)

res = pattern + ['WELCOME'.center(m, '-') + pattern[::-1]
res = '\n'.join(res)


# Condensed version
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
res = '/n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])

print(res)
