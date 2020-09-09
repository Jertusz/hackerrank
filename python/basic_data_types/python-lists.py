n = int(input())
lst = []
for _ in range(n):
    data = input().split()
    command = data[0]
    data = [int(x) for x in data[1:]]
    if command == "insert":
        lst.insert(data[0], data[1])
    elif command == "print":
        print(lst)
    elif command == "remove":
        lst.remove(data[0])
    elif command == "append":
        lst.append(data[0])
    elif command == "sort":
        lst.sort()
    elif command == "pop":
        lst.pop()
    elif command == "reverse":
        lst.reverse()
