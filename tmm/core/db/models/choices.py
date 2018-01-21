import logging
logging.basicConfig(filename='trace.log', level='DEBUG')


class Choice(object):
	"""Representation of the user choice during the system"""
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

class FirstChoice(Choice):
	"""Specific representation of the first user choice in the system"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, weight=3, **kwargs)

	def is_in_output(self, outputs):
		try:
			# TODO check if elem in outputs are type str
			list(outputs)
			for o in outputs:
				if self.word in o:
					print(o)
				else:
					logging.info('Discard %s' % o)
		except Exception as e:
			logging.warn('ParamError: --%s-- is not a list' %outputs)
			print(e)

class SecondChoice(Choice):
	"""Specific representation of the second user choice in the system"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, weight=2, **kwargs)

	def get_description(self):
		# TODO: a sofisticated description of the self.word user input
		return 'TODO'

	def get_list_consistent(self):
		# TODO: 
		# find anywhere list of self.word consistent
		# should be a little web scraping that find words consistent
		#
		# Example as 'Pen' with weight from 1 to 3 (lower to higher):
		# [('School', 3), ('Study', 2), ('Rucksack', 2), ('Table', 1)]
		# Numpy | Scrapy --- "I don't now HOW"

		return 'TODO'

class ThirdChoice(Choice):
	"""
	Specific representation of the second user choice in the system
	should be forced to an action verb!
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, weight=1, **kwargs)	
