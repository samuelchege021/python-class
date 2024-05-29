
from tkinter import *
from tkinter import  messagebox #import message library



def click():
   #messagebox.showinfo(title="This is a info message box",message="you are person")
    
   # messagebox.showwarning(title="warning",message="You have a virus!!!")
 
   # messagebox.showerror(title="Error !",message="something went wrong")
  #if messagebox.askokcancel(title="ask ok cancel",message='do you want to do the thing ?') :
   # print("you did the thing")

 # else:
  #  print("you cancel the thing")
    
   #if messagebox.askretrycancel(title="ask ok cancel",message='do you want to do retry the thing ?') :
     # print("you retried the thing")

   #else:
    # print("you cancel the thing")

    #messagebox.askyesno(title="ask yes or no",)

    #if messagebox.askyesno(title="ask yes or no",message="Do you like cake?"):
     #print("Ilike cake to ")
    #else:
       #print("why do you not like cake")
    


   # answer=messagebox.askquestion(title="askquestion",message="do you  like pie ?")
    #if (answer =="yes"):
       # print("I like pie to")

   # else:
     #   print("why do you not like pie")
    

    answer=messagebox.askyesnocancel(title="yes no cancel",message="do you like to code",icon="error")   #warningicon #info
    if(answer==True):
        print("you like to code")

    elif(answer==False):
        print("Then why are you watching a video on coding")

    else:
        print("you have dodged the question")

    


window= Tk()

button=Button(window,command=click,text="clickme")



button.pack()





window.mainloop()