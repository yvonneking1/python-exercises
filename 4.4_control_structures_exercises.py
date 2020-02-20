# 1. Conditional Basics
# a) prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = input("What day of the week is it?")
if day_of_the_week == 'Monday':
    print("Today is Monday, blah!")
else:
    print("Today is not Monday, it is", day_of_the_week)
print("Have a great", day_of_the_week)

# b) prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekend_or_not = input("What day of the week is it?")
if weekend_or_not == "Saturday" or weekend_or_not == "Sunday":
    print("Hooray!", weekend_or_not, "is part of the weekend!!")
elif weekend_or_not == "Friday":
    print("ALright!", weekend_or_not, "is the start of the weekend")
else:
    print(weekend_or_not, "is sadly a weekday")

# c) create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
num_hours_worked_in_a_week = 47
hourly_rate = 45
paycheck_total = 0
if num_hours_worked_in_a_week <= 40:
    paycheck_total += num_hours_worked_in_a_week * hourly_rate
    print("This week you made", paycheck_total, "dollars")
else:
    paycheck_total += (40 * hourly_rate) + ((num_hours_worked_in_a_week - 40) * (hourly_rate * 1.5))
    print("This week you made", paycheck_total, "dollars")

# 2. Create an integer variable i with a value of 5.
i = 5
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

n = 0
while n < 102:
    print(n)
    n += 2
print("hello")

# Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x >= -10:
    print(x)
    x -= 5

# Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000. Output should equal:
num = 2
while num < 1000000:
    print(num)
    num = num ** 2

# Write a loop that uses print to create the output shown below.
# 100
# 95
# 90 all the way to 5
num1 = 100
while num1 >= 5:
    print(num1)
    num1 -= 5
print('hello')

# 2b) Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:
muliples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_input = input('Please enter in a number')
for number in muliples:
    print(num_input, "x", number, "=", str((number * int(num_input))))

# Create a for loop that uses print to create the output shown below.1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
nums = [2, 3, 4, 5, 5 , 6, 7, 8, 9]
for num in nums:
    print(num * str(num))

# 2c) break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Your output should look like this:
# Number to skip is: 27

num_range = range(1,51)

for num in num_range:
    if num == 27:
        continue
    elif num % 2 != 0:
        print("Here is an odd number:", str(num))


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a numeric type.)
positive_number = input('Please enter a postive number')
count_numbers = 0

if int(positive_number) < 0:
    positive_number = input('Please enter a postive number')
    
while int(positive_number) > 0 and count_numbers != int(positive_number):
    count_numbers += 1
    print(count_numbers)

# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.

# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

fizz_numbers = range(1,101)
for num in fizz_numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 4. Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

first_int = input("Please provide a number greater than 0")
first_range = range(1, (int(first_int) + 1))

for num in first_range:
    if num <= int(first_int):
        print("number | squared | cubed")
        print("------ | ------ | ------ |")
        print(str(num), str(num ** 2), str(num ** 3))
              
user_continue = input("Would you like to continue, yes or no?")

if user_continue.lower() == "no":
    print("Have a great day!")

if user_continue.lower() == "yes":
    new_number = input("What number would you like to go up to?")
    second_range = range(1, (int(new_number) + 1))
    for nums in second_range:
        if nums <= int(new_number):
            print("number | squared | cubed")
            print("------ | ------ | ------ |")
            print(str(nums), str(nums ** 2), str(nums ** 3))

# 5.Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

number_grade = input("What is your numerical grade?")

if int(number_grade) <= 59:
    print("You received an F")
elif int(number_grade) <= 66:
    print("You received a D")
elif int(number_grade) <= 79:
    print("You received a C")
elif int(number_grade) <= 87:
    print("You received a B")
else:
    print("You received an A")

cont_with_grades = input("Would you like to continue, yes or no?")

if cont_with_grades.lower() == 'yes':
    new_number_grade = input("Enter in your next numerical grade")
    if int(new_number_grade) <= 59:
        print("You received an F")
    elif int(new_number_grade) <= 66:
        print("You received a D")
    elif int(new_number_grade) <= 79:
        print("You received a C")
    elif int(new_number_grade) <= 87:
        print("You received a B")
    elif int(new_number_grade) > 87:
        print("You received an A")