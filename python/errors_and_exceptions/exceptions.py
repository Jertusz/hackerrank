for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        try:
            print(a//b)
        except ZeroDivisionError as e:
            print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
