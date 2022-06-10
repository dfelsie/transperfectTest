import requests
import json


if __name__=='__main__':
    URL='https://data.police.uk/api/forces'

    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    for datapoint in data:
        if not 'id' in datapoint:
            continue
        #print(datapoint['id'])
        seniorOfficerUrl = 'https://data.police.uk/api/forces/' + datapoint['id'] + '/people'
        seniorRequest = requests.get(url = seniorOfficerUrl)
        if seniorRequest.status_code != 200 or not seniorRequest.json():
            continue
        print(seniorRequest.json())
    #print(data)