from bs4 import BeautifulSoup
import urllib2
import time
CONST_URL="https://edpost.stcloudstate.edu/?page="
FILTER_URL="&submit=Search+Entire+Posting&currentFilter="
SEARCH_STRINGS=["english+teacher","language+arts","english+language+arts","language+arts+teacher"]
jobs = []
all_jobs = []

print "--------------------------------------------------------"

def has_next_page(soup):
    if len(soup.find_all('li',{"class":"PagedList-skipToNext"}))==0:
        return False
    else:
        return True

def job_search(search_str):
    page_num=1
    url = CONST_URL+str(page_num)+FILTER_URL+search_str
    soup = BeautifulSoup(" ",'html.parser')
    print "Searching for jobs with keywords: ",search_str
    print "--------------------------------------------------------"
    while has_next_page(soup) or page_num==1:
        time.sleep(5) #Slow down call rate
        print "Trying url:\n",url
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc,'html.parser')
        jobs = soup.find_all('a',{"class":"jobtitle"})
        for job in jobs:
            all_jobs.append(job)
        print len(jobs)," jobs on page ",page_num
        page_num += 1
        url=CONST_URL+str(page_num)+FILTER_URL+search_str
    print "--------------------------------------------------------"
    return all_jobs

for keyword in SEARCH_STRINGS:
    job_search(keyword)
print "################################################"
print "Total jobs found: ",len(all_jobs)
for job in all_jobs:
    print(job.get_text())
