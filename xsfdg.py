from tkinter import *

from tkinter import filedialog

def saveFile():
    file=filedialog.asksaveasfile(initialdir="C:\\Users\\Admin\\Desktop\\textfile",defaultextension=".txt",
                                filetypes=[("Text file",".txt"),
                                           ("Html file",".html"),
                                           ("All files", ".*"),
                                           ("Pngfile","png")])
                            
   
    #filetext=str(text.get(1.0,END))
    filetext=input("enter some text i guiess") 
    file.write(filetext)
    file.close()
   
    #print(file)
window=Tk()

button=Button(window,text="save",command=saveFile)

text=Text(window)
text.pack()
button.pack()


window.mainloop()
