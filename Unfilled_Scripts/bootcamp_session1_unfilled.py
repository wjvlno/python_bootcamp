# Markdown Cell
# Importing Modules and Functions

# Code Cell
# Importing Modules and Functions - Tutorial

# import numpy module. We'll call it as 'np' from here forward
import numpy as np
# import specific functions/classes from 'math' module
from math import sqrt, pi

# Using the imported package and functions

# build a numpy array
array = np.array([2, 6, 8])

# sum elements in the array
array_sum = np.sum(array)

# perform calculation with a loaded function from 'math' (sqrt)
root_value = sqrt(array_sum)

# printing values to the screen
print("Square root of 16 is:", sqrt(16))
print(f"Square root of {array_sum} is: {sqrt(array_sum)}") # using f strings

# using 'pi' from 'math' module
print("Value of pi is:", pi)
print(f"Value of pi is: {pi}") # using f strings


# Code Cell
# Importing Modules and Functions - Task #1
# Working with a new module

# 1. Import the 'datetime' module
import ...

# 2. Use 'dir(module_name)' to check what we can do with the 'datetime' module
dir(...)

# 3. import the 'date' class from the 'datetime' module
from ... import ...

# 4. check methods in the 'date' class using dir()
...

# 5. Make a variable, 'current_date', using 'today' method in 'date' class
# Note: adding parentheses - 'today()' - calls this method and returns an object
# that we can set as a variable
current_date = ...
print(f"Today's date is {current_date}")

# 6. Use dir() to see the attributes in our new variable, current_date
...

#7.  print some attributes (e.g., year, month, & day)
print ("- Year: ", end = "")
print (...)

print ("- Month: ", end = "")
print (...)

print ("- Day: ", end = "")
print (...)


# Code Cell
# Importing Modules and Functions - Task #2

# 1. import the 'datetime' class from the 'datetime' module
from ... import ...

# 2. check methods in the 'datetime' class
dir(...)

# 3. use the 'now()' method from the 'datetime' class
current_datetime = ...

# 4. use the 'time()' method to get JUST the time (ignore the date)
current_time = ...

# 5. pull the hour and minute attributes and make new variables
current_hour = ...
current_minute = ...

# 6. print the current hour and minute timestamp
print(f"It is currently {...}:{current_minute:02d}") # zero-pad minutes
print(f"- Hour: {...}")
print(f"- Minute: {...}")


# Code Cell
# Bonus: accounting for timezones

from datetime import datetime
import pytz

# use now() method
current_datetime = datetime.now(tz=pytz.timezone("America/New_York"))

# use time() method
current_time = current_datetime.time()

# pull attributes
current_hour = current_time.hour
am_pm = "AM"
if current_hour > 12:
  current_hour =-12 # subtract 12 for non-military time
  am_pm = "PM"
current_minute = current_time.minute

# print current time
print(f"Here, it's {current_hour}:{current_minute:02d} {am_pm}") # zero-pad minutes
print(f"- Hour: {current_hour}")
print(f"- Minute: {current_minute}")

# Code Cell
# Bonus: making a function that tells the time

def whats_the_time(tz): # takes one input (timezone)
  current_time = datetime.now(tz=pytz.timezone(tz)).time()

  current_hour = current_time.hour
  if current_hour > 12:
    current_hour =-12 # subtract 12 for non-military time

  current_minute = current_time.minute

  location_from_tz = tz.split('/',1)[1].replace('_', ' ')

  if current_minute < 30:
    print(f"It's {current_minute} minutes past {current_hour} o'clock in {location_from_tz}")
  elif current_minute > 30:
    print(f"It's {60 - current_minute} minutes to {current_hour} o'clock in {location_from_tz}")
  elif current_minute == 30:
    print(f"It's half past {current_hour} o'clock in {location_from_tz}")

# Call the function with "America/New_York" timezone
whats_the_time("America/New_York")

# Markdown Cell
# Basic Data Types

# Code Cell
# Basic Data Types - Tutorial
integer = 10
floating = 10.5
string = "Python Rulez"
boolean = True

# Lists: Ordered, mutable collections of items
# use brackets [x1, x2, ...]
my_list = [1, 2, 3, 4]
print("List:", my_list)
print()

# Tuples: Ordered, immutable collections of items
# use parentheses (x1, x2, ...)
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)
print()

# Dictionaries: Collections of key-value pairs
# use curly braces {"key1": value1, "key2": value2, ...}
my_dict = {"last_name": "Jergis",
           "first_name": "Merv",
           "age": 75}
print("Dictionary:", my_dict)
print(my_dict.keys())

# Code Cell
# Basic Data Types - Task

# 1. Create a list of your favorite movies

fav_movies = ...

# 2. Create a list of the years they were made
movie_years = ...

# 3. Make a dictionary from your lists with keys: Title, Year
movie_dict = ...
print(movie_dict)

# Markdown Cell
# Indexing and Slicing

# Code Cell
# Indexing and Slicing - Tutorial #1

# Make a list of integers
my_list = [10, 20, 30, 40, 50]
print(my_list)
print()

# Check number of elements in the list
print("List length:",len(my_list))
print()

# Indexing returns an element
first_element = my_list[0]
last_element = my_list[-1]

# Slicing returns a 'sublist'
# When slicing, the start is always included, and the end is always excluded
first_four = my_list[0:4]
print("First four elements:", first_four)
print()

# Other ways to slice
print("First two elements:", my_list[:2]) # pull the first two elements
print()

print("Elements after fourth:", my_list[4:]) # pull elements after position 4
print()

# Using a 'step'; e.g., skipping every other number
# Format: 'start:stop:stepSize'
print("Skipping every other element:", my_list[0:len(my_list):2]) # here, 2 is the step size

# Code Cell
# Indexing and Slicing - Task #1

# 1. Index 40 from 'my_list'
...

# 2. Slice the values 20 and 30 from 'my_list'
...

# Code Cell
# Indexing and Slicing - Tutorial #2

# Numpy has an array class too
# We can index numpy arrays the same way as above

# Make a 1-Dimensional array of 10 random numbers between 0 and 100
new_array = np.random.rand(10)*100
print(new_array)

# Slice the first 5 values
print(new_array[0:5])

# Index the 5th value
print(new_array[4])


# Code Cell
# Conditional indexing and slicing - Tutorial

# pull values below 42 (a few ways to do this)

# First
nums_below_list1 = new_array[new_array < 42]
print(nums_below_list1)

# Second
nums_below_list2 = []
for num in new_array:
  if num < 42:
    nums_below_list2.append(num)
print(nums_below_list2)

# Third
nums_below_list3 = [num for num in new_array if num < 42]
print(nums_below_list3)

# More on these last two methods to come...

# Code Cell
# Indexing and Slicing - Task

# Here's what string slicing looks like:
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# Note: with strings, indices fall between characters

# Start with a list of strings
string_list = ["Python", "is", "a", "snake", "and", "a", "language"]

# Index the first string
first_string = ...

# Slice the first 3 characters of the first string
first_three_char = ...

print(first_three_char)

# Markdown Cell
# Working with DataFrames

# Code Cell
# Working with DataFrames - Tutorial #1

import pandas as pd

# Building a DataFrame

# We'll start by making a dictionary
data = {
    "Make": ["Volkswagen", "Fiat", "Ferrari", "Ferrari"],
    "Model": ["Jetta", "Panda", "250 GTO", "California"],
    "Year": [2024, 1987, 1963, 2021],
    "Price": [24875.00, 8200.00, 70000000.00, 255995.00],
    "MPG": [30, 8.9, 13.8, 25]
}

# Then convert that dictionary to a DataFrame
df = pd.DataFrame(data)

print(df)

# Code Cell
# Working with DataFrames - Tutorial #2

# Sorting the DataFrame

# Sorting by the 'Price' column in ascending order
df_sorted_asc = df.sort_values(by="Price")
print("\nDataFrame sorted by Price (ascending):")
print(df_sorted_asc)

# Sorting in descending order
df_sorted_desc = df.sort_values(by="Price", ascending=False)
print("\nDataFrame sorted by Price (descending):")
print(df_sorted_desc)

# Sorting by multiple columns
df_sorted_twoCol = df.sort_values(by=["Make", "Price"], ascending=[True, False])
print("\nDataFrame sorted by Make (ascending) and Price (descending):")
print(df_sorted_twoCol)

# Code Cell
# Working with DataFrames - Task

# Create a DataFrame with columns `Product`, `Price`, and `Quantity` with at
# least three rows of data

# 1. Make your data dictionary first
data = {
    ...
}

# 2. Create the DataFrame
df = ...

# Print the DataFrame
print(df)

# Code Cell
# Reading and Writing CSVs - Tutorial #1

# We'll import the 'os' module to help write file paths for saving/reading
import os

# set your file destination
file_destination = "C:/Users/wvillano/Downloads" # replace with your own path

# name your CSV
file_destination = "bootcamp_example.csv"

# Use 'os' to create the full filepath
full_path = os.path.join(file_destination, filename)
print(full_path)

# write your df to a csv file
df.to_csv(full_path)

# read in the csv you just saved under a new variable name
df_copy = pd.read_csv(full_path)
print(df_copy)


# Code Cell
# Indexing and Modifying DataFrames - Tutorial

my_df = pd.DataFrame({
    "Product": ["Dell XPS 13", "Double Espresso", "White T-shirt"],
    "Price": [1595.00, 3.15, 15.95],
    "Quantity": [1, 465000, 42]
})

# Print the original DataFrame
print("Original DataFrame:")
print(my_df)
print()

# Accessing a column and modifying its elements
# Increase the price of all products by 10%
my_df["Price"] = my_df["Price"] * 1.20
print("Uh oh lol! Inflation! Prices are up 20%:")
print(my_df)
print()

# Use '.loc' to access/modify multiple elements
# IMPORTANT: Unlike list slicing, .loc is END INCLUSIVE.
# Set the quantity of the first two elements to 0
new_quantity = 0
my_df.loc[0:1, "Quantity"] = new_quantity
# this makes a string that combines the two product names
selected_products = " and ".join(my_df.loc[0:1, "Product"])
print(f"Changing the quantity of {selected_products} to {new_quantity}:")
print(my_df)
print()

# Accessing a specific element using row and column indices
# Change the price of the second element to 50
new_price = 50
my_df.at[2, "Price"] = new_price
selected_products = my_df.at[2, 'Product']
# Adding ':.2f' to the 'new_price' variable tells python to print 2 decimals
print(f"Changing the price of {selected_products} to ${new_price:.2f}:")
print(my_df)


