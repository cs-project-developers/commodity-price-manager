import requests
from pprint import pprint
from datetime import date 
today_ = str(date.today())
month_ = today_.split("-")[1]
date_ = today_.split("-")[2]
year_ =today_.split("-")[0]
today_ = date_+"/"+month_+"/"+year_
apikey = "579b464db66ec23bdd000001bd1f213b3d5c4a1b44412bd3c21dfae6"

def getRawData(apikey=apikey):
    
        baseUrl = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
        params = {"api-key":  apikey, "limit" : 1000,"format":"json"}
        response = requests.get(baseUrl,params)
        response = response.json()
        return response

def mined_data():
        raw_data = getRawData()
        recorded_data = raw_data.get("records")
        return recorded_data
    
def commodity_name_list():
        coms_data = []
        datas = mined_data()
        for data in datas:
            result = data['commodity']
            if result not in coms_data:
                coms_data.append(result)
        return coms_data


