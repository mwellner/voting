\set ON_ERROR_STOP on

CREATE USER www;
CREATE DATABASE voting;
GRANT ALL PRIVILEGES ON DATABASE voting TO www;

\connect voting

CREATE TABLE votes (
	id 		     bigserial PRIMARY KEY,
  createdate timestamp DEFAULT 'now',
  changedate timestamp DEFAULT 'now',
  vote       integer
);

ALTER TABLE votes OWNER TO www;

INSERT INTO votes (vote) VALUES (1);
INSERT INTO votes (vote) VALUES (2);
INSERT INTO votes (vote) VALUES (3);
INSERT INTO votes (vote) VALUES (1);
INSERT INTO votes (vote) VALUES (1);
