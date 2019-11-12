from jira import JIRA
import sys
import os

jira = JIRA('https://jira.atlassian.com')
jira_api_key = os.environ["JIRA_API_KEY"]
jira_api_email = os.environ["JIRA_API_EMAIL"]
jira = JIRA(basic_auth=(jira_api_email, jira_api_key), options = {'server': 'https://feverup.atlassian.net'})