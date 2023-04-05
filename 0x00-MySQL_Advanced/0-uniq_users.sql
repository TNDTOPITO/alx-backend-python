-- Creates user table on any data base

CREATE TABLE IF NOT EXISTS USER (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)
