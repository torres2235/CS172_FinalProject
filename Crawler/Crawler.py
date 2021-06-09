'''
1.)take urls from seedUrls.txt
2.)remove from queue/ dequeue
3.)if already visited that website, go back to the queue for a new one
4.)if not visited, get the html
5.)write html to file
6.)parse html to extra links
7.)add extracted links to queue
8.) repeat from (2.)

Needed:
- Two Lists
    - queue
    - visited_urls (for check on (3.) )
- Library to get HTML
    - import requests (?)
    - import urllibs (?)
        - urllibs.request
- Scrapper
    - BeautifulSoup (?)
        - used to extract links
- Some way to check robots.txt
'''

import re
import time
import requests # helps get info from webpages
from bs4 import BeautifulSoup

#---------------------Globals-------------------#
url_list = []
queue = []
visited_urls = []
#-----------------------------------------------#

#---------------------Open our SeedUrls.txt file-------------------#
with open('../SeedUrls.txt', 'r') as urls:
    for line in urls:
        line = re.sub('\n',"", line)
        url_list.append(str(line))
urls.close()
#print(url_list)
#-------------------------------------------------------------------#

#-------------------------Stuff-----------------------#
def crawler(url):
    try:
        print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        #print(plain_text)
        #print(visited_urls)

        soup = BeautifulSoup(plain_text, features = "lxml") # be sure 'pip install lxml'

        for link in soup.findAll('a'): # 'a' is element for links
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            if href[0] == '/': # checks to see if the href is an extension of our current url
                current_url = url + href[1:-1]
                if current_url not in visited_urls:
                    queue.append(current_url)
                    visited_urls.append(current_url)
            else:
                if href not in visited_urls:
                    queue.append(href)
                    visited_urls.append(href)
    except:
        print('') # I get a "string index out of range" sometimes and idk why, so this check is here to help
            
    #print(queue)

for line in url_list: # start crawling our SeedUrls first
    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

for line in queue: # start crawling our queue
    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

#print(visited_urls)