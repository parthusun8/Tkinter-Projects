from tkinter import *
import tkinter.messagebox as Message

root = Tk()
root.geometry("400x500")

error = Label(root, text="", width=40, justify=CENTER)


def showMsg():
    if cb.get() == 1:
        text = "Name : " + name_e.get() + "\n" + "Email : " + email_e.get() + "\n" + "Gender : " + ("Female" if g.get() == 1 else "Male" if g.get() == 2 else "Others")
        print(text)
        Message.showinfo("message", text)
    elif cb.get() == 0:
        error.config(text="Accept Terms and Condition")


name = Label(root, text="Full Name")
email = Label(root, text="Email")
passw = Label(root, text="Password")
name_e = Entry(root, bd=1)
email_e = Entry(root, bd=1)
pass_p = Entry(root, bd=1, show="*")
frame2 = LabelFrame(root, text="Gender")
g = IntVar()
m = Radiobutton(frame2, text="Female", value=1, variable=g)
f = Radiobutton(frame2, text="Male", value=2, variable=g)
o = Radiobutton(frame2, text="Others", value=3, variable=g)

cb = IntVar()
accept = Checkbutton(root, text="Accept the terms and conditions", onvalue=1, offvalue=0, variable=cb)

btn = Button(root, text="submit", command=showMsg)

name.grid(row=0, column=0)
email.grid(row=1, column=0)
passw.grid(row=2, column=0)
name_e.grid(row=0, column=1)
email_e.grid(row=1, column=1)
pass_p.grid(row=2, column=1)
frame2.grid(row=3, column=1)
m.grid(row=1, column=1)
f.grid(row=2, column=1)
o.grid(row=3, column=1)
accept.grid(row=4, column=1)
btn.grid(row=5, column=1)
error.grid(row=6, column=0, columnspan=2, pady=12)

root.mainloop()
