-- Creates a db and hbtn_0d_usa a table states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name varchar(256) NOT NULL,
	PRIMARY KEY (id)
);
