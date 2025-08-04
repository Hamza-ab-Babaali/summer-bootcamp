from tkinter import *
windows=Tk()

windows.title("hello hamza")
windows.configure(background="light green")
windows.geometry(1000*1100)


button1 = Button(windows, text=' 1 ', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0) 
 
button2 = Button(windows, text=' 2 ', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
button2.grid(row=2, column=1)

button3 = Button(windows, text=' 3 ', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
button3.grid(row=2, column=0) 
 
button4 = Button(windows, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
button4.grid(row=2, column=1)

button5 = Button(windows, text=' 5 ', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
button5.grid(row=2, column=0) 
 
button6 = Button(windows, text=' 6 ', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
button6.grid(row=2, column=1)


windows.mainloop()
