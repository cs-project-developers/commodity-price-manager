import requests
from pprint import pprint

apikey = "579b464db66ec23bdd000001d18f8b46035d4f0373893279d670e4fd"
baseUrl = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
params = {"api-key":  apiKey, "limit" : 500,"format":"json"}
    
def getData():
    response = requests.get(baseUrl,params)
    response = response.json()
    return response

pprint(getData())
