from jira import JIRA
import sys

# jira_key = str(sys.argv[1])
jira = JIRA('https://jira.atlassian.com')
jira = JIRA(basic_auth=('francisco.cantero@feverup.com', 'zdBXRYy6EQMHWgrHdPjO03D2'), options = {'server': 'https://feverup.atlassian.net'})
