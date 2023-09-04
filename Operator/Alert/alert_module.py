import slackweb
def alert_mo(Url,message):
    slack = slackweb.Slack(url=Url)
    slack.notify(text = message)
    
