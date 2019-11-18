#!/bin/sh

createVersion() {
	echo "$(python3 create_jira_version.py $RELEASE_VERSION "${RELEASE_NOTES}")"
}

slackReleaseNotes() {
	release_notes=$(python3 get_release_notes.py "${RELEASE_NOTES}")
	echo "$(python3 send_slack_message_if_not_blank.py "${release_notes}")"
}

while [ "$1" != "" ]; do
    case $1 in
        --create-version )
            action="create-version"
            ;;
        --slack-release-notes ) 
			action="slack-release-notes"
			;;
    esac
    shift
done

case ${action} in
    create-version )
        createVersion
        ;;
    slack-release-notes )
        slackReleaseNotes
        ;;
esac
