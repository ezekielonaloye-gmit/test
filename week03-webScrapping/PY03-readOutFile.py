#Extract the first <tr> table row from the file 
#Lab03 question 4
from bs4 import BeautifulSoup

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.tr)