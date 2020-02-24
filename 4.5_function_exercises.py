# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == "2"

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    if x.lower() in ('a','e','i','o') and len(x) == 1:
        return True
    else:
        return False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    if is_vowel(x) or len(x) > 1:
        return False
    else:
        return True

# 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_begining_consonants(word):
    first_letter = word[0]
    if is_vowel(first_letter):
        return word
    else:
        return word.capitalize()

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip(tip,bill):
    if tip >= 1:
        tip /= 100
    tip_amount = bill * tip
    return tip_amount 

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
def apply_discount(price, discount):
    if discount >= 1:
        discount /= 100
    discount_total = price * discount
    return price - discount_total

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.
def handle_commas(number_string):
    new_number = number_string.replace(",","")
    return int(new_number)

# 8.Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(x):
    if x >= 90:
        return "A"
    elif x >=80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(letters):
    new_word = ""
    for letter in letters:
        if is_consonant(letter):
            new_word += letter
    return new_word

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def remove_leading_whitespace(words):
    words = words.lower()
    if words[0] == " ":
        return words[1:]
    else:
        return words
    
def remove_ending_whitespace(words):
    words = remove_leading_whitespace(words)
    if words[-1] == [" "]:
        return words[:-1]
    else:
        return words

def normalize_name(words):
    words = remove_ending_whitespace(words)
    return words.replace(" ", "_")

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative 
# sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(numbers):
    total = 0
    new_list = []
    for num in numbers:
        total += num
        new_list.append(total)
    return new_list

#Bonus questions
# 1. Create a function named twelveto24. It should accept 
# a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.

def twelveto24(time):
    if time[-2] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2] == "AM":
        return time[:-2]
    elif time[-2] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:-2]
