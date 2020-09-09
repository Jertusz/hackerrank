def minion_game(string):
    s = string

    vowels = 'AEIOU'
    length = len(s)

    K = sum([length-i for i in range(length) if s[i] in vowels])
    S = sum([length-i for i in range(length) if s[i] not in vowels])

    if K > S:
        print("Kevin", K)
    elif K < S:
        print("Stuart", S)
    else:
        print("Draw")
