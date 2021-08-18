import re

class Extractor:
	def __init__(self, html):
		self.webpageHTML = html
		self.pattern = r'href=[\'"]?([^\'" >]+)'

	def parse(self):
		urls = re.findall(self.pattern, self.webpageHTML)
		return urls