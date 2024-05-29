from tkinter import *





def create_window():
   # new_window=Toplevel()  #top level=new window on top of other windows,linked to a "bottom" window 
   new_window=Tk()
   
   
   old_window.destroy()

old_window=Tk()


button=Button(old_window,text="create new window",command=create_window).pack()



old_window.mainloop()