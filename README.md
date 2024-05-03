# Analysis45
A data analysis library created with Python

# Documentation
## How to use
First, download analysis45.py. Then put it in your project folder, and in another python file, write `from analysis45 import *`\
These are the classes in it:

## Classes

### CSV
The CSV class works with CSV files (duh), it is basically a simplification of the csv library in python\
`CSV(filename)`

#### init()
initializes the csv file

#### output()
prints out a more elegant version of the csv table

#### row(num)
returns the num'th row of the CSV file

#### column(num)
returns the num'th column of the CSV file

#### primary_row
Shows the first row in the CSV file, all other functions ignore the primary row.

#### table
The actual table

#### filename
The filename

## Functions

#### average(list)
finds the average of all the items in a list
