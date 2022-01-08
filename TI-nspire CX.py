# 'pip install tkinter' won't work anymore since tkinter comes defaulted in every python installation
# tkinter will still be used.

from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background ="red")
root.resizable(width =False, height =False)
root.geometry("480x568+0+0")

class Calc():
    def __init__(self):
        self.total =0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self. result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    

added_value = Calc()

# the frame is based of the root. function which is equal to Tk
calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial',20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")
# ^ previous line allows the first symbol on the calc to be a '0'

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width =6, height =2, font=('arial', 20, 'bold'), bd =4, text =numberpad[i]))
        btn[i].grid(row =j, column =k, pady =1)
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i +=1

# =========================================Standard Calculator===================================================

btnClear = Button(calc, text="C", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =1, column =0, pady =1)
btnAllClear = Button(calc, text="CE", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =1, column =1, pady =1)
btnSq = Button(calc, text="√", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =1, column =2, pady =1)
btnAdd = Button(calc, text="+", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.operation("add")).grid(row =1, column =3, pady =1)
btnSub = Button(calc, text="-", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.operation("sub")).grid(row =2, column =3, pady =1)
btnMul = Button(calc, text="*", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.operation("multi")).grid(row =3, column =3, pady =1)
btnDiv = Button(calc, text="÷", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.operation("divide")).grid(row =4, column =3, pady =1)
btnZer = Button(calc, text="0", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.numberEnter(0)).grid(row =5, column =0, pady =1)

btnDot = Button(calc, text=".", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue", command = lambda: added_value.numberEnter(".")).grid(row =5, column =1, pady =1)
btnPM = Button(calc, text="±", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =2, pady =1)
btnEq = Button(calc, text="=", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =3, pady =1)

# ================================== Scientific Calculator =============================================
btnEq = Button(calc, text="=", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =3, pady =1)
btnEq = Button(calc, text="=", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =3, pady =1)
btnEq = Button(calc, text="=", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =3, pady =1)
btnEq = Button(calc, text="=", width =6, height =2, font=('arial', 20, 'bold'), bd =4,
                  bg ="powder blue").grid(row =5, column =3, pady =1)


# =========================MENU and Function============================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")


root.config(menu=menubar)
root.mainloop()


