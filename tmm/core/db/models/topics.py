from tmm.core.db.models.users import User

import logging
logging.basicConfig(filename='trace.log', level='DEBUG')


class Topic(object):
	def __init__(self, *arg, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
		self.description = ''

	def set_description(self, description):
		self.description = description

	def set_user(self, user):
		self.user = user

	def get_user(self):
		if self.user:
			return self.user
