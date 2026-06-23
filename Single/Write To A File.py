# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
 
import requests
from bs4 import BeautifulSoup
 
base_url = 'https://www.nytimes.com'
r = requests.get(base_url) # GET request for the HTML from nytimes 
soup = BeautifulSoup(r.text, "html.parser") # Take the HTML code from the nytimes website

filename = input("File to save to: ")

with open(filename, 'w') as f:
    for story_heading in soup.find_all(class_="css-xdandi"): # Inspect element and search the headlines to find the class used 
        if story_heading.a: 
            f.write(story_heading.a.text.replace("\n", " ").strip())
        else: 
            f.write(story_heading.contents[0].get_text().strip())

# Not completely my own work. Followed along with solutions: https://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html
