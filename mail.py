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
non_appli = get_records(0)
appli = get_records(2)
all_appli = get_records(3)

#TODO get all records that have not been sent yet
# if new records have applitrack ID verify no previous records with same ID
# have been sent
#  if it has been sent update the record is_sent=1

print "Non applitrack ...",len(non_appli)
print "Applitrack unique ...",len(appli)
print "All Applitrack ...",len(all_appli)


message = """From: JobUpdates <{usr}>
To: Dana <{rcvr}>
MIME-Version: 1.0
Content-type: text/html; charset=utf-8
Subject: New Job Postings: {date}

<p>Check out these postings you may have not have seen yet :)</p>
<h2>Jobs With Applitrack</h2>
<table style="width:100%;border:1px solid black">
    <tr style="border:1px solid black">
        <th style="border:1px solid black">EdPost Link</th>
        <th style="border:1px solid black">AppliTrack Link</th>
        <th style="border:1px solid black">AppliTrack ID</th>
        <th style="border:1px solid black">Post DT</th>
        <th style="border:1px solid black">Exp DT</th>
    </tr>
    <tr style="border:1px solid black">
        <td style="border:1px solid black"><a href="https://edpost.stcloudstate.edu/EdPost/displayrecord?postID=265025&submit=Search%20Entire%20Posting&KeyWordString=English%20Teacher%20-%20Janesville%20Waldorf">EdPost Link</a>
        </td>
        <td style="border:1px solid black"><a href="https://www.applitrack.com/jwp/OnlineApp/JobPostings/View.asp?AppliTrackJobId=249">AppliTrack</a></td>
        <td style="border:1px solid black">a</td>
        <td style="border:1px solid black">date1</td>
        <td style="border:1px solid black">date2</td>
    </tr>
</table>
</br>
</br>
<h2>Jobs Without Applitrack</h2>
<table>
    <tr style="border:1px solid black">
        <th style="border:1px solid black">EdPost Link</th>
        <th style="border:1px solid black">Post DT</th>
        <th style="border:1px solid black">Exp DT</th>
    </tr>
</table>
""".format(usr=usr,rcvr=rcvr,date=date)

#try:
#    smtpObj = smtplib.SMTP('localhost',1025)
#    smtpObj.login(usr,pwd)
#    smtpObj.sendmail(usr, receivers, message)
#    print "Successfully sent email"
#except smtplib.SMTPException:
#    print "Error: unable to send email"
#    print traceback.format_exc()
