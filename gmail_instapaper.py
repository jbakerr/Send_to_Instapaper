from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET = 'client_secret.json'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = build('gmail', 'v1', http=creds.authorize(Http()))

threads = GMAIL.users().threads().list(
    userId='me', q='from:nytdirect@nytimes.com'
).execute().get('threads', [])

for thread in threads:
    tdata = GMAIL.users().threads().get(userId='me', id=thread['id']).execute()
    nmsgs = len(tdata['messages'])

    msg = tdata['messages'][0]['payload']
    subject = ''
    for header in msg['headers']:
        if header['name'] == 'Subject':
            subject = header['value']
            break
    if subject:
        print(subject)

