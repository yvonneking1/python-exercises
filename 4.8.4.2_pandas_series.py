# 1. Use pandas to create a Series from the following data:
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
import pandas as pd
import numpy as np

# a. Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# b. Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()

# c. Run the code necessary to produce only the unique fruit names.
fruits.unique()

# d. Determine how many times each value occurs in the series.
fruits.value_counts()

# e. Determine the most frequently occurring fruit name from the series.
fruits.mode()

# f. Determine the least frequently occurring fruit name from the series.
fruits.value_counts()

# g. Write the code to get the longest string from the fruits series.
fruits[fruits.str.len().sort_values(ascending = False)].max()
fruits[5]

# h. Find the fruit(s) with 5 or more letters in the name.
def fruits_with_more_than_5_characters(fruit):
    if len(fruit) > 5:
        return fruit

fruits.apply(fruits_with_more_than_5_characters)

# i. Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# j. Count the letter "a" in all the fruits (use string vectorization)
fruits.apply(lambda l: l.count("a"))

# k. Output the number of vowels in each and every fruit.
def count_vowels(letters):
    vowels = list("aeiou")
    count = 0
    for letter in letters:
        if letter in vowels:
            count += 1
    return count

fruits.apply(count_vowels).count_values()

# l. Use the .apply method and a lambda function to find the fruit(s) containing 
# two or more "o" letters in the name.
fruits.apply(lambda l: l.count("o") >= 2)

# m. Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.contains("berry")]


# n. Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.contains("apple")]

# o. Which fruit has the highest amount of vowels?
fruits[fruits.apply(count_vowels).max()]

# Use pandas to create a Series from the following data:
datapoints = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])# What is the data type of the series?

# What is the data type of the series?
datapoints.describe()

# Use series operations to convert the series to a numeric data type.
with_commas = datapoints.str[1:]
new_list = with_commas.str.replace(",", "")
numbers = new_list.astype("float")

# What is the maximum value? The minimum?
numbers.agg(['max', 'min'])

# Bin the data into 4 equally sized intervals and 
# show how many values fall into each bin.
pd.cut(numbers, 4).value_counts().sort_index()

# Plot a histogram of the data. Be sure to include a title and axis labels.
%matplotlib inline
import matplotlib.pyplot as plt
numbers.plot.hist()
plt.title('Distribution of Numbers')
plt.xlabel('Bins')
plt.ylabel('Frequency')

# Use pandas to create a Series from the following exam scores:
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# What is the minimum exam score? The max, mean, median?
exam_scores.agg(["min", "max", "mean", "median"])

# Plot a histogram of the scores.
exam_scores.plot.hist()

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def convert_to_letter_grade(n):
    if n >= 90  :
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    elif n >= 60:
        return 'D'
    else:
        return 'F'

exam_scores.apply(convert_to_letter_grade)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.
curved_exam_scores = exam_scores + (100 - exam_scores.max())

# Use pandas to create a Series from the following string:
string_list = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# What is the most frequently occuring letter? Least frequently occuring?
string_list.mode()

# How many vowels are in the list?


# How many consonants are in the list?

# Create a series that has all of the same letters, but uppercased
string_list[string_list.str.upper()]

# Create a bar plot of the frequencies of the 6 most frequently occuring letters.