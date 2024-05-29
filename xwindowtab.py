from tkinter import *
from tkinter import ttk   #tab come from notebook ,so we had to import anther module





window=Tk()

notebook=ttk.Notebook(window)  #widget that maneges a collection of windows/dispalys 

tab1=Frame(notebook) #new frame for tab 1
tab2=Frame(notebook)
notebook.add(tab1,text="tab1")
notebook.add(tab2,text="tab 2")
notebook.pack(expand=True,fill="both")#expand=expand to fill the space not otherwise used 
                          #fill   spoace on x and y
Label(tab1,text="hello,this is tab#1",width=50,height=25).pack()
Label(tab2,text="goodbye,this tab#2",width=50,height=25).pack()



window.mainloop()