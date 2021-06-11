# CS172 - Final Project

## Team member 1 - Renzo Olivares
## Team member 2 - Phyllis Chen
## Team member 3 - Joshua Torres

### Overview: 
Using URLs to create documents, and utilizing Elasticsearch to index the documents, Croogle is a web crawler for cs.ucr.edu. 

#### In order to run Croogle:
- Python 3.7
- `pip install requests`
- `pip install lxml`
- `pip install BeautifulSoup4`

1. Run the builder.sh file to run crawler.py and indexer.py, which are parts 1 and 2 of the project.
2. Running runner.sh will allow the user to search through the index
    * For example, when prompted "Enter search: ", the user can query "CSE" to return results.


##### Part 1: Crawler
The crawler collects the URLs from seedurls.txt in order to begin crawling. There is a 0.5 second wait time for implicit politeness.

The crawler keeps a counter on the URL and assigns a document ID to it as well. Using the requests library, the crawler can get the text from the website and parse it using BeautifulSoup.

The crawler uses a similarity hash to check for previously visited URLs, and is also able to check if an href link is an extension of the current URL it is on.

 ##### needs storing explanation :)
##### Part 2: Indexer
The indexer takes all the documents that the crawler has collected and uses Elastic Search to index. 

##### needs moar here :)

##### Part 3: Extension
We have implemented a web-based interface using Flutter to display the user's query and the list of results returned by Elasticsearch.

Croogle UI:
![image](https://user-images.githubusercontent.com/43655330/121717413-fd16cd80-ca95-11eb-88e7-87fe88f11d26.png)

Croogle UI with a query:
![image](https://user-images.githubusercontent.com/43655330/121752722-98736700-cac5-11eb-8907-d9dc5064cd98.png)

