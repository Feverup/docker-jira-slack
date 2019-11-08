import slack
import os

# Set token on an Environment variable
slack_token = os.environ["SLACK_API_TOKEN"]
client = slack.WebClient(token=slack_token)
version = os.environ["RELEASE_VERSION"]
channel = os.environ["SLACK_CHANNEL"]
def slack_message(text):
	response = client.chat_postMessage(
    channel=channel,
    text=text,
    username="Jenkins",
    icon_url="https://jenkins.io/images/logos/general/general.png",
	blocks=[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Release notes for version " + version
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Type:*\nRelease/Hotfix"
				},
				{
					"type": "mrkdwn",
					"text": "*When:*\nSubmitted Aut 10"
				},
				{
					"type": "mrkdwn",
					"text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
				},
				{
					"type": "mrkdwn",
					"text": "*User:*\n@cantero"
				}
			]
		},
		{
			"type": "section",
			"text": {
					"type": "mrkdwn",
					"text": "*Notes:*\n```" + text + "```"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Approve"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"url": "https://ci.feverup.com/view/iOS/job/iOS%20AppStore%20release/build?delay=0sec"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    )
	
	assert response["ok"]