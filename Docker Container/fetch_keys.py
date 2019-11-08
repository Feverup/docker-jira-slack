from main import *
import os
import argparse, sys
from slack_message_release import slack_message

parser=argparse.ArgumentParser()

parser.add_argument('version', help='Specify the current release version')
parser.add_argument('issues_id', help='Specify the issues id')

args=parser.parse_args()
release_version = args.version
issues_id = args.issues_id

# Read diff log between latest master and the given branch
# issues_diff_master = 'git log --right-only --cherry-pick --pretty=format:\"%s\" origin/master...origin/develop | \
# 		    grep -E \'^.*[A-Z]{2,4}-[0-9]+.*\' | \
# 		    sed -E \'s/^.*([A-Z]{3,4}-[0-9]+).*$/\\1/\' | \
# 		    sort | uniq'
# issues_id = os.popen(issues_diff_master).read()

release_notes = ''

for key in issues_id.split():
	issue = jira.issue(key)
	release_notes += '<' + issue.permalink() + '|*' + issue.key + '*> (' + issue.fields.issuetype.name + ') ' + issue.fields.summary + '\n'

print(release_notes)