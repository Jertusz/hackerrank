import re

def fun(s):
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1, 3}$")
    return pattern.match(s)
