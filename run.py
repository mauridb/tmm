import os
import sys
import time
import logging
logging.basicConfig(filename='trace.log', level='DEBUG')

from tmm import settings

from tmm.core.system import registration, create_topic, make_choices, match_making_system
from tmm.core.db.database_operations import _create, _read, _delete
from tmm.core.db.migrate import migrate
from tmm.core.db.connection_db import connection_db

def main():
	"""
	Main application
	"""
	print(settings.TEXT_DESCRIPTION, end='\n\n')

	if settings.DEBUG == True:
		data = {}
	
	while 1:
		UI = sys.stdin.readline().strip() # trim whitespaces
		# sys.stdout.write(user_interface)
		# sys.stdout.flush()


		# check ui for user registration
		if UI == '/registration':
			logging.info('I am creating user')
			user = registration()
			logging.info('User succesfully created!')

		# check ui to subscribe in a specific topic
		if UI == '/topic':
			logging.info('I am creating topic')			
			topic = create_topic(user)
			logging.info('Topic succesfully created')

		# check ui start input choices
		if UI == '/choices':
			logging.info('I am creating choices')
			first_choice, second_choice, third_choice = make_choices()
			logging.info('Choices are created succesfully!')

		# check ui to launch the logic of the system
		if UI == '/match making':
			logging.info('Started match making system!')
			match_making_system()
			logging.info('Completed match making system!')
			
		# check ui to exit the platform
		if UI == '/query':
			logging.info('Query database models..')
			_read()		
		
		# query on database
		if UI == '/delete':
			logging.info('Delete data..')
			_delete()
		
		# store data into database
		if UI == '/save':
			logging.info('Storing data..')
			_create(
				user=user, 
				topic=topic, 
				first_choice=first_choice, 
				second_choice=second_choice, 
				third_choice=third_choice
				)				
		
		# check ui to exit the platform
		if UI == '/exit':
			logging.info('Good bye, enjoy! <3')
			break

if __name__ == '__main__':
	# connection database
	connection_db(
		settings.DB_CONFIG['NAME'], 
		settings.DB_CONFIG['USER'], 
		settings.DB_CONFIG['HOST'],
		settings.DB_CONFIG['PASSWORD']
	)

	# main application start
	main()