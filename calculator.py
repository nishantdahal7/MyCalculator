from tkinter import *


#this is what happens when you click any button
def clickbutton(clicked):
    your_value = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(your_value) + str(clicked))

#this is the result of specifically clicking the clear button
def clearbutton():
    entry.delete(0 , END)

#function for the equal button
def equalbutton():
    try:
        value = str(entry.get())   # this converts the value of entry to string and stores it
        answer = eval(value)  #evaluates the output of the value given
    except:
        answer = "xxx SyntaxError.... xxx"
    finally:
        entry.delete(0, END)  # deletes the value in entry
        entry.insert(0, answer)  # inserts the value of ans in entry




#creating the app window
root = Tk()

#background and app color
root.configure(bg = 'deepskyblue')

#title and icon
root.title('My Calculator')
root.iconbitmap('calcy.ico')







#entry bar
entry = Entry(root, width=20, borderwidth=10, font=('Devanagari MT', 30), fg='red', bg='bisque', )
entry.grid(row=0, column=0, columnspan=5, padx=15, pady=25, ipadx=10, ipady=10)


#Creation of Buttons
but0 = Button(root, text = '0',command =lambda:clickbutton(0), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but00 = Button(root, text = '00',command =lambda:clickbutton(00), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but1 = Button(root, text = '1',command =lambda:clickbutton(1), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but2 = Button(root, text = '2',command =lambda:clickbutton(2), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but3 = Button(root, text = '3',command =lambda:clickbutton(3), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but4 = Button(root, text = '4',command =lambda:clickbutton(4), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but5 = Button(root, text = '5',command =lambda:clickbutton(5), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but6 = Button(root, text = '6',command =lambda:clickbutton(6), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but7 = Button(root, text = '7',command =lambda:clickbutton(7), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but8 = Button(root, text = '8',command =lambda:clickbutton(8), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')
but9 = Button(root, text = '9',command =lambda:clickbutton(9), font=('Devanagari MT', 25), fg = 'royalblue', bg = 'lavender', activeforeground='white', activebackground='rosybrown')

but_dec = Button(root, text = '.',command =lambda:clickbutton('.'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_add = Button(root, text = '+',command =lambda:clickbutton('+'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_sub = Button(root, text = '-',command =lambda:clickbutton('-'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_mul = Button(root, text = '*',command =lambda:clickbutton('*'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_div = Button(root, text = '÷' ,command =lambda:clickbutton('/'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_power = Button(root, text = '^',command =lambda:clickbutton('**'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_mod = Button(root, text = '%',command =lambda:clickbutton('%'), font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_clear = Button(root, text = 'Clear',command =clearbutton, font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )
but_equal = Button(root, text = '=',command =equalbutton, font=('Devanagari MT', 25), fg = 'aliceblue', bg = 'mediumslateblue' )


#Button Arrangement
but0.grid(row = 5, column = 0, ipadx = 40, ipady = 20)
but00.grid(row = 5, column = 1, ipadx = 31, ipady = 19)
but1.grid(row = 4, column = 0, ipadx = 40, ipady = 20)
but2.grid(row = 4, column = 1, ipadx = 40, ipady = 20)
but3.grid(row = 4, column = 2, ipadx = 40, ipady = 20)
but4.grid(row = 3, column = 0, ipadx = 40, ipady = 20)
but5.grid(row = 3, column = 1, ipadx = 40, ipady = 20)
but6.grid(row = 3, column = 2, ipadx = 40, ipady = 20)
but7.grid(row = 2 , column = 0, ipadx = 40, ipady = 20)
but8.grid(row = 2, column = 1, ipadx = 40, ipady = 20)
but9.grid(row = 2, column = 2, ipadx = 40, ipady = 20)

but_dec.grid(row = 5, column = 2, ipadx = 44, ipady = 19)
but_add.grid(row = 3, column = 3, ipadx = 40, ipady = 19)
but_sub.grid(row = 4, column = 3, ipadx = 43, ipady = 20)
but_mul.grid(row = 1, column = 3, ipadx = 42, ipady = 20)
but_div.grid(row = 2, column = 3, ipadx = 40, ipady = 19)
but_power.grid(row = 1, column = 1, ipadx = 42, ipady = 20)
but_mod.grid(row = 1, column = 0, ipadx = 34, ipady = 20)
but_clear.grid(row = 1, column = 2, ipadx = 12, ipady = 20)
but_equal.grid(row = 5, column = 3, ipadx = 39, ipady = 19)



root.mainloop()
