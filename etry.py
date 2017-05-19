import imaplib
from values import *

# Open connection
connection = imaplib.IMAP4_SSL(mailserver)

# Login
connection.login(emailid, password)

# Get folder info of INBOX
folderStat, unseenInfo = connection.status('INBOX', "(UNSEEN)")
# print(unseenInfo[0])

# Decoding byte object to string object
x = unseenInfo[0].decode("utf-8")

# Create counter for unread emails
unreadCounter = int(x.split()[2].strip(').,]'))

# Folder list
status, folderList = connection.list()

# Selecting the folder
status, data = connection.select('INBOX')

# Search using keywords in INBOX

status, message = connection.search(None, '(SUBJECT "Enter your keyword")')

# Store the list of ids in a list
strmessage = message[0].decode("utf-8")
idlist = strmessage.split(' ')
# print(idlist)

# Fetch the message geader using the ID
for i in range(len(idlist)):
    status, msgHead = connection.fetch(idlist[i], '(BODY.PEEK[HEADER])')
    x1 = msgHead
    x2 = x1[0][1].decode("utf-8")
    x3 = x2.split('Subject')
    x4 = x3[1]
    x5 = x4.split('\r')
    subject = x5[0]
    print("The subject is", subject)

# Fetch the full message
# status, fullMsg = connection.fetch('4761', '(RFC822)')
# print(fullMsg)
