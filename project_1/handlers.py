# Handler:
#     generate the resulting marked-up text
#     receives detailed instructions from the parser
# TODO : adfadf

class Handler:
    def callback(self,prefix,name,*args):
        '''
        Find the correct method
        '''
        method = getattr(self,prefix+name,None)
        try:
            return method(*args)
        except AttributeError:
            print('error')
            return None

    def start(self,name):
        '''
        Helper methods
        '''
        self.callback('start_',name)

    def end(self,name):
        '''
        Helper methods
        '''
        self.callback('end_',name)

# Returns a new function to serve as the replacement function in re.sub
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_',name,match)
            if result is None:
                return match.group(0)
            return result
        return substitution



class HTMLRenderer(Handler):
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')

    def sub_emphasis(self,match):
        return "<em>%s</em>" % match.group(1)


class Parser:
    '''
    A Parser reads a text file, applying rules and controlling a handler.
    '''
    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self,rule):
        self.rules.append(rule)

    def addFilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
            ## Need to Check
        self.filters.append(filter)

    def parse(self,file):
        self.handler.start('document')
        for block in block(file):
            for filter in self.filters:
                ## pay attention to self.handler here
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last: break

        self.handler.end('document')


if __name__ == '__main__':
    from handlers import HTMLRenderer
    import re
    # TODO: Not the expected result
    handler = HTMLRenderer()
    print(re.sub(r'\*(.+?)\*',handler.sub('emphasis'),r'This *is* a test'))

