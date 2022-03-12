import requests  # allows us to grab the html page
from bs4 import BeautifulSoup  # Allows us to scrape
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup)  # will return in the form of html
# print(soup.body)
# print(soup.body.contents) in form of list
# print(soup.find_all('div')) 
# print(soup.find_all('a'))  # all  the links on the page
print(soup.title)
# find gives the first relatable while find_all :)...
# print(soup.select('a')) # selects all these tags
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2= soup2.select('.subtext')

mega_links = links +links2
mega_subtext=subtext+subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links,subtext):
	hn = []
	for idx,item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace('points',''))
			if points>99:
				hn.append({'title': title, 'link': href, 'votes':points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))
