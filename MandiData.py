import requests
from pprint import pprint

apikey = "579b464db66ec23bdd000001d18f8b46035d4f0373893279d670e4fd"
class MandiData:

    def __init__(self, api_key, date = None):
        self.apiKey = api_key
        self.date = date
        self.baseUrl = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        self.params = {"api-key":  self.apiKey, "limit" : 500, "date":self.date, "format":"json"}
    

    def getData(self):
        response = requests.get(self.baseUrl, self.params)
        response = response.json()
        return response

pprint(MandiData(apikey).getData())