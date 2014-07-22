# obo.py

def stripTags(pageContents):
    startLoc = pageContents.find("<hr/><h2>")
 
    pageContents = pageContents[startLoc:]

    inside = 0
    text = ''
    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text