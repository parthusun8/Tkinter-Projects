from tkinter import *


def calculate(x):
    global ans
    ans += x
    print(ans)
    entry.config(text=ans)


def output():
    global ans
    evaluation = str(eval(ans))
    ans = evaluation
    entry.config(text=evaluation)


def clear():
    global ans
    ans = ""
    entry.config(text=ans)


ans = ''
root = Tk()
entry = Label(root, text=ans, font=("Helvetica", 14), anchor="e", width=25)
entry.grid(row=0, column=0, columnspan=10)

k = 1
for i in range(3):
    for j in range(3):
        numbers = Button(root, text=str(k), command=lambda x=str(k): calculate(x), height=3, width=10, bg="white",
                         fg="black")
        numbers.grid(row=i + 2, column=j)
        k += 1

clear = Button(root, text='C', command=clear, height=3, width=10, fg="black", bg="grey").grid(row=1, column=0)
rootOver = Button(root, text='√', command=lambda x='**0.5': calculate(x), height=3, width=10, fg="black",
                  bg="grey").grid(row=1, column=1)
power = Button(root, text='x^y', command=lambda x='**': calculate(x), height=3, width=10, fg="black", bg="grey").grid(
    row=1, column=2)
modulus = Button(root, text='√', command=lambda x='%': calculate(x), height=3, width=10, fg="black", bg="grey").grid(
    row=1, column=3)

zero = Button(root, text='0', command=lambda x='0': calculate(x), height=3, width=10, fg="black", bg="white").grid(
    row=5, column=0)
decimal = Button(root, text='.', command=lambda x='.': calculate(x), height=3, width=10, fg="black", bg="white").grid(
    row=5, column=1)
add = Button(root, text='+', command=lambda x='+': calculate(x), height=3, width=10, fg="black", bg="grey").grid(row=2,
                                                                                                                 column=3)
sub = Button(root, text='-', command=lambda x='-': calculate(x), height=3, width=10, fg="black", bg="grey").grid(row=3,
                                                                                                                 column=3)
mul = Button(root, text='*', command=lambda x='*': calculate(x), height=3, width=10, fg="black", bg="grey").grid(row=4,
                                                                                                                 column=3)
div = Button(root, text='/', command=lambda x='/': calculate(x), height=3, width=10, fg="black", bg="grey").grid(row=5,
                                                                                                                 column=3)

equals = Button(root, text="=", command=output, height=3, width=10, fg="black", bg="orange").grid(row=5, column=2)

root.mainloop()
