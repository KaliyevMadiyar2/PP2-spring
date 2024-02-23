import re

def first(str_):
    pattern = "ab*"
    matches = re.findall(pattern, str_)
    if matches:
        return matches
    else:
        return "No matches found."

str_ = input()
answer = first(str_)
print(','.join(map(str, answer)))
