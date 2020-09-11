def beautifulDays(i, j, k):
    res = 0
    for x in range(i, j+1):
        t = x
        rev = 0
        ld = x%10
        rev = (rev * 10) + ld
        while x > 0:
            x = x // 10
            ld = x%10
            rev = rev * 10 + ld
        if rev % 10 == 0:
            rev = rev // 10
        if (t - rev) % k == 0:
            res += 1 
    return res
