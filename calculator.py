from tkinter import *



root = Tk()
root.title("Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("416x550+469+60")
calc = Frame(root, bd=20, pady=5, bg="gainsboro", relief=RIDGE)
calc.grid()


root.mainloop()