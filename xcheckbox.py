from tkinter import*

#checkboxe or check button

window=Tk()
def display():
    if(x.get())==1:
        print("you agred")
    else:
        print("you dont agree") 

python_photo= PhotoImage(file="python.png")
x=IntVar()

check_button =Checkbutton(window,text="i agree with something",
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command=display,
                          font=("Arial",20),
                          fg="#00FF00",
                          bg="black",
                          activeforeground="#00FF00",
                          activebackground="black",
                          padx=25,
                          pady=10,
                          compound=LEFT,
                          image=python_photo,
)
check_button.pack()

window.mainloop()


