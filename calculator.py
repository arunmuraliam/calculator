from tkinter import *



root = Tk()
root.title("Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("416x550+469+60")   #set the size of frame

# creating a frame
calc = Frame(root, bd=20, pady=5, bg="gainsboro", relief=RIDGE)
calc.grid()



# entry widget is created
txtDisplay = Entry( calc, font=('arial', 16, 'bold'), bd=20, width=28,justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)
txtDisplay.bind("<Key>", lambda e : "break")  # disable characters from keyboard
txtDisplay.insert(0, "0")


root.mainloop()