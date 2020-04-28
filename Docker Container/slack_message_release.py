import slack
import os
import urllib.parse
from datetime import date

slack_token = os.environ["SLACK_API_TOKEN"]
client = slack.WebClient(token=slack_token)
version = os.environ["RELEASE_VERSION"]
channel = os.environ["SLACK_CHANNEL"]
release_or_hotfix = os.environ["RELEASE_OR_HOTFIX"]
release_notes = os.environ["RELEASE_NOTES"]
url = os.getenv('CI_TRIGGER_JOB_URL', "https://jenkins.io")
should_display_approve = os.getenv("DISPLAY_APPROVE_BUTTON", "false")
should_display_approve = should_display_approve.lower() == "true"


def slack_message(text):
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": release_or_hotfix.title() + " notes for version " + version
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Type:*\n" + release_or_hotfix.title()
                },
                {
                    "type": "mrkdwn",
                    "text": "*When:*\nSubmitted " + date.today().strftime("%B %d, %Y")
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
            "type": "divider"
        }
    ]

    if should_display_approve:
        slack_buttons = {
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
                    # "url": "https://ci.feverup.com/view/iOS/job/Approve%20Release/buildWithParameters?token=" + ci_token + "&release_or_hotfix=" + release_or_hotfix + "&release_version=" + version + "&release_notes=\"" + urllib.parse.quote(text) + "\""
                    "url": "url"
                }
                # {
                #     "type": "button",
                #     "text": {
                #         "type": "plain_text",
                #         "emoji": True,
                #         "text": "Deny"
                #     },
                #     "style": "danger",
                #     "value": "click_me_123"
                # }
            ]
        }
        blocks.append(slack_buttons)

	response = client.chat_postMessage(
    channel=channel,
    text=text,
    username="Jenkins",
    icon_url="https://jenkins.io/images/logos/general/general.png",
	blocks=blocks
    )

	assert response["ok"]
