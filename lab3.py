import requests
from bs4 import BeautifulSoup


url = "http://www.pracuj.pl/praca/informatyk;kw/pomorskie;r,9"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>"%(link.get("href"),link.text)
	
	
g_data = soup.find_all("h2", {"class": "offer__list_item_link"})

for item in g_data:
	print item.text
	