# chalice new-project lambda_coins
# cd lambda_coins
# nano app.py

pip install requests -t ./vendor/
echo request > requirements.txt

pip install slackbot -t ./vendor/
echo slackbot >> requirements.txt

# chalice local
# chalice deploy
