from urllib.request import urlopen
import json
from datetime import datetime 

apiEur = "https://api.coindesk.com/v1/bpi/currentprice.json"
responseApiEur = urlopen(apiEur)
apiDataEur = json.loads(responseApiEur.read())

apiCzk = "https://api.coindesk.com/v1/bpi/currentprice/CZK.json"
responceApiCzk = urlopen(apiCzk)
apiDataCzk = json.loads(responceApiCzk.read())

serverTimeEur = apiDataEur["time"]["updated"]
timeNowEur = datetime.now()
formatTimeEur = timeNowEur.strftime("%b %d, %Y %H:%M:%S")
eurCost = apiDataEur["bpi"]["EUR"]["rate_float"]

serverTimeCzk = apiDataCzk["time"]["updated"]
timeNowCzk = datetime.now()
formatTimeCzk = timeNowCzk.strftime("%b %d, %Y %H:%M:%S")
CzkCost = apiDataCzk["bpi"]["CZK"]["rate_float"]

data = {'1 BitCoin':{'EUR':{'server time': str(serverTimeEur), 'request time': str(formatTimeEur), 'price': str(eurCost)}, 
                     'CZK':{'server time': str(serverTimeCzk), 'request time': str(formatTimeCzk), 'price': str(CzkCost)}}}

if __name__ == '__main__':
    print(data)