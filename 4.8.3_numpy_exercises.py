# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
negative_number = a < 0
negative_number.sum()

# 2. How many positive numbers are there?
positive_numbers = a > 0
positive_numbers.sum()

# 3. How many even positive numbers are there?
positive_numbers = a [a > 0]
positive_evens = positive_numbers % 2 == 0
positive_evens.sum()

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
add_3 = a[a + 3]
positive_numbers1 = add_3 > 0
positive_numbers1.sum()

# 5. If you squared each number, what would the new mean and standard deviation be?
squared_numbers = a ** 2
np.mean(squared_numbers)
np.std(squared_numbers)

# 6. A common statistical operation on a dataset is centering.
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

centered_data = squared_numbers - np.mean(squared_numbers)

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = x − μ / σ
z_score = (a - np.mean(a)) / np.std(a)


# Numpy excercises cont.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:

# Exercise 1 - Make a variable called sum_of_a to 
# hold the sum of all the numbers in above list
sum_of_a = np.sum(a)

# Exercise 2 - Make a variable named min_of_a to
# hold the minimum of all the numbers in the above list
min_of_a = np.min(a)

# Exercise 3 - Make a variable named max_of_a 
# to hold the max number of all the numbers in the above list
max_of_a = np.max(a)

# Exercise 4 - Make a variable named mean_of_a 
# to hold the average of all the numbers in the above list
mean_of_a =np.mean(a)

# Exercise 5 - Make a variable named product_of_a 
# to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
step_1 = np.array(a)
odds_in_a = step_1[step_1 % 2 != 0]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = step_1[step_1 % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [[3, 4, 5], [6, 7, 8]]

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **
# Hint, you'll first need to make sure that the "b" variable is a numpy array**
