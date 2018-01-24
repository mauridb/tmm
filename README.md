# TMM (Title Match Making)
"A tool that should help us to find a title about somethings passing inputs"

"Requirements installed:"
- Python3
- Postgresql

## Environment
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Create a local Postgresql database
```bash
$ sudo -i -u postgres
$ createuser <USER> -P --interactive	# insert your personale password
$ createdb <DATABASENAME>
```

## Create local settings launching following script
```bash
$ python3 create_local_settings.py
```

## Start the system
```bash
$ python3 run.py
```

"Yeah, it's working, enjoy! Feel free to contact me in pvt.."
