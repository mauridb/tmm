import os
import sys
import logging
logging.basicConfig(filename='trace.log', level='DEBUG')

from tmm.core.db.models.users import User
from tmm.core.db.models.choices import FirstChoice, SecondChoice, ThirdChoice
from tmm.core.db.models.topics import Topic

from tmm.core.db.database_operations import _create


def registration():
	# create user
	user = User()
	user.set_first_name(input('Insert your first_name..\n'))
	user.set_last_name(input('Insert your last_name..\n'))
	return user

def create_topic():
	topic = Topic(title=input('Type a topic for your attempt..\n'))
	return topic

def make_choices():
	fc = FirstChoice(word=input('Type your first choice..\n'))
	sc = SecondChoice(word=input('Type your second choice..\n'))
	tc = ThirdChoice(word=input('Type your third choice..\n'))
	return (fc, sc, tc)

def match_making_system():
	print('i am match_making_system method')

