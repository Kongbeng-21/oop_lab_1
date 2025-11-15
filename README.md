# -Lab Overview 

## What is this lab all about?
-This lab focusing on OOP structure and managing related datasets,and using lambda functions fot data manipulation.Demonstrates how to build simple databases-like DB() and operations (filter,aggregate and join)

## Project Structure - 
├── README.md                 # Report the project overview.
├── Cities.csv                # The dataset containing city, country, and temperature data.
|---- data_processing.py	  # Main Python file containing DataLoader, DB and Table classes.

## Design Overview 
### -DataLoader(): Load CSV files and convert into list of dictionaries.
### -Table(): Process data from CSV file.
-filter(condition): return a new table rows that meet the condition.
-aggregate(aggregation_function, aggregation_key): applies a function for example average,min or max on values of given column.
-join(other_table, join_column_name):
return new Table by inner join with another based on a shared column.
### -DB(): Work as a database,holding multiple Table() objects.
-insert(table_object): add table to database
-search(table_name): retrieve a table from the database by its name.

## How to test and run your code
-Typing "python data_processing.py" in terminal or click run botton.
