import re


pattern = re.compile(r"(:|,| +)(#[\da-fA-F]{3}|#[\da-fA-F]{6})\b")

    
for _ in range(int(input())):
    line  = input()
    items = pattern.findall(line)

    if items:
        for item in items:    
            print(item[1])
