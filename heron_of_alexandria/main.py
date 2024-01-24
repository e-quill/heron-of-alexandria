import tkinter 

mw = tkinter.Tk()

mw.title("Heron of Alexandria")
mw.geometry("700x600")

bg = tkinter.PhotoImage(file = "heron.png")

label1 = tkinter.Label(mw, image = bg) 
label1.place(x = -300, y = 0) 

mw.mainloop()