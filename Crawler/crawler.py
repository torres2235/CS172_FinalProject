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
from sys import setdlopenflags
import time
import requests # helps get info from webpages
from doc import Doc
from bs4 import BeautifulSoup

#---------------------Globals-------------------#
url_list = []
queue = []
docs = []
visited_urls = dict()
crawled_count = 0
doc_id = 0
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
    global crawled_count, doc_id

    try:
        print(url)
        source_code = requests.get(url)
        plain_text = source_code.text

        # print(plain_text)
        #print(visited_urls)

        soup = BeautifulSoup(plain_text, features = "lxml") # be sure 'pip install lxml'
        # print(soup.get_text(separator=' '))
        docs.append(Doc('RJP' + str(doc_id), soup.get_text(separator=' ')))

        for link in soup.findAll('a'): # 'a' is element for links
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            if href[0] == '/': # checks to see if the href is an extension of our current url
                current_url = url + href[1:-1]
                if current_url not in visited_urls:
                    queue.append(current_url)
                    visited_urls[current_url] = 1
            else:
                if href not in visited_urls:
                    queue.append(href)
                    visited_urls[href] = 1
        
        crawled_count += 1
        doc_id += 1
    except:
        print('') # I get a "string index out of range" sometimes and idk why, so this check is here to help
            
    #print(queue)

for line in url_list: # start crawling our SeedUrls first
    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

for line in queue: # start crawling our queue
    if crawled_count == 3:
        break

    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

open('testdoc', 'w').close()

test_doc = open('testdoc', 'a')

for doc in docs:
    test_doc.write('<DOC>\n')
    test_doc.write(f'<DOCNO> {doc.docno} </DOCNO>\n')
    test_doc.write(f'<TEXT>\n')
    test_doc.write(f'{doc.text}\n')
    test_doc.write('</TEXT>\n')
    test_doc.write('</DOC>')
    print('DOCNO: ' + doc.docno)
    print('\n')
    print('TEXT: ' + doc.text)

test_doc.close()
#print(visited_urls)

#we have an initial link that we crawl first
#we pull all the links in there and at it to our queue
#then we crawl the queue and repeat 

#parent and its children links go in 1 doc file.
#parent RJP0-0, and children RJP0-1, RJP0-2.......