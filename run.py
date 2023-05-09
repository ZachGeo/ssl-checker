import subprocess, requests, sys, os

from datetime import date, datetime

today = date.today()
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')

output = subprocess.run(["bash", "/tmp/ssl-checker/ssl_expiration.sh", "/tmp/ssl-checker/input.csv"], stdout=subprocess.PIPE, text=True)

def ssl_remaining_days(remaining_days, servername, slack_text=''):
    if 7 <= remaining_days < 364:
        slack_text = "Certificate for {} is expiring in {} days.".format(servername, remaining_days)
    elif 0 <= remaining_days < 7:
        slack_text = "Certificate for {} is expiring in {} days!".format(servername, remaining_days)
    elif remaining_days <= 0:
        slack_text = "Certificate for {} has been expired!!".format(servername)

    return slack_text

def post_message_to_slack(slack_text):
    uri = 'https://slack.com/api/chat.postMessage'
    return requests.post(uri, {
            'token': SLACK_TOKEN,
            'channel': SLACK_CHANNEL,
            'text': slack_text
        }).json()

for item in range(len(output.stdout.splitlines())):
    servername = output.stdout.splitlines()[item].split(", ")[0]
    expiration_date = datetime.strptime(output.stdout.splitlines()[item].split(", ")[1], "%Y-%m-%d").date()
    remaining_days = abs((today - expiration_date).days)
    slack_text = ssl_remaining_days(remaining_days, servername)

    log = post_message_to_slack(slack_text)
    print(log)
