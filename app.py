import json
import requests
import slackbot
import slackweb
from chalice import Chalice, Cron
#from urlparse import parse_qsl

app = Chalice(app_name='lambda_coins')
app.debug = True

API_BITFLYER = "https://api.bitflyer.jp/v1/ticker?product_code=BTC_JPY"
API_ZAIF = "https://api.zaif.jp/api/1/ticker/btc_jpy"
API_COINCHECK = "https://coincheck.com/api/ticker"

WEBHOOK_URL = "https://hooks.slack.com/services/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"
slack = slackweb.Slack(url=WEBHOOK_URL)

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

#Cron(minutes, hours, day_of_month, month, day_of_week, year)
#@app.schedule(Cron('1/2', '*', '*', '*', '?', '*'))
@app.schedule('rate(6 hours)')
def notify_btc_jpy(event):
    bf = requests.get(API_BITFLYER).json()["ltp"]
    zaif = requests.get(API_ZAIF).json()["last"]
    cc = requests.get(API_COINCHECK).json()["last"]

    text = f"bitflyer: {bf}, zaif: {zaif}, coincheck: {cc}"
    print(text)
    slack.notify(text=text)
