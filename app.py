# Exercise 1: Get connected and have a look at the food table
# Import sqlite3
# Import the display function from visualizer.py
# Connect to the food.db database
# Get a cursor so you can write queries to the database
# Use the execute function to run a SELECT * query on food.db
# Show the output of your select query on a webpage by using the display() function
# In the terminal, run this Python file
# Open tables.html with Live Server

import sqlite3
from visualizer import display

# Connect to the database
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

# Execute SELECT * query to retrieve all records
cursor.execute("SELECT * FROM food")
display(cursor)

# Exercise 2
# Write a SELECT query limiting output to 5 rows
# Send the query to the db using execute
# Call the display() function and pass it the output of execute
# In the terminal, run this Python file
# Open tables.html with Live Server
# Edit the SELECT query so that the 5 rows retrieved start at row 500
# In the terminal, run this Python file
# Check output on tables.html

# Query to retrieve 5 rows
cursor.execute("SELECT * FROM food LIMIT 5")
display(cursor)

# Query to retrieve 5 rows starting at row 500
cursor.execute("SELECT * FROM food LIMIT 5 OFFSET 500")
display(cursor)

# Exercise 3
# Part 1
# Write a SELECT query using ORDER BY with the Name column,
# limit the results to 10
# Execute the query, call the display() function, run the file,
# and check output on tables.html
# Part 2
# Edit the SELECT query you just made using ORDER BY with the rowid column, specify DESC and limit the results to 10
# Check the output
# *In SQLite3, the index column, or Primary Key, is called rowid

# Part 1: Query ordered by Name limited to 10
cursor.execute("SELECT * FROM food ORDER BY Name LIMIT 10")
display(cursor)

# Part 2: Query ordered by rowid in descending order limited to 10
cursor.execute("SELECT * FROM food ORDER BY rowid DESC LIMIT 10")
display(cursor)

# Exercise 4
# Part 1
# Create a SELECT query to retrieve the food names
# * Make sure to spell the column heading exactly as you've seen it in previous results
# Execute the query, call the display() function, run the file,
# and check output on tables.html
# Part 2
# Edit the SELECT query to retrieve all the food names and species, limit results to 20
# Check the output

# Part 1: Query to retrieve food names
cursor.execute("SELECT Name FROM food")
display(cursor)

# Part 2: Query to retrieve food names and species, limited to 20
cursor.execute("SELECT Name, Species FROM food LIMIT 20")
display(cursor)

# Exercise 5: Get the name and species of all of the nuts
# Create a SELECT query to retrieve the food names and species of nuts
# Use a WHERE clause to specify nuts from the Group column
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve names and species of nuts
cursor.execute("SELECT Name, Species FROM food WHERE \"Group\" = \"Nuts\"")
display(cursor)

# Exercise 6: Get all of the onions and herbs
# Create a new SELECT query to retrieve all of the herbs and onions
# Use the Subgroup column to filter
# Execute the query, call the display() function, run the file,
# and check output on tables.html

# Query to retrieve all herbs and onions
cursor.execute("SELECT * FROM food WHERE Subgroup = \"Herbs\" OR Subgroup = \"Onions\"")
display(cursor)
