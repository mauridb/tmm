"""
Platform configurations..
"""
import os

# database naming
DATABASE_NAME = 'database.csv'

# create columns of database
if DATABASE_NAME not in os.listdir():
	columns = input('Create database columns in comma separated value..\n').split(',')

# Description of the platform
TEXT_DESCRIPTION = "Description:\n- /registration \t---> register on platform \
		\n- /topic \t\t---> channel where you wanna insert\
		\n- /choices \t\t---> make your 3 choices to retrieve a list of titles\
		\n- /match making \t---> after 3 inputs start logic\
		\n- /save \t\t---> save your result in database..\
		\n- /exit \t\t---> Bye Bye :D "


