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
from bs4 import BeautifulSoup
import string
import hashlib
import sys
import json
import os

#---------------------Globals-------------------#
url_list = []
queue = []
docs = []
visited_urls = dict()
crawled_count = 0
doc_id = 0

sim_hashes = dict()
#-----------------------------------------------#

#---------------------Open our SeedUrls.txt file-------------------#
with open('../seedurls.txt', 'r') as urls:
    for line in urls:
        line = re.sub('\n',"", line)
        url_list.append(str(line))
urls.close()
#print(url_list)
#-------------------------------------------------------------------#

def remove_punctuation(token):
    return token.translate(str.maketrans('', '', string.punctuation))

def remove_stop_words(set_of_tokens, set_of_stop_words):
    for stop_word in set_of_stop_words:
        stop_word_regex = re.compile(r'\b{0}\b'.format(stop_word))
        set_of_tokens = re.sub(stop_word_regex, '', set_of_tokens)

    return set_of_tokens

token_regex = re.compile(r'\w+(?:\.?\w+)*')

# Load stop words
stop_words_file = open('stopwords.txt', 'r')
stop_words = []
for line in stop_words_file:
    stop_words.extend(line.split())
stop_words_file.close()

#-------------------------Stuff-----------------------#
def crawler(url):
    global crawled_count, doc_id

    try:
        print(url)
        raw_website = requests.get(url)
        raw_html = raw_website.text

        parsed_html = BeautifulSoup(raw_html, features = "lxml") # be sure 'pip install lxml'
        is_content_seen = content_seen(parsed_html.get_text(separator= ' '))

        if is_content_seen:
            return

        full_doc_id = 'RJP' + str(doc_id)
        docs.append({"docno" : full_doc_id, "url": url, "text": parsed_html.get_text(separator=' ')})

        parsed_links = parsed_html.findAll('a')
        # robot_url_filter(parsed_links)
        dup_url_eliminator(parsed_links, url)
        
        crawled_count += 1
        doc_id += 1
    except:
        print('') # I get a "string index out of range" sometimes and idk why, so this check is here to help
            
    #print(queue)

def content_seen(text):
    global sim_hash

    content_hash = sim_hash(text)

    if content_hash in sim_hashes:
        return True
    else:
        sim_hashes[content_hash] = 1
        return False

def dup_url_eliminator(links, url):
    global queue

    for link in links:
        href = link.get('href')

        if href[0] == '/': # checks to see if the href is an extension of our current url
            current_url = url + href[1:-1]
            if current_url not in visited_urls:
                queue.append(current_url)
                visited_urls[current_url] = 1
        else:
            if href not in visited_urls:
                queue.append(href)
                visited_urls[href] = 1

def robot_url_filter(links):
    #Our target www1.cs.ucr.edu does not have any forbidden links
    return

def sim_hash(text):
    global token_regex, sim_hashes

    text = remove_punctuation(text).lower()
    text = remove_stop_words(text, stop_words)
    tokens = re.findall(token_regex, text)

    hashes = dict()
    weights = dict()

    for token in tokens:
        if token not in weights:
            weights[token] = 1
        else:
            weights[token] += 1

    for token in tokens:
        hash = (bin(int(hashlib.sha256(bytes(token, encoding='utf-8')).hexdigest(), 16)))[2:]

        if len(hash) < 256:
            diff = 256 - len(hash)
            offset = ''
            for i in range(diff):
                offset += '0'
            hash = offset + hash
        
        hashes[token] = list(map(int, hash))

    final_hash = []

    current_sum_column = 0
    current_bit = 0

    while(True):
        if current_sum_column == 256:
            break

        for token, value in hashes.items():
            current_bit += value[current_sum_column] * weights[token] if value[current_sum_column] > 0 else -1 * weights[token]

        current_sum_column += 1
        final_hash.append(current_bit)
        current_bit = 0

    for i in range(len(final_hash)):
        final_hash[i] = 1 if final_hash[i] > 0 else 0

    final_hash = int("".join(map(str,final_hash)))

    return final_hash

for line in url_list: # start crawling our SeedUrls first
    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

for line in queue: # start crawling our queue
    if crawled_count == 4:
        break

    crawler(line)
    time.sleep(0.5) # wait 0.5secs for implicit politeness

for doc in docs:
    json_object = json.dumps(doc, indent=4)
    json_file = open(os.path.join('../indexer/docs/', f'{doc["docno"]}.json'), 'w')
    json_file.write(json_object)
    json_file.close()
#print(visited_urls)

#we have an initial link that we crawl first
#we pull all the links in there and at it to our queue
#then we crawl the queue and repeat 

#parent and its children links go in 1 doc file.
#parent RJP0-0, and children RJP0-1, RJP0-2.......
