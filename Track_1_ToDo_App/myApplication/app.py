
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, 'todo_list.txt')

todo_list = []
# Load todo list from todo_list.txt
try:
    with open(todo_file, "r") as file:
        todo_list = [line.strip() for line in file]
except FileNotFoundError:
    pass

#continue to loop and display menu until user selects to exit the program
while True:
    print() # Add a couple of blank lines
    print()
    print("To-do list: ") # Print the title of the list
    for index, todo in enumerate(todo_list, start=1): # Loop through existing to-do items with index
        print(f"{index}. {todo}") # Print item number and todo item

    # Print the menu
    print() # Add a of blank lines
    print("Actions:")
    print("A - Add to-do item")
    print("R - Remove")
    print("X - Exit")
    choice = input("Enter your choice (A or X): ")
    choice = choice.upper() #converts the choice to uppercase

    #user selected 'a' or 'A' - To Add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ") 
        todo_list.append(todo)
        continue  #tells the program to go back to the start of the loop
    #user selected 'r' or 'R' - To Remove an item from the list
    if choice == "R":
        item_number = int(input("Enter the number of the item to remove: "))
        if item_number > 0 and item_number <= len(todo_list):
            todo_list.pop(item_number - 1)
        else:
            print("Invalid item number")
        continue

    #user selected 'x' or 'X' to exit program
    if choice == "X":
        with open("todo_list.txt", "w") as file:
            for todo in todo_list:
                file.write(todo + "\n")
        break #tells the program to exit the loop

    #user selected something else
    print("Invalid choice")
    

