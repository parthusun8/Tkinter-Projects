from tkinter import *
import tkinter.messagebox as Message



tk = Tk()

tk.title("Q2")
tk.geometry('450x200')


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
        print("Saving")
    else:
        print("Non Saving")


reg = Label(tk, text="CustId")
reg.grid(column=0, row=0)
regd = Entry(tk, width=40)
regd.grid(column=1, row=0)

name = Label(tk, text="Customer Name : ")
name.grid(column=0, row=1)
nameEl = Entry(tk, width=40)
nameEl.grid(column=1, row=1)

dept = Label(tk, text="Branch")
dept.grid(column=0, row=2)
deptEl = Entry(tk, width=40)
deptEl.insert(0, "adyar")
deptEl.grid(column=1, row=2)

g = IntVar()

gender = Label(tk, text="Type")
gender.grid(column=0, row=3)
male = Radiobutton(tk, text="Saving", variable=g, command=setVal, value=1)
female = Radiobutton(tk, text="Non Saving", variable=g, command=setVal, value=2)
male.grid(column=1, row=3)
female.grid(column=2, row=3)

age = Label(tk, text="Amount")
age.grid(column=0, row=4)
ageEn = Scale(tk, from_=19, to=30, orient=HORIZONTAL)
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