from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 100)

print(random_num)

# 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):
    number = simpledialog.askfloat("Guess", "What is your guess?")

    if number == random_num:
        sys.exit(0)
elif number >= random_num:
        messagebox.showinfo("High or Low", "Too High!")
    elif number <= random_num:
        messagebox.showinfo("High or Low", "Too Low!")

messagebox.showinfo("High or Low", "Game Over!")

window.mainloop()
