#!/usr/bin/env python
'''
Search MN teacher job postings on St. Cloud State University's EdPost Website.
Job postings are parsed for relevant information and inserted into a sqlite DB
which will be used to send automated alerts for new postings.

Author: Will Wermager will@wermager.me
'''

from bs4 import BeautifulSoup
import urllib2
import time
import sqlite3
from db import insert,update_sent_status,get_records,close_db
import random

DOMAIN = "https://edpost.stcloudstate.edu"

CONST_URL = DOMAIN+"/?page="

FILTER_URL = "&submit=Search+Entire+Posting&currentFilter="

SEARCH_STRINGS = ["english+teacher",\
                  "language+arts",\
                  "english+language+arts",\
                  "language+arts+teacher"]
jobs = []
all_jobs = []

# job ids currently in DB
id_list = [row[0] for row in get_records()]

# Retruns soup obj
def get_soup(url):
    wait = random.randint(5,10)
    print "Wait ",wait,"sec... Trying url:\n",url
    time.sleep(wait)
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc,'html.parser')
    return soup

# Checks if search result has multiple pages of listings
def has_next_page(soup):
    if len(soup.find_all('li',{"class":"PagedList-skipToNext"}))==0:
        return False
    else:
        print "Has additional page"
        return True

# returns edpost links of all jobs listed for search criteria passed
def get_jobs(search_str):
    page_num=1
    url = CONST_URL+str(page_num)+FILTER_URL+search_str
    soup = BeautifulSoup(" ",'html.parser')
    while has_next_page(soup) or page_num==1:
        soup = get_soup(url)
        jobs = soup.find_all('a',{"class":"jobtitle"})
        for job in jobs:
            link = DOMAIN + job['href']
            all_jobs.append(link)
        print len(jobs)," jobs on page ",page_num
        page_num += 1
        url=CONST_URL+str(page_num)+FILTER_URL+search_str
    return all_jobs

# if available gets applitrack posting link from edpost posting
def get_app_url(soup):
    app_a = soup.find('a',{"target":"AppliTrackPosting"})
    if app_a == None:
        return None
    return app_a['originalsrc']

# get edpost post_id
def get_post_id(edlink):
    return edlink.split("=")[1].split("&")[0].strip()

# get applitrack id app_id
def get_app_id(applink):
    if applink == None:
        return None
    return applink.split("=")[1]

# get app post_dt & exp_dt returns list
def get_dates(soup):
    post_dt = soup.find('p',{"class":"posted"})
    exp_dt = soup.find('p',{"class":"expire"})
    return post_dt.text,exp_dt.text


# gets all job links for a particular search string
for keyword in SEARCH_STRINGS:
    get_jobs(keyword)

# gets all data fields and inserts job into database
for url in all_jobs:
    post_id = int(get_post_id(url))

    if post_id not in id_list:
        print "Getting new job: ",post_id

        job_soup = get_soup(url)
        app_url = get_app_url(job_soup)
        app_id = get_app_id(app_url)
        post_dt = get_dates(job_soup)[0]
        exp_dt = get_dates(job_soup)[1]
        email_sent = 0

        print "insert ",post_id,"\n",\
                url,"\n",\
                app_url,"\n",\
                app_id,"\n",\
                post_dt,"\n",\
                exp_dt,"\n",\
                email_sent

        insert(post_id,url,app_url,app_id,post_dt,exp_dt,email_sent)
    else:
        print "Skipping job ",post_id,": ",url

close_db()
