
from tkinter import*
#button =you click,then it does stuff
count=0

def click():
    global count
    count+=1
    print(count)
    print("you clicked the button!")

window=Tk()
photo=PhotoImage(file="thum.png")

button=Button(window,#master is the window used to display the button
              text="click me!",
              command=click,
              font=("comic sans",30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00",
              activebackground="black",
              state=ACTIVE,
              image= photo,
              compound="bottom"
                             #DISABLED
              ) 
button.pack()
window.mainloop()