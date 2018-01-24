import os
import sys
import psycopg2
import logging


def connection_db(dbname, user, host, pwd):
	try:
		# establish connection
		connection_str = "dbname='{}' user={} host={} password={}".format(dbname, user, host, pwd) 
		conn = psycopg2.connect(connection_str)
		logging.info('DATABASE: Connection established.')

		# create cursor
		cursor = conn.cursor()

		# create simple table
		cursor.execute("""CREATE TABLE tutorials (name char(50));""")

		# run a SELECT statement
		cursor.execute("""SELECT * FROM tutorials""")
		rows = cursor.fetchall()
		print(rows)
	except Exception as e:
		print(e)
