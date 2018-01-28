class Log(object):
	"""Log model representation to track every log into database."""
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	# TODO
