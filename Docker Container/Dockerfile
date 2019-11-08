FROM python:3

ADD . /

# ARGUMENTS
# ARG release_notes
# ARG product_version
# ENV RELEASE_NOTES=$release_notes
# ENV RELEASE_VERSION=$product_version

RUN pip install jira
RUN pip install slackclient

# Make ssh dir
# RUN mkdir /root/.ssh/

# # Copy over private key, and set permissions
# # Warning! Anyone who gets their hands on this image will be able
# # to retrieve this private key file from the corresponding image layer
# ADD id_rsa /root/.ssh/id_rsa

# # Create known_hosts
# RUN touch /root/.ssh/known_hosts
# # Add bitbuckets key
# RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# RUN git clone --depth=1 $projectUrl
# WORKDIR "/iOS"
# RUN git fetch

# RUN echo $RELEASE_NOTES
# RUN echo $(python send_slack_message_if_not_blank.py "$(python fetch_keys.py $RELEASE_VERSION $RELEASE_NOTES)")
# CMD [ "python", "send_slack_message", "python fetch_keys.py", $RELEASE_VERSION , $RELEASE_NOTES ]