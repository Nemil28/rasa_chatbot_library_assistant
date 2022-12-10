import requests
import json

def book():
    link = "https://api.lib.harvard.edu/v2/collections?limit=100"
    json_data = requests.get(link).json()
    #print(json_data)

    a = set([])

    for i in range(20):
        a.add(json_data[i]["contactDepartment"])

    d = dict.fromkeys(a, 0)
    #print(d)
    #print(type(d))
        
    return d