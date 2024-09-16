import sqlite3
from usr import Usr
from os.path import isfile

name = "data.db"

def create():

    # Return early if database is already set up
    if isfile(name):
        return
    
    accounts = [Usr("regular", "password").data, 
                Usr("admin", "admin", True).data]

    # Create database files
    con = sqlite3.connect(name)
    cur = con.cursor()

    # Create table for accounts and load them
    cur.execute("CREATE TABLE usrs (usr PRIMARY KEY, pw NOT NULL, isadmin NOT NULL)")
    cur.executemany("INSERT INTO usrs VALUES (?, ?, ?)", accounts)
    con.commit()

    # Create table to store tickets
    cur.execute("CREATE TABLE tickets (ticketno PRIMARY KEY, usr NOT NULL, subject NOT NULL, status NOT NULL, priority NOT NULL, dt NOT NULL)")
    con.commit()

    # Add placeholder data 
    tickets = [ (1,  "John Smith",   "Computer not working",       "Pending",  "Low",  "2024-09-15 12:22"),
                (2,  "Jane Doe",     "cannot send any e-mails",    "Assigned", "Low",  "2024-09-16 14:00"),
                (3,  "Mary",         "PC encrypted by ransomware", "Assigned", "High", "2024-09-13 16:55"),
                (4,  "Sam Jones",    "Lost my keyboard",           "Resolved", "Low",  "2012-12-21 12:00"),
                (5,  "Jeremy Fox",   "Computer Slowness",          "Resolved", "Low",  "2024-09-09 09:09"),
                (6,  "Terry Jobs",   "Require new laptop",         "Pending,", "Low",  "2024-09-15 13:30"),
                (7,  "Muhammad Li",  "Servers are down",           "Pending",  "High", "2024-10-01 13:37"),
                (8,  "J.M.",         "New Starter Onboarding",     "Assigned", "Low",  "2024-09-10 21:00"),
                (9,  "Jerry Allen",  "monitor is cracked!",        "Resolved", "Low",  "2024-09-13 17:38"),
                (10, "Sarah McGill", "Blue-screen when booting",   "Resolved", "High", "2024-07-19 04:10")]
    
    cur.executemany("INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?)", tickets)
    con.commit()

    con.close()

def table():

    if not isfile(name):
        create()

    con = sqlite3.connect(name)
    cur = con.cursor()   

    res = cur.execute("SELECT * FROM tickets").fetchall()
    con.close()

    return res