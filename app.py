import json
import requests
import slackbot
from chalice import Chalice
#from urlparse import parse_qsl

app = Chalice(app_name='lambda_coins')
app.debug = True

API_BITFLYER = "https://api.bitflyer.jp/v1/ticker?product_code=BTC_JPY"
API_ZAIF = "https://api.zaif.jp/api/1/ticker/btc_jpy"
API_COINCHECK = "https://coincheck.com/api/ticker"

@app.route('/bitcoin', methods=['POST'],
           content_types=['application/json',
                          'application/x-www-form-urlencoded'])
def bitcoin():
    body = app.current_request.raw_body
    #parsed = dict(parse_qsl(body))
    
    bf = requests.get(API_BITFLYER).json()["ltp"]
    zaif = requests.get(API_ZAIF).json()["last"]
    cc = requests.get(API_COINCHECK).json()["last"]
    return {"text": json.dumps(
        {"bitflyer": bf, "zaif": zaif, "coincheck": cc})}
