import requests

class restclient:
    def __init__(self,url:str)->None:
        self.url = url
    
    def get(self,id = ""):

        uri = self.url+ "/"+id
        response = requests.get(uri)
        return response.text

