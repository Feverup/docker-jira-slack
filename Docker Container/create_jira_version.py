from main import *
import argparse
from datetime import datetime

parser=argparse.ArgumentParser()

parser.add_argument('version', help='Specify the current release version')
parser.add_argument('issues_id', help='Array of JIRA issues id')

args=parser.parse_args()
release_version = args.version
issues_id = args.issues_id

release_notes = ''

released = True
current_time = datetime.now().strftime('%Y-%m-%d')
try:
	jira.create_version(name=release_version,project=project_key,releaseDate=current_time,startDate=current_time,released=released)
except JIRAError as e:
	print("It looks like the version already exists")

for key in issues_id.split():
	issue = jira.issue(key)
	# issue.update(fields={'fixVersions': [{ 'name' : '6.31.0' }]})
	print("Fix version for " + issue.key + " updated to " + release_version)

print(release_notes)