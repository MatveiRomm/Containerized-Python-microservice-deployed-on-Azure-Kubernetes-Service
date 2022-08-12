from datetime import datetime 
from requests import get

def showJson():
    # pull data in json format from api
    apiEur = "https://api.coindesk.com/v1/bpi/currentprice.json"
    responseApiEur = get(apiEur)
    apiDataEur = responseApiEur.json()
    
    apiCzk = "https://api.coindesk.com/v1/bpi/currentprice/CZK.json"
    responceApiCzk = get(apiCzk)
    apiDataCzk = responceApiCzk.json()
    
    # parse json to take server's time, client's request time and cost 
    serverTimeEur = apiDataEur["time"]["updated"]
    timeNowEur = datetime.now()
    formatTimeEur = timeNowEur.strftime("%b %d, %Y %H:%M:%S")
    eurCost = apiDataEur["bpi"]["EUR"]["rate_float"]

    serverTimeCzk = apiDataCzk["time"]["updated"]
    timeNowCzk = datetime.now()
    formatTimeCzk = timeNowCzk.strftime("%b %d, %Y %H:%M:%S")
    CzkCost = apiDataCzk["bpi"]["CZK"]["rate_float"]
    
    # build new json output
    data = {'1 BitCoin':{'EUR':{'server time': str(serverTimeEur), 'request time': str(formatTimeEur), 'price': str(eurCost)}, 
                         'CZK':{'server time': str(serverTimeCzk), 'request time': str(formatTimeCzk), 'price': str(CzkCost)}}}
    return data
