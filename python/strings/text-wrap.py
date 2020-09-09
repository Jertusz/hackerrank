import textwrap

def wrap(string, max_width):
    txt = textwrap.fill(string, max_width)
    return txt
