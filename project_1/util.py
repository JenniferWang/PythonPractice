# A text block generator

def lines(file):
    """
    tack a new line to the end of the file
    """
    for line in file:
        yield line
    yield '/n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip() and not line.strip()[0] == '-':
            block.append(line)
        elif not line.strip() and block:
            yield ''.join(block).strip()
            block = []        
        elif line.strip() and line.strip()[0] =='-':
            yield line.strip()


