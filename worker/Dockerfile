FROM 				ubuntu:15.10
MAINTAINER 	mathias wellner <mathias@mwellner.de>

# install nodejs and node package manager
RUN					apt-get update && apt-get install -y nodejs npm postgresql-client redis-tools

# create working directory
RUN         mkdir -p /usr/src/app
WORKDIR     /usr/src/app

# install node dependencies
COPY 				package.json /usr/src/app/
RUN  				npm install --production

# copy rest of files to container
COPY        . /usr/src/app/

# start web app
#CMD         ["npm", "start"]
