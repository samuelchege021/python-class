#Gui.
#graphical user interface

#tkinter
from tkinter import  *

window = Tk()  # Instantiate an instance of a window
window.geometry("420x420")  # Set window size
window.title("samido first Gui program")

icon=PhotoImage(file="cute.png")
window.iconphoto(True,icon)
window.config(background="black") #hexcolorpacker

window.mainloop()  # Place window on the computer screen, 