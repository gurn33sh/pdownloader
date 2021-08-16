import requests
from urllib.parse import urlparse

class Downloader:
    def __init__(self, url, fileName=None):
        try:
            self.url = url
            if fileName:
                self.fileName = fileName
            else:
                self.fileName = self.parseName()
            # Request item from url
            self.requestItem()
            if self.response.status_code == 200:
                self.saveFile()
                # Stream the object and save file
        except Exception as e:
            print("Couldn't initiate due to ", e)

    def parseName(self):
        name = urlparse(self.url)
        return name.path.split('/')[-1]

    def requestItem(self):
        try:
            self.response = requests.get(self.url, stream=True)
        except Exception as e:
            pass

    def saveFile(self):
        with open(self.fileName, 'wb') as f:
            for chunk in self.response.iter_content(chunk_size=8192): 
                if chunk: 
                    f.write(chunk)
