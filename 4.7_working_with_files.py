#1 . Read the contents of your last exercise file into a variable.
# a. Print out every line in the file
# b. Print out every line in the file, but add a line numbers
with open("4.6_import_exercises.py",) as f:
    import_exercisses = f.read()

print(import_exercisses)

with open("4.6_import_exercises.py") as f:
    for i, line in enumerate(f, start=1):
        print('{} = {}'.format(i, line.strip()))


# 2. Write some python code to create a grocery list.
# a. Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 
#    3 things that you need to buy from the grocery store.
# b. Create a function named make_grocery_list. 
#    When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.
# c. Create a function named show_grocery_list. When run, it should read the items from the text file and show each item on the
#  grocery list.
# d. Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.

grocery_list = ["sangiovese", "cheese", "fruit"]

def make_grocery_list(items = grocery_list):
    with open("my_grocery_list1.txt", "a") as f:
        for item in items:
            f.write(item + "/n")


def show_grocery_list():
    with open("my_grocery_list1.txt") as f:
        items = f.read()
    return items


def buy_item(item):
    return grocery_list.remove(item)



