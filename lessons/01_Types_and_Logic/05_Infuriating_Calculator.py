"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

num1 =  simpledialog.askfloat("First Number", "What is your first number?")

num2 =  simpledialog.askfloat("Second Number", "What is your second number?")

operation =  simpledialog.askstring("Operation", "What is the operation")

if operation == "+":
    messagebox.showinfo('calc', str(num1+num2))
elif operation == "-":
    messagebox.showinfo('calc', str(num1-num2))
elif operation == "*":
    messagebox.showinfo('calc', str(num1*num2))
elif operation == "/":
    messagebox.showinfo('calc', str(num1/num2))
else:
    messagebox.showerror()
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

window.mainloop()