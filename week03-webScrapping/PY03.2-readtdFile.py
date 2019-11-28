#We get each row & the contents of TD  
#Lab03 question 6
from bs4 import BeautifulSoup

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    for col in cols:
        print(col.text)
    