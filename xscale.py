from tkinter import*

def submit():
    print("the temperature is:"+str(scale.get())+"degree c") 
window=Tk()

hotImage=PhotoImage(file="cute.png")
hotlabel=Label(image=hotImage)
hotlabel.pack()
scale=Scale(window,from_=0, to= 1000,
            length=600,
            orient=VERTICAL,#orientationof scale  
             font=( "consoles",20),
             tickinterval=10,
             #showvalue=0
             resolution=5 ,#increment of slider
             troughcolor="#69EAFF",
             fg="#FF1C00",
             bg="#111111"
)



#scale.set(((scale["from"]-scale["t0"])/2)+scale["to"])
scale.pack()

button=Button(window,text="submit",command=submit)
button.pack()


window.mainloop()
