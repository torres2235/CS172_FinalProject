import requests

index = 'http://localhost:9200/test/_doc?pretty'
search = 'http://localhost:9200/test/_search?pretty'
headers = {"Content-Type": "application/json"}

doc = {"docno": "RJP0", "link": "www.cs.ucr.edu", "text": "CSE at UC Riverside We Engineer Excellence COVID-19 Updates Read More Your browser does not support the video tag. Creating the next generation of engineers, researchers, and scholars News CSE Professor Received Doctoral Dissertation Faculty Award 5/21/2021 Prof. Nael Abu-Ghazaleh received the Doctoral Dissertation Faculty Award which is a campus-wide award to faculty who provide excellent mentorship and support of their graduate students Read More CSE Professor Papalexakis received the NSF CAREER award 5/14/2021 The award will support work on autonomous tensor analysis. Read More ICPC team advances to North American Division Championship 3/19/2021 The UCR team, RGBMoon, will be one of nine teams advancing to the ICPC North American Division Championship. Read More All News Events UCR is in the Pacific time zone, but event times shown below are adjusted to the time zone of your device. Today Back Next 06/04/2021 — 09/02/2021 Month Week Day Agenda There are no events in this range. All Events Distinguished Lecture Series UCR Library Campus Store Career Opportunities Diversity Maps and Directions Visit UCR Department of Computer Science and Engineering Winston Chung Hall, Room 351 Bourns College of Engineering  Riverside, CA 92521-0429 Tel: (951) 827-5639 Fax: (951) 827-9345 Email:   contact@cs.ucr.edu Related Links Department Intranet Twitter Facebook Privacy Policy Terms and Conditions © 2019 Regents of the University of California"}

response = requests.post(index, headers=headers, json=doc)
search_query = { "query": { "match_all": {}}}
response2 = requests.get(search, headers=headers, json=search_query)

print(response.status_code)
print(response.text)
print(response2.status_code)
print(response2.text)