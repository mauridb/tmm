import os
import sys
import csv
import time
import logging
logging.basicConfig(filename='database.log', level='DEBUG')

from tmm import settings

def _create(*args):
	print(args[0]['TOPIC'])
	with open(settings.DATABASE_NAME, 'a', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow([
					args[0]['FULLNAME'],
					args[0]['TOPIC'],
					args[0]['FIRST_CHOICE'],
					args[0]['SECOND_CHOICE'],
					args[0]['THIRD_CHOICE'],
					time.strftime('%Y-%m-%d %H:%M'),
					input('Leave a comment to improve the platform..\n')
			])
	
def _read(db):
	with open(db, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print(row)

def _update():
	# TODO
	pass

def _delete(index):
	# TODO
	pass
	
