from tkinter import *
import tkinter.messagebox as Message

tk = Tk()

tk.title("Q5")
tk.geometry('800x200')

def message1():
    Message.showinfo("Insert", "Data is inserted in db")


def message2():
    Message.showinfo("Update", "Data is updated in db")


def message3():
    Message.showinfo("Delete", "Data is deleted in db")


def message4():
    Message.showinfo("Select", "Data is selected in db")

def setVal():
    # print("You selected ", g.get())
    if g.get() == 1:
        print("A")
    elif g.get() == 2:
        print("B")

def setDes():
    # print("You selected ", g.get())
    if d1.get() == 1:
        print("7:15pm")
    if d2.get() == 1:
        print("9am")


reg = Label(tk, text="BookingId")
reg.grid(column=0, row=0)
regd = Entry(tk, width=40)
regd.grid(column=1, row=0)

name = Label(tk, text="Passenger Name : ")
name.grid(column=0, row=1)
nameEl = Entry(tk, width=40)
nameEl.grid(column=1, row=1)

dept = Label(tk, text="Flight")
dept.grid(column=0, row=2)
deptEl = Entry(tk, width=40)
deptEl.insert(0, "IND345")
deptEl.grid(column=1, row=2)

g = IntVar()

gender = Label(tk, text="Class")
gender.grid(column=0, row=3)
male = Radiobutton(tk, text="A", variable=g, command=setVal, value=1)
female = Radiobutton(tk, text="B", variable=g, command=setVal, value=2)
male.grid(column=1, row=3)
female.grid(column=2, row=3)

d1 = IntVar()
d2 = IntVar()
gender = Label(tk, text="Time of Show")
gender.grid(column=3, row=3)
male = Checkbutton(tk, text="7:15pm", variable=d1, command=setDes)
female = Checkbutton(tk, text="9am", variable=d2, command=setDes)
male.grid(column=4, row=3)
female.grid(column=5, row=3)

age = Label(tk, text="Age")
age.grid(column=0, row=4)
ageEn = Scale(tk, from_=3, to=10, orient=HORIZONTAL)
ageEn.grid(column=1, row=4)

btnInsert = Button(tk, text="Insert", command=message1)
btnUpdate = Button(tk, text="Update", command=message2)
btnDelete = Button(tk, text="Delete", command=message3)
btnSelect = Button(tk, text="Select", command=message4)
btnInsert.grid(column=0, row=5)
btnUpdate.grid(column=1, row=5)
btnDelete.grid(column=0, row=6)
btnSelect.grid(column=1, row=6)

tk.mainloop()