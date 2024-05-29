from tkinter import *
from tkinter import colorchooser    #submodule

def click():
   #color= colorchooser.askcolor()
   #print(color)
  # colorHex=color[1]
   #print(colorHex)

   #window.config(bg=colorHex)
   #or window.config(bg=color[1])
   window.config(bg=colorchooser.askcolor()[1])
   
   
       #change the background color
window=Tk()

window.geometry("420x420")

button=Button(text="clickme",command=click)


button.pack()


window.mainloop()
