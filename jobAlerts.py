from bs4 import BeautifulSoup
import urllib2
import time

SEARCH_STRINGS=["english+teacher","language+arts","english+language+arts","language+arts+teacher"]
jobs = []
all_jobs = []

print "----------------------------------------------------------"

for srchStr in SEARCH_STRINGS:
    print "Wating 5 seconds"
    time.sleep(5) #Slow down call rate
    url = "https://edpost.stcloudstate.edu/?KeyWordString="+srchStr+"&StateCityZipString=&submit=Search+Entire+Posting"
    print "Trying url:\n",url
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc,'html.parser')
    #print(soup.prettify())
    jobs = soup.find_all('a',{"class":"jobtitle"})
    print "With search string ",srchStr," found ",len(jobs)," jobs."
    print "----------------------------------------------------------"
    for job in jobs:
        all_jobs.append(job)

print "Total jobs found: ",len(all_jobs)
for job in all_jobs:
    print(job.get_text())
