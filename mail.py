import smtplib
from db import get_records,update_sent_status
import traceback
import datetime
configs = [line.rstrip('\n') for line in open('configs')]
usr = configs[0]
pwd = configs[1]
rcvr = configs[2]
receivers = [rcvr]
date = datetime.datetime.now().date()
posts = []
jobs = get_records(0) #list of records that have not been sent
print(len(jobs))
for job in jobs:
    post_id = job[0]
    posts.append(post_id)
    url = job[1]
    # add for all needed elements

message = """From: JobUpdates <{usr}>
To: Dana <{rcvr}>
MIME-Version: 1.0
Content-type: text/html; charset=utf-8
Subject: New Job Postings: {date}

<p>Check out these postings you may have not have seen yet :)</p>
<h2>Jobs With Applitrack</h2>
<table>
    <tr>
        <th>EdPost Link</th>
        <th>AppliTrack Link</th>
        <th>AppliTrack ID</th>
        <th>Post DT</th>
        <th>Exp DT</th>
    </tr>
    <tr>
        <td><a href="https://edpost.stcloudstate.edu/EdPost/displayrecord?\
        postID=265025&submit=Search%20Entire%20Posting&KeyWordString=English\
        %20Teacher%20-%20Janesville%20Waldorf">EdPost Link</a>
        </td>
        <td><a href="https://www.applitrack.com/jwp/OnlineApp/JobPostings/\
        View.asp?AppliTrackJobId=249">AppliTrack</a></td>
        <td>a</td><td>date1</td>
        <td>date2</td>
    </tr>
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
</table>
""".format(usr=usr,rcvr=rcvr,date=date)

try:
    smtpObj = smtplib.SMTP('localhost',1025)
    smtpObj.login(usr,pwd)
    smtpObj.sendmail(usr, receivers, message)
    print "Successfully sent email"
except smtplib.SMTPException:
    print "Error: unable to send email"
    print traceback.format_exc()

#<head>
#    <style>
#        table {
#            font-family: arial, sans-serif;
#            border-collapse: collapse;
#            width: 100%;
#        }
#
#        td, th {
#            border: 1px solid #dddddd;
#            text-align: left;
#            padding: 8px;
#        }
#
#        tr:nth-child(even) {
#            background-color: #dddddd;
#        }
#    </style>
#</head>
