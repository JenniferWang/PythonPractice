# templates.py

import fileinput, re

field_pat = re.compile(r'\[(.+?)\]')

scope = {}

def replacement(match):
    code = match.group(1)
    try:
        #if the field can be evaluated, return it:
        return str(eval(code,scope))
    except SyntaxError:
        exec(code,scope)
        return ''

# get all the text in a single string
lines = []
for line in fileinput.input():
    #line = re.sub(r'(.*?)\n',r'\1',line)
    lines.append(line)

text = ''.join(lines)

# substitute all the occurences of the field pattern:
print(field_pat.sub(replacement, text))