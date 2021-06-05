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
'''


