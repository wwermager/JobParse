import smtplib
from db import get_records,update_sent_status
import traceback
import datetime
configs = [line.rstrip('\n') for line in open('configs')]
usr = configs[0]
pwd = configs[1]
rcvr = configs[2]

job = get_records(0) #records that have not been sent

date = datetime.datetime.now().date()
receivers = [rcvr]
message = """From: JobUpdates <{usr}>
To: Dana <{rcvr}>
MIME-Version: 1.0
Content-type: text/html; charset=utf-8
Subject: New Job Postings: {date}

<p>Check out these postings you may have not have seen yet :)</p>
<h2>Jobs With Applitrack</h2>
<head>
    <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
    </style>
</head>
<table>
    <tr>
        <th>EdPost Link</th>
        <th>AppliTrack Link</th>
        <th>AppliTrack ID</th>
        <th>Post DT</th>
        <th>Exp DT</th>
    </tr>
    <tr>{appli records}</tr>
</table>
</br>
</br>
<h2>Jobs Without Applitrack</h2>
<table>
    <tr>
        <th>EdPost Link</th>
        <th>Post DT</th>
        <th>Exp DT</th>
    </tr>
    <tr>{non-appli records}</tr>
</table>

""".format(**locals())
try:
    smtpObj = smtplib.SMTP('localhost',1025)
    smtpObj.login(usr,pwd)
    smtpObj.sendmail(usr, receivers, message)
    print "Successfully sent email"
except smtplib.SMTPException:
    print "Error: unable to send email"
    print traceback.format_exc()

