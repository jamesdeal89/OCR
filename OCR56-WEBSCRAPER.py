import urllib.request 
import urllib

def getWebsite(address):
	rawPage = urllib.request.urlopen(address).read().decode('utf-8')
	return rawPage

def getNextTarget(page):
	startLink = page.find("<a href=")
	if startLink == -1:
		return None, 0
	startQuote = page.find('"', startLink)
	endQuote = page.find('"', startQuote + 1)
	url = page[startQuote + 1 : endQuote]
	return url, endQuote

def findAllLinks(page):
	while True:
		url, endpos = getNextTarget(page)
		if url:
			print(url)
			page = page[endpos:]
		else:
			break

findAllLinks(getWebsite("https://www.rottentomatoes.com/"))