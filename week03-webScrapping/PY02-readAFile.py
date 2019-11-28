#test you can read a file <carviewer2.html> 
#Lab03 question 3 
from bs4 import BeautifulSoup

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())