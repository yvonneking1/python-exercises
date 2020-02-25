# 1. Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

import function_exercises as fe

fe.capitalize_begining_consonants("tomato")

fe.cumsum([1, 2, 3, 4])

fe.get_letter_grade(84)

from function_exercises import capitalize_begining_consonants as c

c('rover')

from function_exercises import get_letter_grade as get_letter_grade
grade(87)



# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import permutations
len(list(permutations(["a", "b", "c", 1, 2, 3])))

# 2. How many different ways can you combine two of the letters from "abcd"?
from itertools import combinations
len(list(combinations(["a", "b", "c", "d"], 2)))

# write some code that calculates and outputs the following information:









# Total number of unread messages for all users
import json
profiles_list = json.load(open("profiles.json"))

# Total number of users
num_of_profiles = len(profiles_list)

# Number of active users
active_profiles = [profile for profile in profiles_list if profile['isActive'] == True]
num_active_profiles = len(active_profiles)

# Number of inactive users
num_inactive_profiles = num_of_profiles - num_active_profiles 
inactive_profiles = [profile for profile in profiles_list if profile['isActive'] == False]

# Grand total of balances for all users
balances_with_dollar_sign = [profile["balance"] for profile in profiles_list]
balances = [float(balance.replace("$", "").replace(",", "")) for balance in balances_with_dollar_sign]
sum_of_balances = sum(balances)

# Average balance per user
average_balance = sum_of_balances/num_of_profiles

# User with the lowest balance
user_with_lowest_balance = [profile for profile in profiles_list if profile["balance"] == min(balances_with_dollar_sign)]

# User with the highest balance
user_with_highest_balance = [profile for profile in profiles_list if profile["balance"] == max(balances_with_dollar_sign)]

# Most common favorite fruit
common_favorite_fruit = fruit for fruit in fruits
import statistics 
from statistics import mode
most_common_fruit = mode(fruits)

# Least most common favorite fruit
from collections import Counter
fruit_count = Counter(fruits)
least_favorite_fruit = sorted(fruit_count)[0]
