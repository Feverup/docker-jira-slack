echo $RELEASE_NOTES
echo $RELEASE_VERSION
echo $SLACK_CHANNEL
python send_slack_message_if_not_blank.py "$(python fetch_keys.py $RELEASE_VERSION "$RELEASE_NOTES")"