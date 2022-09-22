from tkinter import ttk
from tkinter import *

root = Tk()
phone_list = ttk.Style()
tree = ttk.Treeview(root, column=("Name", "Phone"), show='headings', height=5)


def add():
    tree.insert('', 'end', values=(name.get(), phn.get()))
    name.delete(0, END)
    phn.delete(0, END)


def delete():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)


def edit():
    selected_item = tree.selection()[0]
    tree.item(selected_item, values=(name.get(), phn.get()))


Label(root, text="Name").grid(row=0, column=0)
name = Entry(root)
name.grid(row=0, column=1)
Label(root, text="Phone").grid(row=1, column=0, pady=15)
phn = Entry(root)
phn.grid(row=1, column=1, pady=15)

Button(root, text="Add", command=add).grid(row=2, column=0, pady=15)
Button(root, text="Update", command=edit).grid(row=2, column=1, pady=15)
Button(root, text="Delete", command=delete).grid(row=2, column=2, pady=15)

scroll_bar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=tree.yview)
scroll_bar.grid(row=3, column=3, sticky="nsew", pady=15)

tree.configure(yscrollcommand=scroll_bar.set)

tree.column("#1", anchor=CENTER)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Phone")

tree.insert('', 'end', values=('Test Name', '8582815659'))
tree.insert('', 'end', values=('Parth Sundarka', '7894561238'))
tree.insert('', 'end', values=('Aditya Pathak', '7854962315'))
tree.insert('', 'end', values=('Rishi Pratap', '1584965863'))
tree.insert('', 'end', values=('Mahek Kamani', '7586324561'))
tree.insert('', 'end', values=('Maharanav Pulsar', '7578324561'))
tree.insert('', 'end', values=('Srijan Chakraborty', '7578326561'))

tree.grid(row=3, columnspan=3, pady=15)
root.mainloop()
