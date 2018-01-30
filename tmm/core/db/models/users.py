import psycopg2
import logging
logging.basicConfig(filename='trace.log', level='DEBUG')


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

	def get_user_id(self, dbname, user, host, pwd):
		"""
		Use it to retrieve self postgres id.
		"""
		try:
			# connection database
			connection_str = "dbname='{}' user={} host={} password={}".format(dbname, user, host, pwd) 
			conn = psycopg2.connect(connection_str)
			logging.info('DATABASE: Connection established.')

			# create cursor
			cursor = conn.cursor()

			# retrieve user sql statement
			cursor.execute("""
				SELECT * FROM users 
				WHERE user_first_name = %s and user_last_name = %s""", (self.first_name, self.last_name))

			# fetch result
			row = cursor.fetchone()
			user_id = row[0]

			cursor.close()
			conn.commit()
			return user_id
		except Exception as e:
			raise e
