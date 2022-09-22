import tkinter
from tkinter import *

root = Tk()
rateVar = StringVar()
paymentsVar = StringVar()
principleVar = StringVar()
monthly_paymentVar = StringVar()
loanVar = StringVar()


root.title("Customer Loan")
root.config(bg="grey")

rate = Label(root, text="Annual Rate : ", width=20, anchor="w",bg="grey").grid(row=0, column=0,padx=8,pady=5)
Entry(root, textvariable=rateVar, width=25).grid(row=0, column=1,pady=5,sticky="E")
payments = Label(root, text="Number of Payments : ", width=20, anchor="w",bg="grey").grid(row=1, column=0,padx=8,pady=5)
Entry(root, textvariable=paymentsVar, width=25).grid(row=1, column=1,pady=5)
principle = Label(root, text="Loan Principle : ", width=20, anchor="w",bg="grey").grid(row=2, column=0,padx=8,pady=5)
Entry(root, textvariable=principleVar, width=25).grid(row=2, column=1,pady=5)
monthly_payment = Label(root, text="Monthly Payment : ", width=20, anchor="w",bg="grey").grid(row=3, column=0,padx=8,pady=5)
Entry(root, textvariable=monthly_paymentVar, width=25).grid(row=3, column=1,pady=5)
loan = Label(root, text="Remaining Loan : ", width=20, anchor="w",bg="grey").grid(row=4, column=0,padx=8,pady=5)
Entry(root, textvariable=loanVar, width=25).grid(row=4, column=1,pady=5)
final = Button(root, text="Final Balance", width=14, height=1,bg="grey").grid(row=6, column=0)
pay_btn = Button(root, text="Monthly Payment", width=14, height=1,bg="grey").grid(row=6, column=1)
quit_btn = Button(root, text="Quit", width=8, height=1,bg="grey").grid(row=6, column=2, padx=10)

root.mainloop()

