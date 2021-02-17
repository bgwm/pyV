import email, getpass, imaplib, os, re

acct = "gzjisfuckingaswsomecanyoubelievethat@gmail.com"
pwd = "123456789"

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(acct, pwd)

m.select("Inbox")

resp, items = m.search(None, "UNSEEN")
items = items[0].split()
items = items[::-1]

chunkSize = 11 
metaChunk = [items[i:i + chunkSize] for i in range(0, len(items), n)]

print ("metaChunk DONE")

c = 1
dataSet = [];
for items in metaChunk:
    for id in items:#[::-1]: 
        resp, data = m.fetch(id, "(BODY.PEEK[HEADER])")
        dataSet.append(data[0][1])
        print ("[%d]"%(c), end=", ", flush=True),
        c = c+1

m.logout()

print ("size: %d" % (len(dataSet)))
print ("dataSet DONE")

i = 0
content = []
for data in dataSet:
    mail = email.message_from_string(data.decode('utf-8', 'ignore'))

    row = mail["From"] + ";" + mail["Date"] + ";\n"
    content.append(row);
    
    print(row, end=', ', flush=True)

print ("content DONE")

c = 1 
fileName = "./out/header-4.csv";
with open(fileName, "r+") as f:
    d = f.read()
    for row in content:
        f.write(row)
        print ("{%d}"%(c), end=", ", flush=True)
        c = c+1
    f.close()



