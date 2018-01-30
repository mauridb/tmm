"""
Platform configurations..
"""
import os
import sys


# todo: environment production, development

# file names

# Debug mode
DEBUG = True

# Description of the platform
TEXT_DESCRIPTION = "Description:\n- /registration \t---> register on platform \
		\n- /topic \t\t---> channel where you wanna insert\
		\n- /choices \t\t---> make your 3 choices to retrieve a list of titles\
		\n- /match making \t---> after 3 inputs start logic\
		\n- /save \t\t---> save your result in database..\
		\n- /query \t\t---> query database fields..\
		\n- /exit \t\t---> Bye Bye :D "


# DATABASE CONFIGURATIONS
DB_CONFIG = {
	"NAME": "testpython",
	"USER": "mauridb",
	"HOST": "localhost",
	"PASSWORD": "mauridb"
}
