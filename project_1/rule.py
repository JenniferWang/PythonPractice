class Rule:
	def action(self,block,handler):
		'''
    	Base class for all rules

    	call methods such as handler.start('headline'),handler.feed(block) and handler.end('headline')
		because we don't want to attempt to use any other rules, return True, which will end the rule processing for this block.
		'''
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True

class HeadlineRule(Rule):
	'''
	A heading is a single line that is at most 70 characters and that doesn't end with a colon.
	'''
	type = 'heading' # used by 'action' inherited from 'Rule'
	def condition(self,block):
		# if the block fits the definition of a headline, return true;
		# otherwise, return false
		return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadlineRule): # Note that it is inherited from HeadingRule
	'''
	The title is the first block in the document, provided that it is a heading
	'''
	type = 'title'
	first = True

	def condition(self,block):
		if not self.first: return False
		self.first = False
		return HeadlineRule.condition(self,block)

class ListItemRule(Rule):
	'''
	A list item is a paragraph that begins with a hyphen. As part of the formatting, the hyphen is removed.
	'''
	type = 'listitem'
	def condition(self,block):
		return block[0] == '-'
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True

class ListRule(ListItemRule):
	'''
	A list begins between a block that is not a list item and a subsequent list item. It ends after the last consecutive list item.
	'''
	type = 'list'
	inside = False # indicate whether the parser is currently inside the list
	def condition(self,block):
		'''
		The condition is always true because you want to examine alll blocks
		'''
		return True
	def action(self,block,handler):
		if not self.inside and ListItemRule.condition(self,block): # means you have just entered a list
			handler.start(self.type)
			self.inside = True
		elif self.inside and not ListItemRule.condition(self,block):
			handler.end(self.type)
			self.inside = False
		return False

class ParagraphRule(Rule):
	'''
	A paragraph is simply a block that isn't covered by any of the other rules.
	'''
	type = 'paragraph'
	def condition(self,block):
		'''
		always true as this is the default rule
		'''
		return True

