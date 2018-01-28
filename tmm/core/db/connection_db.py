import os
import sys
import psycopg2
import logging


COMMANDS = [
	"""
	CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            user_first_name VARCHAR(255) NOT NULL,
            user_last_name	VARCHAR(255) NOT NULL
        )
	""",
	"""
	CREATE TABLE IF NOT EXISTS topics (
			topic_id SERIAL PRIMARY KEY,
			topic_title VARCHAR(255) NOT NULL,
			topic_description VARCHAR(500),
			topic_user_id INT REFERENCES users(user_id)
		)
	""",
	"""
	CREATE TABLE IF NOT EXISTS first_choices (
			first_choice_id SERIAL PRIMARY KEY,
			first_choice_word VARCHAR(255) NOT NULL
		)
	""",
	"""
	CREATE TABLE IF NOT EXISTS second_choices (
			second_choices_id SERIAL PRIMARY KEY,
			second_choices_word VARCHAR(255) NOT NULL
		)

	""",
	"""
	CREATE TABLE IF NOT EXISTS third_choices (
			third_choices_id SERIAL PRIMARY KEY,
			third_choices_word VARCHAR(255) NOT NULL
		)
	""",
	"""
	CREATE TABLE IF NOT EXISTS logs (
			log_id SERIAL PRIMARY KEY,
			log_name VARCHAR(50) NOT NULL,
			log_message TEXT
		)
	"""
]

def connection_db(dbname, user, host, pwd):
	try:
		# establish connection
		connection_str = "dbname='{}' user={} host={} password={}".format(dbname, user, host, pwd) 
		conn = psycopg2.connect(connection_str)
		logging.info('DATABASE: Connection established.')

		# create cursor
		cursor = conn.cursor()

		# create simple table
		for command in COMMANDS:
			cursor.execute(command)

		cursor.close()
		conn.commit()
	except Exception as e:
		print(e)
