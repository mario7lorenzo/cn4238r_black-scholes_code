import datetime as dt
import requests
import pandas as pd
import json
from datetime import timezone

def main():
	tickerCode = 'TSLA'
	url = "https://yfapi.net/v7/finance/options/" + tickerCode
	day = 5
	month = 11
	year = 2021
	maturityDatetime = dt.datetime(year,month,day)
	maturityDatetime = maturityDatetime.replace(tzinfo=timezone.utc)
	maturityUnixTimestamp = int(dt.datetime.timestamp(maturityDatetime))

	with open("api_key.txt") as f:
		api_key = f.readline()
	f.close()

	querystring = {"date": maturityUnixTimestamp}
	headers = {
	    'x-api-key': api_key
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)

	jsonResponse = json.loads(response.text)
	calls = jsonResponse["optionChain"]["result"][0]["options"][0]["calls"]
	puts = jsonResponse["optionChain"]["result"][0]["options"][0]["puts"]

	callsdf = pd.read_json(json.dumps(calls))
	putsdf = pd.read_json(json.dumps(puts))
	
	callsdf.to_csv(tickerCode+"-"+maturityDatetime.strftime("%Y%m%d")+"-calls.csv")
	putsdf.to_csv(tickerCode+"-"+maturityDatetime.strftime("%Y%m%d")+"-puts.csv")
	return

if __name__ == '__main__':
	main()