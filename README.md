# capturador_notas_spreadsheet
python application to capture information from Google Sheet using a job scheduler.  

## Requirements:
- pip ( install google-api-python-client and schedule );
- Google Account Developer with sheet api credential;
  ( [Tutorial here](https://developers.google.com/sheets/api/quickstart/python) )
  
## How use this:
- change your credential .json file to "client_secret.json"

##### in quickstart.py do:
- set your ID and COLUMN_ID;
- set speadsheetid and rangeName at main().

##### in job_scheduler do:
-  set your schedule ( [tutorial here](https://pypi.python.org/pypi/schedule) )

##### in gmail_sender do:
- change parameters from create_message().

##### now execute 'python job_scheduler.py'
