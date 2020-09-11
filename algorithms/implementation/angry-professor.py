def angryProfessor(k, a):
    s = 0
    for stud in a:
        if stud <= 0:
            s += 1
    if s < k:
        return "YES"
    else:
        return "NO"
