import requests
from urllib.parse import urlparse

class Downloader:
    def __init__(self, url, fileName):
        try:
            self.url = url
            if fileName:
                self.fileName = fileName
            else:
                self.fileName = parseName(self.url)

            # Request item from url
            self.requestItem()
            if self.response == 200:
                pass
                # Stream the object and save file
        except Exception as e:
            print("Couldn't initiate due to ", e)

    def parseName(self):
        name = urlparse(self.url)
        return name.path.split('/')[-1]

    def requestItem(self):
        try:
            self.response = requests.get(self.url, stream=True)
            return response
        except Exception as e:
            pass
