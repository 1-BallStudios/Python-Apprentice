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
nights = []
guests = dict()

for i in range (50):
    rooms.append("Empty")
    nights.append("")
    guests[str(i+1)] = "NONE"

window = Tk()
window.title("Hotel Management")
window.geometry("500x500")
window.resizable(False, False)

def CIG():
    room = simpledialog.askinteger("Check In Guest", "enter a room (1-50)")
    if room > 0 and room < 51 and rooms[room-1] == "Empty":
        rooms[room-1] = "Full"
        night = simpledialog.askinteger("Check In Guest", "enter # of nights (1+)")
        if night > 0:
            nights[room-1] = str(night)
            name = simpledialog.askstring("Check In Guest", "enter name")
            guests[str(room)] = name

def COG():
    room = simpledialog.askstring("Check Out Guest", "enter name")
    #if room > 0 and room < 51 and rooms[room-1] == "Full":
    rooms[room-1] = "Empty"
    cost = 0
    for i in range(50):
        if guests[str(i+1)] == guests[str(room)]:
            cost += 50 * int(nights[i])
            nights[i] = ""
            guests[str(i)] = "NONE"
        messagebox.showinfo("Check Out Guest", guests[str(room)] + " is charged $" + str(cost))


button1 = tkinter.Button(window, text="Check In Guest",font=("Arial",18),command=CIG)
button1.place(x=25,y=25)
button2 = tkinter.Button(window, text="Check Out Guest",font=("Arial",18),command=COG)
button2.place(x=250,y=25)

window.mainloop()