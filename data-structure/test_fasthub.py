import requests
import json
from datetime import datetime,date

def get_total(substr):
    response = requests.get("https://jsonmock.hackerrank.com/api/moviesdata/search/?Title={}".format(substr))
    total = json.loads(response.text)
    print(total['total'])
    
    
def get_page(a,b,c):
    response = requests.get("https://jsonmock.hackerrank.com/api/iot_devices/search?status={}".format(a))
    result = json.loads(response.text)
    
    device = result['data']
    count = 0
    for item in device:
        # if item['operatingParams']['rootThreshold'] > b:
        #     count +=1
        my_date = datetime.strptime(c,'%m/%y')
        print(my_date)
        
        
    
get_page('STOPPED',45,'3-2019')