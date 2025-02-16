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
guests = dict()
screen_content = "None"
index = 1

for i in range (50):
    rooms.append(True)
    guests[str(i+1)] = "NONE"

window = Tk()
window.title("Hotel Management")
window.geometry("500x500")
window.resizable(False, False)

def CIG():
    room = simpledialog.askinteger("Check In Guest", "enter a room (1-50)")
    if room > 0 and room < 51 and rooms[room-1]:
        rooms[room-1] = False
        night = simpledialog.askinteger("Check In Guest", "enter # of nights (1+)")
        if night > 0:
            name = simpledialog.askstring("Check In Guest", "enter name")
            guests[name] = (room,night)
    update_display()

def COG():
    name = simpledialog.askstring("Check Out Guest", "enter name")
    room = guests[name][0]
    rooms[room-1] = True
    cost = 0
    if guests[name]:
        rooms[guests[name][0]] = True
        cost += 50 * int(guests[name][1])
        guests[name] = None
        messagebox.showinfo("Check Out Guest", name + " is charged $" + str(cost))
    update_display()

def update_display():
    screen_content = "None"
    for i in guests.keys():
        if guests[i][0] == index:
            screen_content = i + ': Room: ' + str(guests[i][0]) + ", Nights: " + str(guests[i][1])
    screen = tkinter.Label(window, bg="white",width=25,font=("Arial",24),text=screen_content)
    screen.place(x=20,y=100)

def Up():
    global index
    if index <= 49:
        index += 1
    update_display()

def Down():
    global index
    if index >= 2:
        index -= 1
    update_display()

update_display()
button1 = tkinter.Button(window, text="Check In Guest",font=("Arial",18),command=CIG)
button1.place(x=25,y=25)
button2 = tkinter.Button(window, text="Check Out Guest",font=("Arial",18),command=COG)
button2.place(x=250,y=25)
button1 = tkinter.Button(window, text="+1",font=("Arial",18),command=Up)
button1.place(x=25,y=150)
button2 = tkinter.Button(window, text="-1",font=("Arial",18),command=Down)
button2.place(x=80,y=150)

window.mainloop()