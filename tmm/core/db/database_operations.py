import os
import sys
import csv
import time
import psycopg2
import logging
logging.basicConfig(filename='database.log', level='DEBUG')

from tmm import settings


def _create(**kwargs):
	# TODO: topic, first choice, second choice, third choice, log
	if kwargs['user']:
		# insert into user
		try:
			user = kwargs['user']
			connection_str = "dbname='{}' user={} host={} password={}".format(
				settings.DB_CONFIG['NAME'], 
				settings.DB_CONFIG['USER'], 
				settings.DB_CONFIG['HOST'], 
				settings.DB_CONFIG['PASSWORD']
			) 
			conn = psycopg2.connect(connection_str)
			logging.info('DATABASE: Connection established.')
			cursor = conn.cursor()
			cursor.execute("""
				INSERT INTO users (user_first_name, user_last_name) VALUES (%s, %s)
				""",
				(user.first_name, user.last_name)
				)
			cursor.close()
			conn.commit()

		except Exception as e:
			print(e)


def _read():
	# TODO
	pass

def _update():
	# TODO
	pass

def _delete():
	# TODO
	pass
	
