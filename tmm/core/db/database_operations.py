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

	if kwargs['topic']:
		# insert into user
		try:
			topic = kwargs['topic']
			topic_user_id = topic.user.get_user_id(
				settings.DB_CONFIG['NAME'],
				settings.DB_CONFIG['USER'],
				settings.DB_CONFIG['HOST'],
				settings.DB_CONFIG['PASSWORD'],				
			)
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
				INSERT INTO topics (topic_title, topic_description, topic_user_id) VALUES (%s, %s, %s)
				""",
				(topic.title, topic.description, topic_user_id)
				)
			cursor.close()
			conn.commit()

		except Exception as e:
			raise e

	if kwargs['first_choice']:
		fc = kwargs['first_choice']
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
			INSERT INTO first_choices (first_choice_word) VALUES (%s)
			""",
			(fc.word,)
			)
		cursor.close()
		conn.commit()

	if kwargs['second_choice']:
		sc = kwargs['second_choice']
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
			INSERT INTO second_choices (second_choice_word) VALUES (%s)
			""",
			(sc.word,)
			)
		cursor.close()
		conn.commit()

	if kwargs['third_choice']:
		tc = kwargs['third_choice']
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
			INSERT INTO third_choices (third_choice_word) VALUES (%s)
			""",
			(tc.word,)
			)
		cursor.close()
		conn.commit()



def _read():
	# TODO
	pass

def _update():
	# TODO
	pass

def _delete():
	# TODO
	pass
	
