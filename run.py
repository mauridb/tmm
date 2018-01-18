import os
import sys
import logging
logging.basicConfig(filename='trace.log', level='DEBUG')

from tmm.users import User
from tmm.choices import FirstChoice, SecondChoice, ThirdChoice
from tmm.topics import Topic

def main():
	"""
	Main application
	"""
	print("Description:\n- /registration ---> register on platform \
		\n- /match making ---> after 3 inputs start logic\
		\n- /topic ---> channel where you wanna insert\
		\n- /choices ---> make your 3 choices to retrieve a list of titles\
		\n- /exit ---> Bye Bye :D ", end='\n\n')	
	while 1:
		UI = sys.stdin.readline().strip() # trim whitespaces
		# sys.stdout.write(user_interface)
		# sys.stdout.flush()


		# check ui for user registration
		if UI == '/registration':
			# TODO
			print(' registration command')

		# check ui to subscribe in a specific topic
		if UI == '/topic':
			# TODO
			print(' topic command')

		# check ui start input choices
		if UI == '/choices':
			# TODO
			print(' choices command')

		# check ui to launch the logic of the system
		if UI == '/match making':
			print(' match making command')
			
		# check ui to exit the platform
		if UI == '/exit':
			break

if __name__ == '__main__':
	main()