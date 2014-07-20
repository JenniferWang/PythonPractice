# The Main Program
# $python markup.py<test_input.txt> test_output.html
import sys, re
from handlers import *
from util import *
from rule import *

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
        for block in blocks(file):
            for filter in self.filters:
                ## pay attention to self.handler here
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    if rule.action(block,self.handler): break

        self.handler.end('document')

class BasicTextParser(Parser):
	'''
	A specific Parser that adds rules and filters in its constructor.
	'''
	def __init__(self,handler): # The order is important
		Parser.__init__(self,handler)
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadlineRule())
		self.addRule(ParagraphRule()) # Default is placed in the last

		# Filters - They are simply regular expressions
		self.addFilter(r'\*(.+?)\*','emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')


if __name__ == '__main__':
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)

    parser.parse(sys.stdin)
    #print(re.sub(r'\*(.+?)\*',handler.sub('emphasis'),r'This *is* a test'))



 

