import imaplib
from values import *

# Open connection
connection = imaplib.IMAP4_SSL(mailserver)

# Login
connection.login(emailid, password)

# Get folder info of INBOX
folderStat, unseenInfo = connection.status('INBOX', "(UNSEEN)")

# Decoding byte object to string object
x = unseenInfo[0].decode("utf-8")

# Create counter for unread emails
unreadCounter = int(x.split()[2].strip(').,]'))

# Folder list
status, folderList = connection.list()

# Selecting the folder
status, data = connection.select('INBOX')

# Search using keyword in INBOX
status, message = connection.search(None, '(SUBJECT "%s")' %keyword)

# Store the list of ids in a list
strmessage = message[0].decode("utf-8")
idlist = strmessage.split(' ')
oldmaxid = max(idlist)
#print(idlist)
