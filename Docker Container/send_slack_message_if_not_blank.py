import argparse, sys
from slack_message_release import slack_message

parser=argparse.ArgumentParser()

parser.add_argument('release_notes', help='Specify the release notes')
args=parser.parse_args()
RELEASE_NOTES=args.release_notes

def is_not_blank(s):
    return bool(s and s.strip())

if is_not_blank(RELEASE_NOTES):
	slack_message(RELEASE_NOTES)