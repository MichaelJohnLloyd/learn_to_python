
'''Try except. The code below will take a number that you put in and convert into an integer (as numbers
are inputted as strings). It will try to do this, but if you put in a string, like a word,
it will process the except prompt.'''

try:
    number = int(input("Enter a number: "))

    print(number)

# I have made err a variable below which will contain the ValueError.
except ValueError as err:

# By printing the variable it details the exact issue. For example, if I input f, it would detail that
# f is not an integer and does not have a numerical value.
        print(err)