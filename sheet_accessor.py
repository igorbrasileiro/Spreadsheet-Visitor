# -*- coding: utf-8 -*-
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# tutorial link from Google: https://developers.google.com/sheets/api/quickstart/python
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'sheetacessor'

# column number that contains your identification
COLUMN_ID = 0
# Your Identification in Column:
ID = 'IGOR BRASILEIRO DUARTE'

def get_service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """

    service = get_service()
    spreadsheetId = '19GXPYvmKcXJT8UlnZevv7RDJQhCsvIxpLbSgHrJEPiA'
    rangeName = 'Notas!A2:G'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            if row[COLUMN_ID] == ID:
                return createMessageFromRow(row)

# this function capture columns that i want print, from row
def createMessageFromRow(row):
    message = ('Notas do aluno: %s' % row[COLUMN_ID])
    message += '\nNota1, Nota2, Nota3, Nota4, Media:'
    message += ('\n %s,   %s,   %s,   %s,   %s' % (row[1], row[2], row[3], row[4], row[6]))

    return message

if __name__ == '__main__':
    main()
