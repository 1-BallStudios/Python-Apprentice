"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""


from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

num1 =  simpledialog.askfloat("First Number", "What is your first number?")

num2 =  simpledialog.askfloat("Second Number", "What is your second number?")

messagebox.showinfo('sum', "The sum of the 2 numbers is " + str(num1+num2))

window.mainloop()

