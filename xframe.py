#frame=a rectangular container to group and hold widgets



from tkinter import *

window=Tk()
frame=Frame(window,bg="pink",bd=5,relief=RAISED)
#frame.pack(side="bottom")

frame.place(x=100,y=600)
button=Button(frame,text="w",font=("consolas",25),width=3).pack(side=TOP)
button=Button(frame,text="A",font=("consolas",25),width=3).pack(side=LEFT)
button=Button(frame,text="s",font=("consolas",25),width=3).pack(side=LEFT)
button=Button(frame,text="D",font=("consolas",25),width=3).pack(side=LEFT)


window.mainloop()