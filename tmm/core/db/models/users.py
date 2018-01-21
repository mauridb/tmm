class User(object):
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	def set_first_name(self, first_name):
		self.first_name = first_name

	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_fullname(self):
		if self.first_name and self.last_name:
			return '{} {}'.format(self.first_name, self.last_name)
