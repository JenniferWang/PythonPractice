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
        if line.strip():
            block.append(line)
        elif block:
            yield ' '.join(block).strip()
            block = []