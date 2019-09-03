
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
        print("\033[0;32m{} {}\033[0m".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "√ "+checklist[index]

# user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def is_empty():
    if not checklist:
        user_input("List is empthy, Press Enter key to go back: ")
        return True
    return False

# check if user input is a number
def is_number(index):
    while(index.isdigit() == False):
        index = user_input("That's not a number, please an index number: ")
    return index

# Check if user input is within range
def out_of_range(index):
    while(int(index) >= len(checklist)):
        msg = "Index out of range, please enter an index between 0 and "+str(len(checklist)-1)+": "
        index = user_input(msg)
        index = is_number(index)
    return index

def select(function_code):
    if function_code.capitalize() == "C":
        #Create item in checklist here
        item = user_input("\033[0;32mAdd\033[0m to list: ")
        create(item)

    elif function_code.capitalize() == "R":
        # Read item in checklist here
        if(is_empty() == False):
            index = user_input("Index of item you want to\033[36;6;36m read\033[0m: ")
            index = is_number(index)
            index = out_of_range(index)
            print(read(int(index)))

    elif function_code.capitalize() == "D":
        # delete item in checklist here
        if(is_empty() == False):
            index = user_input("Index of item you want to\033[37;0;37m delete\033[0m: ")
            index = is_number(index)
            index = out_of_range(index)
            destroy(int(index))
            list_all_items()

    elif function_code.capitalize() == "F":
        # delete item in checklist here
        if(is_empty() == False):
            index = user_input("Index of item you\033[0;32m completed\033[0m: ")
            index = is_number(index)
            index = out_of_range(index)
            mark_completed(int(index))
            list_all_items()

    elif function_code.capitalize() == "P":
        # Print all items here
        list_all_items()

    elif function_code.capitalize() == "U":
        # Print all items here
        if(is_empty() == False):
            index = user_input("Index of item you want to \033[35;6;35mupdate\033[0m: ")
            index = is_number(index)
            index = out_of_range(index)
            item = user_input("Enter new item: ")
            update(int(index), item)

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
        "Press C to add to list,\033[36;6;36m R to Read\033[0m from list,\033[35;6;35m U  to update \033[0m an item,\033[37;0;37m D to remove\033[0m an item,\033[34;6;34m P to display \033[0m list,\033[0;32m F to complete\033[0m and\033[30;6;30m Q to exit\033[0m: ")
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
