## DESCRIPTION

The main script to use when running is `send_release_notes.sh`. This script will:
- Fetch all the jira issues contained on "RELEASE_NOTES" environment variable.
- Send an slack message to the defined channel if the release notes are not empty.

## USAGE

You can use a list of commands like the following to build and execute the scripts:
```bash
docker build -t release-notes "https://github.com/Feverup/docker-jira-slack.git#develop:Docker Container"
docker run -dt --env-file ./env.list --name release-notes release-notes
docker container exec release-notes sh send_release_notes.sh
docker stop release-notes
docker container rm release-notes
```

Required environment variables:

- **RELEASE_NOTES**: A list of jira issues id. E.g ("IOS-1288 IOS-1289")
- **RELEASE_VERSION**: Version name.
- **SLACK_CHANNEL**: Channel that messages will be sent to.
- **SLACK_API_TOKEN**: Slack API Token
- **JIRA_API_KEY**: JIRA API key
- **JIRA_API_EMAIL**: JIRA API email