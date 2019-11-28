#Text in the columns stored in a list
#Lab03 question 7
from bs4 import BeautifulSoup

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

rows = soup.findAll("tr")
for row in rows:
    dataList = []
    for col in cols:
        dataList.append(col.text)
    print (dataList)