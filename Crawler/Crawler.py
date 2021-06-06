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
import requests # helps get info from webpages
from bs4 import BeautifulSoup

url_list = []
with open('../SeedUrls.txt', 'r') as urls:
    for line in urls:
        line = re.sub('\n',"", line)
        url_list.append(str(line))
urls.close()
#print(url_list)

source_code = requests.get(url_list[0])
plain_text = source_code.text
#print(plain_text)

soup = BeautifulSoup(plain_text, features = "lxml") # be sure 'pip install lxml' 
for link in soup.findAll('a'): # 'a' is element for links
    href = link.get('href')
    title = link.string
    print(href)
    print(title)