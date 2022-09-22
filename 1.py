from tkinter import *
import tkinter

root = Tk()

root.config(bg='red')

def p():
    val = radio_1.get()
    val1 = n_e.get()
    print(val, val1)


l = Label(root, text="Name", bg="red")
l.grid()
n_e = Entry(root, bg="red")
n_e.grid(row=0, column=1)

radio_1 = IntVar()
r1 = Radiobutton(root, text="Male", variable=radio_1, value=1, command=p, bg="red")
r2 = Radiobutton(root, text="Female", variable=radio_1, value=2, command=p, bg="red")

# tk.
r1.grid(row=1, column=0)
r2.grid(row=1, column=1)

check_1 = IntVar()
check_2 = IntVar()
c1 = Checkbutton(root, text="Slot1", variable=check_1, onvalue=1, offvalue=0, bg="red")
c2 = Checkbutton(root, text="Slot2", variable=check_2, onvalue='M', offvalue=0, bg="red")
c1.grid(row=2, column=0)
c2.grid(row=2, column=1)

spin = Spinbox(root, from_=10, to=20, bg="red")
spin.grid(row=3, column=0)

scale = Scale(root, from_=10, to=20, bg="red", orient=HORIZONTAL)
scale.grid(row=3, column=1)
root.mainloop()

