from tkinter import *

cal = Tk()
cal.title('Simple Calculator')
cal.geometry('330x540')
cal.config(background='white')

expression = ""
def show(key):
    global expression
    expression = expression + str(key)
    Text_box.config(text = expression)
def clear():
    global expression
    expression =""
    Text_box.config(text=expression)

def evaluate ():
    global expression
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = 'error'

    Text_box.config(text = result)


Text_box = Label(cal, text = '', width= '15',height='2',font=('Arial',28),bg='white')
Text_box.place(x = 0, y = 0)
btn_clear = Button(cal,command=lambda :clear(), text= 'C', width=3, height=1, font=('Arial',30),background='red')
btn_clear.place(x = 0 ,y = 95)
btn_percent = Button(cal,command=lambda :show('%'), text = '%', width= 3, height=1 ,font=('Arial',30),background='orange')
btn_percent.place(x= 85, y =95)
btn_division = Button(cal,command=lambda :show('/'), text= '/', width= 3 , height= 1, font=('Arial',30), background='orange')
btn_division.place (x=170 ,y= 95)
btn_multiplication = Button(cal,command=lambda :show('*') ,text='*', width=3  , height=1, font=('Arial',30),background='orange')
btn_multiplication.place(x =255 , y= 95)

btn_7 = Button(cal,command=lambda :show('7'), text= '7', width=3, height=1, font=('Arial',30),background='aqua')
btn_7.place(x = 0 ,y = 180)
btn_8 = Button(cal,command=lambda :show('8'), text = '8', width= 3, height=1 ,font=('Arial',30),background='aqua')
btn_8.place(x= 85, y =180)
btn_9 = Button(cal,command=lambda :show('9'), text= '9', width= 3 , height= 1, font=('Arial',30), background='aqua')
btn_9.place (x=170 ,y= 180)
btn_sub= Button(cal,command=lambda :show('-') ,text='-', width=3  , height=1, font=('Arial',30),background='orange')
btn_sub.place(x =255 , y= 180)

btn_4 = Button(cal,command=lambda :show('4'), text= '6', width=3, height=1, font=('Arial',30),background='aqua')
btn_4.place(x = 0 ,y = 270)
btn_5 = Button(cal,command=lambda :show('5'), text = '5', width= 3, height=1 ,font=('Arial',30),background='aqua')
btn_5.place(x= 85, y =270)
btn_6 = Button(cal,command=lambda :show('6'), text= '4', width= 3 , height= 1, font=('Arial',30), background='aqua')
btn_6.place (x=170 ,y= 270)
btn_add = Button(cal,command=lambda :show('+'), text='+', width=3  , height=1, font=('Arial',30),background='orange')
btn_add.place(x =255 , y= 270)

btn_1 = Button(cal,command=lambda :show('1'),text= '1', width=3, height=1, font=('Arial',30),background='aqua')
btn_1.place(x = 0 ,y = 360)
btn_2 = Button(cal,command=lambda :show('2'), text = '2', width= 3, height=1 ,font=('Arial',30),background='aqua')
btn_2.place(x= 85, y =360)
btn_3 = Button(cal,command=lambda :show('3'), text= '3', width= 3 , height= 1, font=('Arial',30), background='aqua')
btn_3.place (x=170 ,y= 360)
btn_equal = Button(cal,command=lambda :evaluate(), text='=', width=3  , height=3, font=('Arial',30),background='orange')
btn_equal.place(x =255 , y= 360)

btn_0 = Button(cal, command=lambda :show('0'),text= '0', width=3, height=1, font=('Arial',30),background='aqua')
btn_0.place(x = 0 ,y = 450)
btn_open = Button(cal,command=lambda :show('('), text = '(', width= 3, height=1 ,font=('Arial',30),background='aqua')
btn_open.place(x= 85, y =450)
btn_close = Button(cal,command=lambda :show(')'), text= ')', width= 3 , height= 1, font=('Arial',30), background='aqua')
btn_close.place (x=170 ,y= 450)


cal.mainloop()
