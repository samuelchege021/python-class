#label =an area widget that hold text and/or an image within a window


from tkinter import *
window=Tk()
photo=PhotoImage(file="C:\\Users\\Admin\\Desktop\\cute.png")
label=Label(window,text="hello world",font=("Arial",40,
                                            "bold"),
                                            fg="green",
                                            bg="black",
                                            relief=RAISED,
                                            bd=10,
                                            padx=20,
                                            pady=20,
                                            image=photo,
                                            compound="bottom"
                                        )    #hex #fg=foreground bg=backgroundcolor padx=paddling
label.pack()
#label.place(x=0,y=0)

window.mainloop()



