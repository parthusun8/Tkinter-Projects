from tkinter import *

root = Tk()
rateVar = StringVar()
paymentsVar = StringVar()
principleVar = StringVar()
monthly_paymentVar = StringVar()
loanVar = StringVar()
email = StringVar()
address = StringVar()


root.title("Registration Form")
root.config(bg="lightgreen")

rate = Label(root, text="Name : ", width=20, anchor="w",bg="lightgreen").grid(row=0, column=0,padx=8,pady=5)
Entry(root, textvariable=rateVar, width=35).grid(row=0, column=1,pady=5,sticky="E")
payments = Label(root, text="Course : ", width=20, anchor="w",bg="lightgreen").grid(row=1, column=0,padx=8,pady=5)
Entry(root, textvariable=paymentsVar, width=35).grid(row=1, column=1,pady=5)
principle = Label(root, text="Semester : ", width=20, anchor="w",bg="lightgreen").grid(row=2, column=0,padx=8,pady=5)
Entry(root, textvariable=principleVar, width=35).grid(row=2, column=1,pady=5)
monthly_payment = Label(root, text="Form No. : ", width=20, anchor="w",bg="lightgreen").grid(row=3, column=0,padx=8,pady=5)
Entry(root, textvariable=monthly_paymentVar, width=35).grid(row=3, column=1,pady=5)
loan = Label(root, text="Contact No. : ", width=20, anchor="w",bg="lightgreen").grid(row=4, column=0,padx=8,pady=5)
Entry(root, textvariable=loanVar, width=35).grid(row=4, column=1,pady=5)
emailId = Label(root, text="Email : ", width=20, anchor="w",bg="lightgreen").grid(row=5, column=0,padx=8,pady=5)
Entry(root, textvariable=email, width=35).grid(row=5, column=1,pady=5)
addressEl = Label(root, text="Address : ", width=20, anchor="w",bg="lightgreen").grid(row=6, column=0,padx=8,pady=5)
Entry(root, textvariable=address, width=35).grid(row=6, column=1,pady=5)
final = Button(root, text="Submit", width=14, height=1,bg="red", justify=CENTER).grid(row=7, column=0, columnspan=2)

root.mainloop()

