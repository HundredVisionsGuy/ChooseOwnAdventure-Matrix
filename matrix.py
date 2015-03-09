# Matrix.py
# by Hundred Visions Guy, 
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "Add some intro to the story." + \
                        "\nAdd some good storytelling info.")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Do you choose the blue pill (1)" + \
                                    " or the red pill(2)?")
    if choice == 1:
        blue()
    elif choice == 2:
        red()
    else:
        messagebox.showinfo("Incorrect Entry",
                            "That was not an option. Type '1' for blue," + \
                            "or '2' for red.")
        intro()

################ Hundred Visions Guy Functions #####################
def red():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ GiveMeYourMilk Functions #####################
def blue():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        blue()

################ Main #####################
intro()

root.destroy()
