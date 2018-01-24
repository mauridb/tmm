import os
import sys


# exec 'cp' unix command
try:
	os.system('cp tmm/settings.py-example tmm/settings.py')
	sys.exit()
	
except Exception as e:
	print(e)
