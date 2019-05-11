#!/usr/bin/env python

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
appli_tbl_rows= ""

ed_posts = get_records(0) # * non-appli and  unsent
ed_posts_ids = [row[0] for row in ed_posts]
ed_posts_sent = get_records(1) # post_id

uniq_appli = get_records(2) # unique unsent appli
uniq_appli_ids = [row[0] for row in uniq_appli]

all_appli_sent = [row[0] for row in get_records(4)] # all app_id sent
all_appli_unsent = [row[0] for row in get_records(5)] # all app_id unsent


# No jobs to send so exit
if len(all_appli_unsent) == 0 and len(ed_posts) == 0:
    print "Exit: No new unique posts.."
    exit()

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

# Transform applitrack posts into html table
for row in uniq_appli:
    # check if sent before - app_id not unique on edpost
    if row[3] not in all_appli_sent:
        print "New unique & unsent applitrack post... ",row[3]
        appli_tbl_rows += \
            "<tr style=\"border:1px solid black\"><td style=\"border:1px solid black\">"\
            +str(row[0])\
            +"</td><td style=\"border:1px solid black\"><a href="\
            +'"'\
            +row[2]\
            +'"'\
            +">"\
            +str(row[3])\
            +"</a></td><td style=\"border:1px solid black\"><a href="\
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
    else:
        print "Skipping applitrack post... ",row[3]


message = """From: JobUpdates <{usr}>
To: Dana <{rcvr}>
MIME-Version: 1.0
Content-type: text/html; charset=utf-8
Subject: New Job Postings: {date}

<p>Check out these postings you may have not have seen yet :)</p>
<p>Searched: english teacher, language arts, english language arts, language
artarts, and language arts teacher.

<h2>Jobs With Applitrack</h2>
<table style="width:100%;border:1px solid black">
    <tr style="border:1px solid black">
        <th style="border:1px solid black">EdPost ID</th>
        <th style="border:1px solid black">AppliTrack ID</th>
        <th style="border:1px solid black">Description</th>
        <th style="border:1px solid black">Post DT</th>
        <th style="border:1px solid black">Exp DT</th>
    </tr>
    {appli_tbl_rows}
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
""".format(usr=usr,rcvr=rcvr,date=date,edpost_tbl_rows=edpost_tbl_rows,appli_tbl_rows=appli_tbl_rows)

try:
    smtpObj = smtplib.SMTP('localhost',1025)
    smtpObj.login(usr,pwd)
    smtpObj.sendmail(usr, rcvr, message)
    print "Successfully sent email... "
    for post_id in ed_posts_ids:
        print "Update sent status on EdPost... ",post_id
        update_sent_status(post_id)

    for app_id in all_appli_unsent:
        print "Update sent status on Appli... ",app_id
        update_sent_status(app_id,1)

except smtplib.SMTPException:
    print "ERROR: unable to send email... "
    print traceback.format_exc()
