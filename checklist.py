
checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# READ ALL
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "√"+checklist[index]

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def select(function_code):
    # Create item

    if function_code.capitalize() == "C":
        #Create item in checklist here
        item = user_input("Add to list: ")
        create(item)


    elif function_code.capitalize() == "R":
        # Read item in checklist here
        index = user_input("Index of item you want to read: ")
        print(read(int(index)))

    elif function_code.capitalize() == "P":
        # Print all items here
        list_all_items()

    elif function_code.capitalize() == "Q":
        # This is where we want to stop our loop
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True


running = True
while running:

    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list: ")
    running = select(selection)


def test():
    # Your testing code here

    user_value = user_input("Please Enter a value:")
    print(user_value)

    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

# test()
