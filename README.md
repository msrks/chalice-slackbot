## slackbot in AWS Lambda

<img src="sample.png" width=400>

#### Dependencies:

```
chalice
requests
slackbot
slackweb
```

#### Features:

[Scheduled Handler](http://chalice.readthedocs.io/en/latest/api.html#Cron)

```
every 6 hours:
  -> notify BTC_JPY to Slack
```

REST API

```
/bitcoin
  POST -> return BTC_JPY  
```

#### Comment:

it is usefle to debug w/ ngrok and outbounding-webhook
