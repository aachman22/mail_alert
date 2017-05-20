import imaplib
from values import *

import time
import tkinter as tk
from tkinter import messagebox

# Start timer
starttime=time.time()

# Create invisible window for alert
root = tk.Tk()
root.withdraw()


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

# Fetch the message header using the ID
for i in range(len(idlist)):
    status, msgHead = connection.fetch(idlist[i], '(BODY.PEEK[HEADER])')
    x1 = msgHead
    x2 = x1[0][1].decode("utf-8")
    x3 = x2.split('Subject')
    x4 = x3[1]
    x5 = x4.split('\r')
    subject = x5[0]
    print("The subject is", subject)
