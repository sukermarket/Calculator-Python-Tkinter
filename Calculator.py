from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
from tkinter import messagebox
import math

window=ThemedTk(theme='arc')
window.configure(themebg="arc")
window.title('Calculator')
window.geometry('360x426')
var=StringVar()
result=''

def clear():
    global result
    result=""
    var.set("")
def equal():
    try:
        global result
        total=str(eval(result))
        var.set(total)
        result=""
    except:
        var.set('error')
        result=''

def press(num):
    global result
    result=result+str(num)
    var.set(result)

textbox=ttk.Entry(window,width=15,font=('tahoma',32),text=var)
textbox.grid(column=0,row=0,columnspan=4,rowspan=2)

button1=ttk.Button(window,text='C',command=clear)
button1.grid(column=0,row=2,ipady=20, ipadx=3)
button2=ttk.Button(window,text='√',command=lambda: press('math.sqrt('))
button2.grid(column=1,row=2,ipady=20, ipadx=3)
button3=ttk.Button(window,text='(',command=lambda: press('('))
button3.grid(column=2,row=2,ipady=20, ipadx=3)
button4=ttk.Button(window,text=')',command=lambda: press(')'))
button4.grid(column=3,row=2,ipady=20, ipadx=3)

button5=ttk.Button(window,text='7',command=lambda: press(7))
button5.grid(column=0,row=3,ipady=20, ipadx=3)
button6=ttk.Button(window,text='8',command=lambda: press(8))
button6.grid(column=1,row=3,ipady=20, ipadx=3)
button7=ttk.Button(window,text='9',command=lambda: press(9))
button7.grid(column=2,row=3,ipady=20, ipadx=3)
button8=ttk.Button(window,text='x',command=lambda: press('*'))
button8.grid(column=3,row=3,ipady=20, ipadx=3)

button9=ttk.Button(window,text='4',command=lambda: press(4))
button9.grid(column=0,row=4,ipady=20, ipadx=3)
button10=ttk.Button(window,text='5',command=lambda: press(5))
button10.grid(column=1,row=4,ipady=20, ipadx=3)
button11=ttk.Button(window,text='6',command=lambda: press(6))
button11.grid(column=2,row=4,ipady=20, ipadx=3)
button12=ttk.Button(window,text='-',command=lambda: press('-'))
button12.grid(column=3,row=4,ipady=20, ipadx=3)

button13=ttk.Button(window,text='1',command=lambda: press(1))
button13.grid(column=0,row=5,ipady=20, ipadx=3)
button14=ttk.Button(window,text='2',command=lambda: press(2))
button14.grid(column=1,row=5,ipady=20, ipadx=3)
button15=ttk.Button(window,text='3',command=lambda: press(3))
button15.grid(column=2,row=5,ipady=20, ipadx=3)
button16=ttk.Button(window,text='+',command=lambda: press('+'))
button16.grid(column=3,row=5,ipady=20, ipadx=3)

button17=ttk.Button(window,text='0',command=lambda: press(0))
button17.grid(column=0,row=6,ipady=20, ipadx=3)
button18=ttk.Button(window,text='÷',command=lambda: press("/"))
button18.grid(column=1,row=6,ipady=20, ipadx=3)
button19=ttk.Button(window,text='.',command=lambda: press('.'))
button19.grid(column=2,row=6,ipady=20, ipadx=3)
button20=ttk.Button(window,text='=',command=equal)
button20.grid(column=3,row=6,ipady=20, ipadx=3)

username=ttk.Label(text="© @Sukermarket",font=("Helvetica",12, "bold"))
username.grid(column=0,columnspan=2,row=7)





window.mainloop()