FROM postgres:9.4

# create directory in container
RUN mkdir -p docker-entrypoint-initdb.d

# copy table creation scripts
COPY create-voting-db.sql /docker-entrypoint-initdb.d/
