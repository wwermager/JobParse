from bs4 import BeautifulSoup
import urllib2
import time
DOMAIN = "https://edpost.stcloudstate.edu"
CONST_URL = DOMAIN+"/?page="
FILTER_URL = "&submit=Search+Entire+Posting&currentFilter="
SEARCH_STRINGS = ["english+teacher"] #,"language+arts","english+language+arts","language+arts+teacher"]

jobs = []
all_links = []
new_list = []

print "--------------------------------------------------------"

def get_soup(url):
    time.sleep(5)
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc,'html.parser')
    return soup

def has_next_page(soup):
    if len(soup.find_all('li',{"class":"PagedList-skipToNext"}))==0:
        return False
    else:
        return True

def get_jobs(search_str):
    page_num=1
    url = CONST_URL+str(page_num)+FILTER_URL+search_str
    soup = BeautifulSoup(" ",'html.parser')
    print "Searching for jobs with keywords: ",search_str
    print "--------------------------------------------------------"
    while has_next_page(soup) or page_num==1:
        print "Trying url:\n",url
        #time.sleep(5) #Slow down call rate
        #html_doc = urllib2.urlopen(url)
        #soup = BeautifulSoup(html_doc,'html.parser')
        soup = get_soup(url)
        jobs = soup.find_all('a',{"class":"jobtitle"})
        for job in jobs:
            link = DOMAIN + job['href']
            all_links.append(link)
        print len(jobs)," jobs on page ",page_num
        page_num += 1
        url=CONST_URL+str(page_num)+FILTER_URL+search_str
    print "--------------------------------------------------------"
    return all_links

def get_application(link):
    soup = get_soup(link)
    app_a = soup.find('a',{"target":"AppliTrackPosting"})
    if app_a == None:
        return "No AppliTrack app for: " + link
    return app_a['originalsrc']

for keyword in SEARCH_STRINGS:
    get_jobs(keyword)
print "Total jobs found: ",len(all_links)
for link in all_links:
    #print str(link)
    print get_application(link)
#uniq_links = set(all_links)
#print len(uniq_jobs)," UNIQUE JOB LINKS!"
