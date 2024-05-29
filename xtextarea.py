#text widget=functions lika a text area,you can enter multiples lines of text 

from tkinter import *




def submit():
    input=text.get("1.0",END)


    print(input)
window=Tk()


text=Text(window,bg="lightyellow")


button=Button(window,text="submit",command=submit,
                          font=("Ink Free",25),
                          height=0,
                           width=20,
                           padx=20,
                           pady=20,
                           fg="purple"
              
                           )

button.pack()

text.pack()



window.mainloop()