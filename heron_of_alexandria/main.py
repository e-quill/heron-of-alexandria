import tkinter 
import logic
from tkinter import messagebox
    
def show_dialog():
  numbers = "0123456789"
  for character in base_entry.get():
    if character not in numbers:
      messagebox.showerror("Error", "Input not in integers.")
  for character in height_entry.get():
    if character not in numbers:
      messagebox.showerror("Error", "Input not in integers.")
  
  area = logic.area_of_triangle(int(base_entry.get()),int(height_entry.get()))
  messagebox.showinfo("Area",f"The Area of the Triangle is {area} units.")
  
mw = tkinter.Tk() #initialize main window

mw.title("Heron of Alexandria")
mw.geometry("700x600")
mw.resizable(False, False)

background_image = tkinter.PhotoImage(file = "heron.png")

background_image_label = tkinter.Label(mw, image = background_image) 
background_image_label.place(x = -250, y = 0) 

base = tkinter.Label(mw, text='Base:', bg="#ffffff",font=("Kozuka Mincho Pro R", 13 )).grid(column=0, padx=(400, 10), pady=(150,10))
height = tkinter.Label(mw, text='Height:', bg="#ffffff", font=("Kozuka Mincho Pro R", 13 )).grid(row=1, column=0, padx=(400, 10), pady=(10,10))

base_entry = tkinter.Entry(mw)
height_entry = tkinter.Entry(mw)

base_entry.grid(row=0, column=1, pady=(150,10))
height_entry.grid(row=1, column=1)

calculate_button = tkinter.Button(mw, text='Calculate Area', command=show_dialog).grid(row=3, column=1, sticky=tkinter.W, pady=4)

mw.mainloop()