# Practice Session
# Exercise 1
# Import sqlite3
# Import display from visualizer.py
# Connect to the simplefolks database and get a cursor

import sqlite3
from visualizer import display

# Connect to the simplefolks.sqlite database
conn = sqlite3.connect("simplefolks.sqlite")
cursor = conn.cursor()

# Exercise 2
# Create a SELECT query to the pets table to retrieve
# 5 pets beginning at rowid 11
# Execute the query, call the display() function, run the file, and open tables.html with Live Server

# Query to retrieve 5 pets starting from rowid 11
query = "SELECT * FROM pets LIMIT 5 OFFSET 10"
cursor.execute(query)
display(cursor)

# Exercise 3
# Create a SELECT query to the people table to retrieve
# just the name and age columns
# Call the display function to show results on tables.html
# Edit the SELECT query to show youngest to oldest
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve name and age from the people table
query = "SELECT name, age FROM people"
cursor.execute(query)
display(cursor)
# Query to retrieve name and age, ordered from youngest to oldest
query = "SELECT name, age FROM people ORDER BY age ASC"
cursor.execute(query)
display(cursor)

# Exercise 4
# Create a SELECT query to the people table to retrieve the
# rowid and name columns, and
# add a clause to put the names in reverse alphabetical order
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve rowid and name, ordered in reverse alphabetical order
query = "SELECT rowid, name FROM people ORDER BY name DESC"
cursor.execute(query)
display(cursor)

# Exercise 5
# Create a SELECT query to retrieve all the cats in the pets table
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve all cats from the pets table
query = 'SELECT * FROM pets WHERE type = "Cat"'
cursor.execute(query)
display(cursor)

# Exercise 6
# Create a SELECT query to retrieve the first and last name of
# every senator in the politicians table
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve first and last names of all senators from the politicians table
query = "SELECT first_name, last_name FROM politicians WHERE position = 'Senator'"
cursor.execute(query)
display(cursor)
