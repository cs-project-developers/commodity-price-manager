import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from datetime import date 
from cachetools import cached, TTLCache

cache_api_data = TTLCache(maxsize=100, ttl=86400)

today_ = str(date.today())
month_ = today_.split("-")[1]
date_ = today_.split("-")[2]
year_ =today_.split("-")[0]
today_ = date_+"/"+month_+"/"+year_

apikey = "579b464db66ec23bdd00000166242144497346c259a60df03f8c7315"
disable_warnings(InsecureRequestWarning)

@cached(cache_api_data)
def getRawData(apikey=apikey):
    
        baseUrl = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        params = {"api-key":  apikey, "limit" : 1000,"format":"json"}
        response = requests.get(baseUrl,params,verify=False)
        response = response.json()
        return response
@cached(cache_api_data)
def mined_data():
        raw_data = getRawData()
        recorded_data = raw_data.get("records")
        return recorded_data
@cached(cache_api_data)    
def commodity_name_list():
        coms_data = []
        datas = mined_data()
        for data in datas:
            result = data['commodity']
            if result not in coms_data:
                coms_data.append(result)
        return coms_data



#################test case statement
