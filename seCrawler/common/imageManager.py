import base64
from urlparse import urlparse

class imageManager():
    def isImageLink(self,url):
        res=urlparse(url)
        if (res.netloc=='' or res.scheme==''):
            return False,''
        else:
            return True,res.scheme

    def getImageBase64(self, imageSource):
        blink, domain = self.isFullLink(imageSource)
        if blink:
            #down load file and as as base64 and return it
            pass
        else:
            if base64.decodestring("imageSource"):
                return imageSource
            else:
                return imageSource.encode("base64")
