FROM        ubuntu:15.10
MAINTAINER  Mathias Wellner <mathias@mwellner.de>

RUN         apt-get update && apt-get install -y python-psycopg2 python-redis 

RUN         mkdir -p /usr/src/app
WORKDIR     /usr/src/app

COPY        . /usr/src/app

CMD         ["python", "worker.py"]
