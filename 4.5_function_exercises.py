# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2

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
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def capitalize_begining_consonants(word):
    first_letter = word[0]
    if first_letter in vowels:
        return word
    else:
        return word.capitalize()

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip(tip,bill):
    if tip >= 1:
        tip /= 100
    tip_amount = bill * tip
    return bill + tip_amount

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
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in letters:
        if letter not in vowels:
            new_word += letter
    return new_word

