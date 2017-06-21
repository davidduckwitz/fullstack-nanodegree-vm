-- Table definitions for the Udacity tournament project.
-- Drop Tables and Views 
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS tournaments;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS player_stats;
DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS count;

CREATE TABLE players (
	ID serial PRIMARY KEY,
	Name varchar(255) NOT NULL
);

-- CREATE TABLE tournament_players ( 
--	TournamentID int REFERENCES tournaments (ID) NOT NULL,
--	PlayerID int REFERENCES players (ID) NOT NULL,
--	HadBye int NOT NULL DEFAULT 0,
--	PRIMARY KEY (TournamentID, PlayerID)
--);

-- Create Table tournaments
CREATE TABLE tournaments (
	ID serial PRIMARY KEY,
	Name varchar(255) NOT NULL
	player int references players(id),
	enemy int references players(id),
	result int
);

-- Create Table matches
CREATE TABLE matches (
	ID serial PRIMARY KEY,
	TournamentID int REFERENCES tournaments (ID) NOT NULL,
	FirstPlayer int REFERENCES players (ID) NOT NULL,
	SecondPlayer int REFERENCES players (ID), 
	Winner int REFERENCES players (ID)
);

-- Create Table player_stats
CREATE TABLE player_stats (
	ID serial PRIMARY KEY,
	player int REFERENCES players (ID) NOT NULL,
	name varchar(255) NOT NULL,
	wins int,
	loses int,
	matches int,
	TournamentID int REFERENCES tournaments (ID) NOT NULL
);

-- Standings View shows number of wins and matches for each Player
CREATE VIEW standings AS 
	SELECT players.id, players.name,Wins.n as wins,Count.n as matches 
	FROM players,Count,Wins
WHERE players.id = Wins.id and Wins.id = Count.id;

-- Count View shows number of matches for each Player
CREATE VIEW Count AS
	SELECT players.id, Count(matches.enemy) AS n 
	FROM players
	LEFT JOIN matches
	ON players.id = matches.player
GROUP BY players.id;

