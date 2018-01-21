import os
import sys
import csv


def migrate(db, cols):
	"""
	Params:
	- db: name of the database
	- cols: columns of the database
	"""
	if db not in os.listdir():
		with open(db, 'a', newline='') as database:
			# create columns of the database csv
			fieldnames = cols
			writer = csv.DictWriter(database, fieldnames=fieldnames)
			writer.writeheader()
	else:
		logging.info('Database already created!')
