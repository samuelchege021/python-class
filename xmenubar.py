from tkinter import *


def openFile():
    print("file has been opened")



def saveFile():
    print("file has been saved")


def exitFile():
    print("file has been existed")



def cut():
    print("you cut some text")  



def copy() :
    print("you have copied some text") 





def paste():
    print("you have paste some text")


















window=Tk()





openImage=PhotoImage(file="open.png")
saveImage=PhotoImage(file="save.png")
exitImage=PhotoImage(file="exit.png")

menuBar=Menu(window)

window.config(menu=menuBar)

filemenu=Menu(menuBar,tearoff=0,font=("my Boli",15))

menuBar.add_cascade(label="File",menu=filemenu)



filemenu.add_command(label="open",command=openFile,image=openImage,compound="left")
filemenu.add_command(label="save",command=saveFile,image=saveImage,compound="left")
filemenu.add_command(label="Exit",command=exitFile, image=exitImage,compound="left")
filemenu.add_separator()


editmenu=Menu(menuBar,tearoff=0,font=("MV BOLI",15))
menuBar.add_cascade(label="Edit",menu=editmenu)


editmenu.add_command(label="cut",command=cut)

editmenu.add_command(label="copt",command=copy)

editmenu.add_command(label="paste",command=paste)
window.mainloop()