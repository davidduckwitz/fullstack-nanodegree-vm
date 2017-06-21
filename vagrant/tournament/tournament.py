#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
# This content id produced by David Duckwitz
# (c) 2017 by David Duckwitz (Project for Nanodegree - Udacity - FULLStack Webdeveloper)
# You can take this for getting ideas, but please create your own script

import time
import psycopg2
from random import shuffle

def connect():
    #Connect to Database
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    #Connect to Database
    db = connect()
    c = db.cursor()
    #Delete from Database
    c.execute("DELETE FROM matches")
    db.commit()
    #Close DB Connection
    db.close()

def deletePlayers():
    deleteTournamentPlayers()
    #Connect to Database
    db = connect()
    c = db.cursor()
    #Delete from Database
    c.execute("DELETE FROM players;")
    db.commit()
    #Close DB Connection
    db.close()

def countPlayers():
    #Connect to Database
    db = connect()
    c = db.cursor()
    #run Database Query
    c.execute("SELECT count(*) from players;")
    rows = c.fetchall()
    #Close DB Connection
    db.close()

    return int(rows[0][0])

def registerPlayer(name, tournamentID = 1):
    #Connect to Database
    db = connect()
    c = db.cursor()
    #run Database Query
    c.execute("INSERT INTO players VALUES (DEFAULT, %s);", (name, ))
    db.commit()
    #Close DB Connection
    db.close()

def playerStandings(tournamentID = 1):
    #Connect to Database
    db = connect()
    c = db.cursor()
    #run Database Query
    c.execute("SELECT * FROM player_stats WHERE TournamentID = %s" , (tournamentID, ))
    rows = c.fetchall()
    #Close DB Connection
    db.close()

    l = list()

    for row in rows:
        l.append((int(row[0]), row[1], int(row[2]), int(row[3])))

    return l

def reportMatch(firstPlayer, secondPlayer, winner, tournamentID = 1):
    #Connect to Database
    db = connect()
    c = db.cursor()
    #run Database Query
    c.execute("INSERT INTO matches VALUES (DEFAULT, %s, %s, %s, %s);", (tournamentID, firstPlayer, secondPlayer, winner))
    db.commit()
    #Close DB Connection
    db.close()

def swissPairings(tournamentID = 1):
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM player_stats ORDER BY wins DESC;")
    rows = c.fetchall()
    db.close()
    i=0
    pairs = []
    while i < len(rows):
        playerOneId = rows[i][0]
        playerOneName = rows[i][1]
        playerTwoId = rows[i+1][0]
        playerTwoName = rows[i+1][1]
        pairs.append((playerOneId,playerOneName,playerTwoId,playerTwoName))
        i=i+2

	return pairs
	