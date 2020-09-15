def appendAndDelete(s, t, k):
    cl = 0
    for i in range(min([len(s), len(t)])):
        if s[i] == t[i]:
            cl += 1
        else:
            break
    if len(s) + len(t) - (2*cl) > k:
        return 'No'
    elif (len(s) + len(t) - (2*cl))%2 == k%2:
        return 'Yes'
    elif len(s) + len(t) - k < 0:
        return 'Yes'
    else:
        return 'No'
