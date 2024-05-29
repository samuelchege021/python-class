#canvas=widget that is used to draw graphs,plots,images in a window


from tkinter import *


window=Tk ()

canvas= Canvas(window,height=500,width=500)

#canvas.create_line(0,0,500,500,fill="blue",width=5)
#canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(0,0,250,250,fill="blue",width=5)
canvas.create_polygon(250,0,500,500,0,500,fill="yellow",width=5)


canvas.pack()

window.mainloop()