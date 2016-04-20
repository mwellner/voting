FROM        ubuntu:15.10
MAINTAINER  Mathias Wellner <mathias@mwellner.de>

RUN         apt-get update && apt-get install -y python-flask python-psycopg2 

RUN         mkdir -p /usr/src/app
WORKDIR     /usr/src/app

COPY        . /usr/src/app

EXPOSE      5000

CMD         ["python", "result.py"]
