import re
def textmatch(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(textmatch("ac"))
print(textmatch("abc"))
print(textmatch("a"))
print(textmatch("ab"))
print(textmatch("abb"))