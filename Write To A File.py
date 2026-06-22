# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
 
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

# Above code taken from solution here: https://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

