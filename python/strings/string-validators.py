s = input()
alnum = "False"
alphabet = "False"
digit = "False"
lower = "False"
upper = "False"
for l in s:
    if l.isalnum():
        alnum = "True"
    if l.isalpha():
        alphabet = "True"
    if l.isdigit():
        digit = "True"
    if l.islower():
        lower = "True"
    if l.isupper():
        upper = "True"
print(alnum, alphabet, digit, lower, upper, sep='\n')
