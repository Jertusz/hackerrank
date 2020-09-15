import re
for _ in range(int(input())):
    name, email = input().split()
    email = email[1:len(email)-1]
    pattern = re.compile("^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
    if pattern.match(email):
        print(f"{name} <{email}>")
