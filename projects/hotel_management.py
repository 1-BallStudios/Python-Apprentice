"""

"""

from tkinter import messagebox, simpledialog, Tk
import tkinter

""" REFRENCES

button = tkinter.Button(window, text="",font=("Arial",24),command=None)
button.place(x=0,y=0)

screen = tkinter.Label(window, bg="white",width=20,font=("Arial",24),text="")
screen.place(x=0,y=0)

"""

rooms = []

for i in range (50):
    rooms.append("Empty")

window = Tk()
window.title("Hotel Management")
window.geometry("500x500")
window.resizable(False, False)

def CIG():
    room = simpledialog.askinteger(None, "enter a room (1-50)")
    if rooms[room-1] == "Empty" and room > 0 and room < 51:
        rooms[room-1] = "Full"

def COG():
    room = simpledialog.askinteger(None, "enter a room (1-50)")
    if rooms[room-1] == "Full" and room > 0 and room < 51:
        rooms[room-1] = "Empty"

button1 = tkinter.Button(window, text="Check In Guest",font=("Arial",18),command=CIG)
button1.place(x=25,y=25)
button2 = tkinter.Button(window, text="Check Out Guest",font=("Arial",18),command=COG)
button2.place(x=250,y=25)

window.mainloop()