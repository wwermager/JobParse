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
edpost_tbl_rows= ""
ed_posts = get_records(0) # * non-appli and  unsent
ed_posts_sent = get_records(1) # post_id
uniq_appli = [row[0] for row in get_records(2)] # unique app_id's
all_appli = get_records(3) # all appli and unsent
all_appli_sent = get_records(4) # app_id
all_post_ids = get_records() # all post_ids in db

print "Edpost sent ...",len(ed_posts_sent)
print "Applitrack unique ...",len(uniq_appli)
print "All Applitrack unsent...",len(all_appli)
print "All Applitrack sent...",len(all_appli_sent)
print "Total posts in DB...",len(all_post_ids)

# Transform db data into html table row format
for row in ed_posts:
    edpost_tbl_rows += \
            "<tr style=\"border:1px solid black\"><td style=\"border:1px solid black\">"\
            +str(row[0])\
            +"</td><td style=\"border:1px solid black\"><a href="\
            +'"'\
            +row[1]\
            +'"'\
            +">"\
            +row[4]\
            +"</a></td><td style=\"border:1px solid black\">"\
            +row[5]\
            +"</td><td style=\"border:1px solid black\">"\
            +row[6]\
            +"</td></tr>"


# if new records have applitrack ID verify no previous records with same ID
# have been sent
#  if it has been sent update the record is_sent=1

print "Edpost not sent...",len(ed_posts)
if len(uniq_appli) == 0:
    #TODO for each unique post generate table string
    print "EMPTY IF"

message = """From: JobUpdates <{usr}>
To: Will <{rcvr}>
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
<table style="width:100%;border:1px solid black">
    <tr style="border:1px solid black">
        <th style="border:1px solid black">EdPost ID</th>
        <th style="border:1px solid black">Description</th>
        <th style="border:1px solid black">Post DT</th>
        <th style="border:1px solid black">Exp DT</th>
    </tr>
    {edpost_tbl_rows}
</table>
""".format(usr=usr,rcvr=rcvr,date=date,edpost_tbl_rows=edpost_tbl_rows)

#try:
#    smtpObj = smtplib.SMTP('localhost',1025)
#    smtpObj.login(usr,pwd)
#    smtpObj.sendmail(usr, receivers, message)
#    print "Successfully sent email"
#    # TODO add logic to update sent status
#except smtplib.SMTPException:
#    print "Error: unable to send email"
#    print traceback.format_exc()
