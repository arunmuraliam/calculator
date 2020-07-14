from tkinter import *



root = Tk()
root.title("Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("416x550+469+60")   #set the size of frame

#=================================== creating a frame  ==================================================

calc = Frame(root, bd=20, pady=5, bg="gainsboro", relief=RIDGE)
calc.grid()



#============================= Entry widget is created ===================================================

txtDisplay = Entry( calc, font=('arial', 16, 'bold'), bd=20, width=28,justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)
txtDisplay.bind("<Key>", lambda e : "break")  # disable characters from keyboard
txtDisplay.insert(0, "0")

#====================================== All Buttons are added ==============================================

# Buttons for Number

numberpad = "789456123"

i = 0
btn = []

for j in range(3,6):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',16,'bold'), bd=4,bg='white', text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)

        i += 1


# Buttons for operations

# ==============================================================================================================

btnDelete=Button(calc,text="DEL",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=1,column=0,pady=1)

btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=1,column=1,pady=1)

btnClearAll=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=1,column=2,pady=1)

btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=1,column=3,pady=1)

#================================================================================================================

btnSq=Button(calc,text="√",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=2,column=0,pady=1)

btnCos=Button(calc,text="cos",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=2,column=1,pady=1)

btnTan=Button(calc,text="tan",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=2,column=2,pady=1)

btnSin=Button(calc,text="sin",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=2,column=3,pady=1)

#================================================================================================================

btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=3,column=3,pady=1)

btnSub=Button(calc,text="-",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=4,column=3,pady=1)

btnMult=Button(calc,text="*",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=5,column=3,pady=1)

btnDiv=Button(calc,text="/",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="gainsboro").grid(row=6,column=3,pady=1)

#================================================================================================================

btnZero=Button(calc,text="0",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="white").grid(row=6,column=0,pady=1)

btnDot=Button(calc,text=".",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="white").grid(row=6,column=1,pady=1)

btnEquals=Button(calc,text="=",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light grey").grid(row=6,column=2,pady=1)


root.mainloop()