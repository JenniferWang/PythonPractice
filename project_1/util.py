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
            yield ''.join(block).strip()
            # 直接连接，当中没有任何分隔符
            block = []

# Handler:
#     generate the resulting marked-up text
#     receives detailed instructions from the parser
class HTMLRenderer:
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')