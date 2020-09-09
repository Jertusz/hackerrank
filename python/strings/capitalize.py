def solve(s):
    s = s.split()
    string = ""
    for w in s:
        string += w.capitalize()
        string += ' '
    return string
