# Handler:
#     generate the resulting marked-up text
#     receives detailed instructions from the parser
# TODO : adfadf

class Handler:
    '''
    An object that handles method calls from  the Parser.

    The Parser will call the start() and end() methods at the 
    beginning of each block, with the proper block name as a
    parameter. The sub() method will be used in regular expression
    substitution. When called with a name such as 'emphasis', it will
    return a proper substitution function.
    '''
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
    '''
    A specific handler used for rendering HTML

    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    '''
    def start_document(self):
        # TODO: check this '...'
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self,match):
        return '<a href ="%s">%s</a>' % (match.group(1),match.group(1))
    def sub_mail(self,match):
        return '<a hrf ="mailto:%s">%s</a>' % (match.group(1),match.group(1))
    def feed(self,data):
        print(data)



