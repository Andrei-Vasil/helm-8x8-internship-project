FROM alpine:3.16.2

# install python
RUN apk update && apk upgrade
RUN apk add python3 && apk add --update py-pip

# add curl
RUN apk add curl

# create a new group and assign an user to it
RUN addgroup -S pythonAppGroup && adduser -S pythonAppUser -G pythonAppGroup

# create the app directory
RUN mkdir -p /home/app
COPY --chown=pythonAppUser:pythonAppGroup ./src/* /home/app/

# switch to python user
USER pythonAppUser
WORKDIR /home/app

# install python dependencies
RUN pip install -r ./requirements.txt

EXPOSE 8080
CMD [ "python3", "main.py" ]
