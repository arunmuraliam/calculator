from tkinter import *



root = Tk()
root.title("Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("416x550+469+60")   #set the size of frame

#=================================== creating a frame  ==================================================

calc = Frame(root, bd=20, pady=5, bg="light gray", relief=RIDGE)
calc.grid()


#=================================== Functions Added =====================================================


class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self,num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)


        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)


    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum ==True :
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current

        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not  self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def clear_Entry(self):
        self.result=False
        self.current=0
        self.display(0)
        self.input_value=True

    def all_CLear_Entry(self):
        self.clear_Entry()
        self.total=0

    def delectBS(self):
        numLen=len(txtDisplay.get())
        txtDisplay.delete(numLen-1,'end')
        if numLen==0:
            txtDisplay.insert(0,"0")

    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)


added_value = Calculator()
#============================= Entry widget is created ===================================================

txtDisplay = Entry( calc, font=('arial', 16, 'bold'), bd=20, width=28,justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)
txtDisplay.insert(0, "0")

#======================================  Buttons are added ==============================================

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

btnDelete=Button(calc,text="DEL",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=1,column=0,pady=1)

btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=1,column=1,pady=1)

btnClearAll=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=1,column=2,pady=1)

btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=1,column=3,pady=1)

#================================================================================================================

btnSq=Button(calc,text="√",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=2,column=0,pady=1)

btnCos=Button(calc,text="cos",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=2,column=1,pady=1)

btnTan=Button(calc,text="tan",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=2,column=2,pady=1)

btnSin=Button(calc,text="sin",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=2,column=3,pady=1)

#================================================================================================================

btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=3,column=3,pady=1)

btnSub=Button(calc,text="-",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=4,column=3,pady=1)

btnMult=Button(calc,text="*",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=5,column=3,pady=1)

btnDiv=Button(calc,text="/",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light gray").grid(row=6,column=3,pady=1)

#================================================================================================================

btnZero=Button(calc,text="0",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="white").grid(row=6,column=0,pady=1)

btnDot=Button(calc,text=".",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="white").grid(row=6,column=1,pady=1)

btnEquals=Button(calc,text="=",width=6,height=2,font=('arial',16,'bold'),bd=4,bg="light grey").grid(row=6,column=2,pady=1)


root.mainloop()