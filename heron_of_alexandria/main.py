import tkinter 

mw = tkinter.Tk() #initialize main window

mw.title("Heron of Alexandria")
mw.geometry("700x600")
mw.resizable(False, False)

background_image = tkinter.PhotoImage(file = "heron.png")

image_label = tkinter.Label(mw, image = background_image) 
image_label.place(x = -250, y = 0) 

base = tkinter.Label(mw, text='Base', bg="#ffffff",font=("Kozuka Mincho Pro R", 13 )).grid(column=0, padx=(400, 10), pady=(150,10))
height = tkinter.Label(mw, text='Height', bg="#ffffff", font=("Kozuka Mincho Pro R", 13 )).grid(row=1, column=0, padx=(400, 10), pady=(10,10))

e1 = tkinter.Entry(mw)
e2 = tkinter.Entry(mw)

e1.grid(row=0, column=1, pady=(150,10))
e2.grid(row=1, column=1)

print(e1.get())










mw.mainloop()