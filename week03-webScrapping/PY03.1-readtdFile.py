#Modify to extract all the <tr> in file  
#Lab03 question 5
from bs4 import BeautifulSoup

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

rows = soup.findAll("tr")
for row in rows:
    print("------------")
    print(row)