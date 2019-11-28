#We retrieve a webpage from the web with below code. 
#Lab 03 question 1
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)