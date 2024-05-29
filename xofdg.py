from tkinter import *
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\Desktop\\textfile",
                                        
                                    title="open file okay?",
                                    filetypes=(("text files","*.txt"),   #* extension
                                    ("all files","*,*")))
    file=open(filepath,"r")  #or rt
    print(file.read())
    file.close()
window=Tk()



button=Button(text="open",command=openFile)
button.pack()


window.mainloop()