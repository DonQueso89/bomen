#!/bin/bash
set -e

for db in bomen; do
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE $db;
	CREATE TABLE IF NOT EXISTS bomen (
		id SERIAL PRIMARY KEY,
		nl_naam VARCHAR(128),
		wetenschappelijke_naam VARCHAR(128),
		nummer INT,
		hoogte VARCHAR(50),
		type VARCHAR(50),
		plantjaar INT,
		eigenaar VARCHAR(50),
		beheerder VARCHAR(50),
		categorie VARCHAR(128),
		geslacht_naam VARCHAR(50),
		location geometry(POINT, 4326),
		sdview VARCHAR(20),
		radius INT
		);
EOSQL
done
