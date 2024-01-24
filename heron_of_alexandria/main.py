import tkinter 

mw = tkinter.Tk() #initialize main window

mw.title("Heron of Alexandria")
mw.geometry("700x600")
mw.resizable(False, False)

background_image = tkinter.PhotoImage(file = "heron.png")

image_label = tkinter.Label(mw, image = background_image) 
image_label.place(x = -300, y = 0) 

base = tkinter.Label(mw, text='Base',font=("Times", 24 )).grid(column=1)
height = tkinter.Label(mw, text='Height', font=("Times", 24 )).grid(column=0)




mw.mainloop()