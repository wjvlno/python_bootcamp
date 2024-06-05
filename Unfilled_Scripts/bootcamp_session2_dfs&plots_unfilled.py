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
################################################################################
# Working with DataFrames - Tutorial #2

# Sorting the DataFrame

# Sorting by the 'Price' column in ascending order
df_sorted_asc = df.sort_values(by="Price")
print("\nDataFrame sorted by Price (ascending):")
print(df_sorted_asc)

# Sorting by multiple columns
df_sorted_twoCol = df.sort_values(by=["Make", "Price"], ascending=[True, False])
print("\nDataFrame sorted by Make (ascending) and Price (descending):")
print(df_sorted_twoCol)

# Sort by 'Price in descending order
df_sorted_desc = ...
print("\nDataFrame sorted by Price (descending):")
print(df_sorted_desc)
################################################################################
# Working with DataFrames - Task

# Create a DataFrame with columns `Product`, `Price`, and `Quantity` with at
# least three rows of data

# 1. Make your data dictionary first
data = ...

# 2. Create the DataFrame
my_df = ...

# Print the DataFrame
print(my_df)
################################################################################
# Reading and Writing CSVs - Tutorial #1

# We'll import the 'os' module to help write file paths for saving/reading
import os

# set your file destination
file_destination = "C:/Users/wvillano/Downloads" # replace with your own path

# name your CSV
filename = "bootcamp_example.csv"

# Use 'os' to create the full filepath
full_path = os.path.join(file_destination, filename)
print(full_path)

# write your df to a csv file
my_df.to_csv(full_path)

# read in the csv you just saved under a new variable name
my_df_copy = pd.read_csv(full_path)
print(my_df_copy)
################################################################################
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

# Accessing a specific element using row and column indices
# Change the price of the second element to 50
new_price = 50
my_df.at[2, "Price"] = new_price
selected_products = my_df.at[2, 'Product']
# Adding ':.2f' to the 'new_price' variable tells python to print 2 decimals
print(f"Changing the price of {selected_products} to ${new_price:.2f}:")
print(my_df)

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
################################################################################
import numpy as np
import pandas as pd

# build df
data = {
    "Make": ["Volkswagen", "Fiat", "Ferrari", "Ferrari"],
    "Model": ["Jetta", "Panda", "250 GTO", "California"],
    "Year": [2024, 1987, 1963, 2021],
    "Price": [24875.00, 8200.00, 70000000.00, 255995.00],
    "MPG": [30, 8.9, 13.8, 25]
}
df = pd.DataFrame(data)

## Inspect df

# view first few rows of df
df.head()

# view last 3 rows of df
df.tail(3)

# view df index (i.e., row names)
df.index

# view df column names
df.columns
################################################################################
## Summary stats
df.describe()
################################################################################
## Make a copy of our df in case we want to revert changes

# this method makes a 'deep' copy
df_backup = df.copy()

# why not just use df_new = df?? Try it out
df_new = ...

# try changing the values in a column...
df_new[...] = ...

print(df_new)
print()
print(df)

# what happened?
################################################################################
# revert df to original

df = df_backup.copy() # use 'copy()' again
print(df)
################################################################################
## DataFrame Assignment

# repeat value across all df rows
df['MPG'] = 35
################################################################################
## Convert DataFrame to different data type / structure
df.to_numpy() # e.g., a NumPy array
df.to_json()

# how can we check other data types that we can convert to with built-in methods?

...
################################################################################
## Extraction/Selection

# Getitem ([])
df['MPG'] # returns a series equivalent to df.MPG

# Slicing rows
df[0:3] # slicing in one dimension will always return rows
################################################################################
## Extraction/Selection

# '.loc' selects by label(s)
df.loc[:, ["Make", "Model"]] # select all rows (:), specific columns

df.loc[1:2, ["Make", "Model"]] # Note: for row slice, both endpoints are included

# Selecting a single row/column returns a scalar value
df.loc[0, "MPG"]
df.at[0, "MPG"] # same result. 'at' can only return single values.
################################################################################
## Extraction/Selection

# .iloc selects by position

# select a row
df.iloc[0] # returns first row of data
df.iloc[0,:] # same result

# select a full column explicitly
df.iloc[:,2]

# pull a slice (rows 2-3, columns 1-2)
df.iloc[1:3,0:2] # Note: '.iloc' slices like NumPy (start included, endpoint excluded)

# pull a single value by position
df.iloc[1, 1]
df.iat[1, 1] # same result
################################################################################
## Extraction/Selection

# Boolean indexing
df[df['Price'] > 50000]
df[df.iloc[:,3] > 50000] # same result

# Pull rows where the Make is Ferrari
...


# multiple boolean conditions
df[(df['Make'] == "Ferrari") | (df['Make'] == "Fiat")] # Make is Ferrari OR ('|') Fiat

# Pull rows where the Make is Ferrari AND ('&') the model is California
...
################################################################################
## Setting new values

# new column, can be Pandas series, list, numpy array, etc.
df["Ranking_1"] = pd.Series([1, 3, 2, 4])
df["Ranking_2"] = [1, 3, 2, 4]
df["Ranking_3"] = np.array([1, 3, 2, 4])

# view
df
################################################################################
## Concatenating DataFrames

# Original DataFrame
data = {
    "Make": ["Volkswagen", "Fiat", "Ferrari", "Ferrari"],
    "Model": ["Jetta", "Panda", "250 GTO", "California"],
    "Year": [2024, 1987, 1963, 2021],
    "Price": [24875.00, 8200.00, 70000000.00, 255995.00],
    "MPG": [30, 8.9, 13.8, 25]
}
df = pd.DataFrame(data)

# Let's add some more data
additional_data = {
    "Make": ["Volkswagen", "Volkswagen", "Volkswagen", "Volkswagen", "Volkswagen",
             "Fiat", "Fiat", "Fiat", "Fiat", "Fiat",
             "Ferrari", "Ferrari", "Ferrari", "Ferrari", "Ferrari",
             "Alfa Romeo", "Alfa Romeo", "Alfa Romeo", "Alfa Romeo", "Alfa Romeo",
             "Subaru", "Subaru", "Subaru", "Subaru", "Subaru",
             "Chevrolet", "Chevrolet", "Chevrolet", "Chevrolet", "Chevrolet"],
    "Model": ["Golf", "Passat", "Tiguan", "Polo", "Arteon",
              "500", "Tipo", "Punto", "Panda Cross", "124 Spider",
              "488 Spider", "F8 Tributo", "Portofino", "Roma", "SF90 Stradale",
              "Giulia", "Stelvio", "4C", "GTV", "Giulietta",
              "Impreza", "Outback", "Forester", "Crosstrek", "WRX",
              "Malibu", "Camaro", "Equinox", "Tahoe", "Traverse"],
    "Year": [2022, 2023, 2021, 2020, 2022,
             1990, 2018, 2005, 2019, 2017,
             2020, 2019, 2021, 2021, 2022,
             2021, 2020, 2018, 2019, 2019,
             2021, 2020, 2019, 2022, 2022,
             2019, 2022, 2021, 2021, 2020],
    "Price": [23000.00, 27000.00, 25000.00, 22000.00, 35000.00,
              9500.00, 18500.00, 15000.00, 12000.00, 25000.00,
              280000.00, 320000.00, 215000.00, 222000.00, 625000.00,
              43000.00, 41000.00, 56000.00, 45000.00, 39000.00,
              23000.00, 27000.00, 25000.00, 24000.00, 36000.00,
              25000.00, 35000.00, 32000.00, 45000.00, 40000.00],
    "MPG": [28, 29, 26, 31, 25,
            10, 12, 14, 16, 20,
            15, 14, 16, 17, 18,
            24, 22, 28, 26, 25,
            27, 25, 24, 28, 22,
            29, 22, 25, 20, 23]
}
additional_df = pd.DataFrame(additional_data)

# Concatenate the original and additional DataFrames
df = pd.concat([df, additional_df], ignore_index=True)

# sort by Make, Model name
df = df.sort_values(by=["Make", "Model"])

# view the DataFrame with new data
df
################################################################################
## Operating on DataFrames

# Average MPG
df['MPG_mean'] = df["MPG"].mean()

# SD MPG
df['MPG_sd'] = df["MPG"].std()

# Add: Median MPG
df['MPG_median'] = ...

# Add: interquartile range for MPG
df['MPG_IQR'] = ...

# View df with new columns
df
################################################################################
# Average MPG within Make
df['MPG_mean_byMake'] = df.groupby('Make')['MPG'].transform('mean')

# Is MPG higher than overall average?
df = df.assign(MPG_vs_overallMean = np.select([df.MPG < df.MPG_mean, df.MPG > df.MPG_mean], ['Below', "Above"], np.nan))

# Add: Is MPG higher than average for make?
df = ...

# View df with new columns
df
################################################################################
## Aggregation, binning, and filtering

# Group by variable and compute averages
grouped = df.groupby('Make').agg({'Price': 'mean', 'MPG': 'mean'})
print(grouped)

# Make MPG bins
df = (df.assign(MPG_bin = lambda x: pd.cut(x['MPG'],
                                              bins=[0, 15, 25, 10000],
                                              labels=["<=15", "15-25", ">25"])))

# Add: Flag for most expensive car within each make
most_expensive_indices = df.groupby('Make')['Price'].idxmax()
df["Most_Expensive_inMake"] = False
df.loc[...] = ...

# View df with new columns
df
################################################################################
# Bonus: Writing functions for data cleaning

import pandas as pd
import numpy as np

# Create a DataFrame with issues in the Model and Price columns
data = {
    "Make": ["Volkswagen", "Fiat", "Ferrari", "Ferrari", "Volkswagen", "Volkswagen", "Volkswagen", "Volkswagen", "Volkswagen",
             "Fiat", "Fiat", "Fiat", "Fiat", "Fiat",
             "Ferrari", "Ferrari", "Ferrari", "Ferrari", "Ferrari",
             "Alfa Romeo", "Alfa Romeo", "Alfa Romeo", "Alfa Romeo", "Alfa Romeo",
             "Subaru", "Subaru", "Subaru", "Subaru", "Subaru",
             "Chevrolet", "Chevrolet", "Chevrolet", "Chevrolet", "Chevrolet"],
    "Model": ["VW Jetta", "Panda", "250 GTO", "California", "Volkswagen Golf", "Volkswagen Passat", "Volkswagen Tiguan", "VW Polo", "Volkswagen Arteon",
              "Fiat 500", "Fiat Tipo", "Fiat Punto", "Fiat Panda Cross", "Fiat 124 Spider",
              "Ferrari 488 Spider", "Ferrari F8 Tributo", "Ferrari Portofino", "Ferrari Roma", "Ferrari SF90 Stradale",
              "Alfa Giulia", "Stelvio", "Alfa 4C", "Alfa GTV", "Alfa Romeo Giulietta",
              "Subaru Impreza", "Subaru Outback", "Subaru Forester", "Subaru Crosstrek", "Subaru WRX",
              "Chevrolet Malibu", "Chevrolet Camaro", "Chevy Equinox", "Chevrolet Tahoe", "Chevy Traverse"],
    "Year": [2024, 1987, 1963, 2021, 2022, 2023, 2021, 2020, 2022,
             1990, 2018, 2005, 2019, 2017,
             2020, 2019, 2021, 2021, 2022,
             2021, 2020, 2018, 2019, 2019,
             2021, 2020, 2019, 2022, 2022,
             2019, 2022, 2021, 2021, 2020],
    "Price": ["$24875", "Price is $8200", "($70000000)", "$255995", "$23000", "$27000", "Price: $25000", "€22000", "35,000",
              "9500 dollars", "$18500", "15k", "$12000", "25000 USD",
              "€280000", "Price is $320000", "$215000", "222000", "($625000)",
              "43,000", "$41000", "56k", "$45000", "39,000",
              "23,000", "$27000", "Price: $25000", "24k", "36000",
              "$25000", "$35000", "$32000", "45000", "$40000"]
}

# Create DataFrame
df = pd.DataFrame(data)

df = df.sort_values(by = ["Make", "Model"])

# Backup the DataFrame
df_backup = df.copy()

# View the df
# print(df)
# print()

# There are two issues here:

## 1. We have redundant make names in "Model" column. E.g., "Alfa 4C", "VW Jetta"
print(df[df["Model"].str.contains(" ")].Model.values)
print()

## 2. Prices are formatted weird, and we want straightforward numbers
print(df["Price"].values)
print()

# TASK: brainstorm what steps we should take to fix these issues

################################################################################
## Bonus: writing functions for data cleaning

# Step 1: Fix redundant info in the "Model" column

# First, we can write a function that works on individual row values in a column

def clean_model(row, min_matches=2):
    make = row['Make'].lower().replace(' ', '')  # Remove spaces from make name for matching
    model = row['Model']

    # Split the model name into words
    model_words = model.split()

    # Remove words with min_matches or more letter matches to the make name, except the last word
    cleaned_model_words = []
    for i, word in enumerate(model_words):
        if i == len(model_words) - 1:
            cleaned_model_words.append(word)
        else:
            # Check if the word has min_matches or more letters from the make
            word_lower = word.lower()
            match_count = sum(1 for char in word_lower if char in make)
            if match_count < min_matches:
                cleaned_model_words.append(word)

    # Join the remaining words to form the cleaned model name
    model = ' '.join(cleaned_model_words)

    return model

# Then we can apply our function to each row in the 'Model' column using a method in pandas called .apply()

df['Model'] = df.apply(clean_model, axis=1)

# View the cleaned DataFrame
df # Note the changes in the Model column
################################################################################
################################################################################
## How does clean_model work? ##################################################
################################################################################

df = df_backup.copy()

# First inspect the input to the function (DataFrame row)

# pick a row number to test
test_row = 0

row = df.iloc[test_row]
print("Our target row:")
print(row)
print()

# our function has a default argument, 'min_matches=2', which acts like an input
min_matches = 2

# Then we'll look at the first variables created in the function (make & model)

make = row['Make'].lower().replace(' ', '')  # We're converting this to lowercase and removing spaces
print(f"Make: \n{make}")
print()

model = row['Model']
print(f"Model: \n{model}")
print()

# Split the model name into words

model_words = model.split()
print(f"Model Words: \n{model_words}")
print()

# Iterate through the model words, except the last word, and check for matches

# Initialize an empty list to hold the cleaned model words
cleaned_model_words = []

# Enumerate through the model words to get both the index and the word
for i, word in enumerate(model_words):
    # If this is the last word, always add it to the cleaned_model_words list
    print(f"Current word: {word}")
    if i == len(model_words) - 1:
        print(f"Keep the last word in the model name: {word}")
        cleaned_model_words.append(word)
    else:
        # Convert the word to lowercase for comparison
        word_lower = word.lower()
        print(f"Current word (to lowercase): {word_lower}")

        # Count the number of characters in the word that are also in the make name
        match_count = sum(1 for char in word_lower if char in make)
        print(f"Match count for '{word_lower}' with make '{make}': {match_count}")

        # If the match count is less than the minimum matches, add the word to cleaned_model_words
        if match_count < min_matches:
            print(f"Appending word (less than {min_matches} matches): {word}")
            cleaned_model_words.append(word)
        else:
            print(f"Target word (has {match_count} matching characters): {word}")
    print()

# The cleaned_model_words list now contains the filtered model words
print()
print(f"Cleaned Model Name: {cleaned_model_words}")
print()
################################################################################
# Step 2: Clean the "Price" column

# First, we can write a function that works on individual row values in a column

def clean_price(price):
    # Convert price to lowercase for consistent processing
    price = price.lower()

    # Handle 'k' for thousands
    if 'k' in price:
        price = price.replace('k', '000')

    # Handle conversion from euros to dollars
    euro_to_dollar_rate = 1.1
    if '€' in price or 'eur' in price:
        price = price.replace('€', '').replace('eur', '').strip()
        is_euro = True
    else:
        is_euro = False

    # Remove non-numeric characters except for periods
    num_str = ''
    for char in price:
        if char.isdigit() or char == '.':
            num_str += char

    # Convert to float if possible
    if num_str:
        price = float(num_str)
        if is_euro:
            price *= euro_to_dollar_rate
    else:
        return None

    return price

# Then we can apply our function to each row in the 'Price' column using a method in pandas called .apply()

df['Price'] = ...

# View the cleaned DataFrame
df # Note that prices are converted to numeric values and standardized to dollars
################################################################################
################################################################################
## How does clean_price work? ##################################################
################################################################################

df = df_backup.copy()

test_row = 12
row = df.iloc[test_row]

# Inspect the input to the function

price = row['Price']
print("Original Price:")
print(price)
print()

# Convert price to lowercase for consistent processing

price = price.lower()

# Handle 'k' for thousands

if 'k' in price:
    print("'k' detected")
    price = price.replace('k', '000')
    print(f"'k' to thousands: {price}")
else:
    print("No 'k' detected")
print()

# Handle conversion from euros to dollars

euro_to_dollar_rate = 1.1
if '€' in price or 'eur' in price:
    price = price.replace('€', '').replace('eur', '').strip()
    is_euro = True
else:
    is_euro = False
print(f"Price in Euro?: {is_euro}")
print()

# Remove non-numeric characters except for periods

num_str = ''
for char in price:
    if char.isdigit() or char == '.':
        num_str += char

# Convert to float if possible

if num_str:
    price = float(num_str)
    if is_euro:
        price *= euro_to_dollar_rate
        print(f"Final Price (euro to USD): {price}")
    else:
        print(f"Final Price (already in USD): {price}")
################################################################################
## Load Python plotting modules

import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for the plots
sns.set(style="whitegrid")
################################################################################
# 1. Subplotted histograms of "MPG", "Price", "Year"
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Histogram for MPG
sns.histplot(df['MPG'], bins=10, kde=True, ax=axes[0])
axes[0].set_title('Histogram of MPG')

# Histogram for Price
sns.histplot(df['Price'], bins=10, kde=True, ax=axes[1])
axes[1].set_title('Histogram of Price')

# Histogram for Year
sns.histplot(df['Year'], bins=10, kde=True, ax=axes[2])
axes[2].set_title('Histogram of Year')

plt.tight_layout()
plt.show()
################################################################################
# 2. MPG by Price (line with dots)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Price', y='MPG', marker='o')
plt.title('MPG by Price')
plt.show()
################################################################################
# Removing price outliers
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
price_filtered_df = df[~((df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR)))]

# MPG by Price without outliers
plt.figure(figsize=(10, 6))
sns.lineplot(data=price_filtered_df, x='Price', y='MPG', marker='o', errorbar=None)
plt.title('MPG by Price (Without Outliers)')
plt.show()
################################################################################
# 3. Boxplot with violins for MPG within make
plt.figure(figsize=(12, 6))
sns.violinplot(x='Make', y='MPG', data=df, inner=None, palette="vlag", alpha = 0.3)
sns.boxplot(x='Make', y='MPG', data=df, whis=[0, 100], width=.2, palette="vlag")
plt.title('Boxplot with Violins for MPG within Make')
plt.show()
################################################################################
# 4. Boxplot with violins for Price within make
plt.figure(figsize=(12, 6))
sns.violinplot(x='Make', y='Price', data=df, inner=None, color=".8")
sns.boxplot(x='Make', y='Price', data=df, whis=[0, 100], width=.2, palette="vlag")
plt.title('Boxplot with Violins for Price within Make')
plt.show()

# Filter out the Ferrari 250 GTO as an outlier
price_filtered_df_ferrari = df[~((df['Make'] == 'Ferrari') & (df['Model'] == '250 GTO'))]

# Boxplot with violins for Price within make (without Ferrari 250 GTO)
plt.figure(figsize=(12, 6))
sns.violinplot(x='Make', y='Price', data=price_filtered_df_ferrari, inner=None, color=".8")
sns.boxplot(x='Make', y='Price', data=price_filtered_df_ferrari, whis=[0, 100], width=.2, palette="vlag")
plt.title('Boxplot with Violins for Price within Make (Without Ferrari 250 GTO)')
plt.show()
################################################################################
# Task: Make a boxplot with violins for Price within make (without any Ferrari)
...
################################################################################
# 5. MPG by Price with individual colored dots and lines within each make, removing Price outliers
plt.figure(figsize=(12, 8))
sns.lineplot(data=price_filtered_df, x='Price', y='MPG', hue='Make', marker='o', style='Make', palette='tab10')
plt.title('MPG by Price with Individual Colored Dots and Lines within Each Make (Without Outliers)')
plt.show()
################################################################################
