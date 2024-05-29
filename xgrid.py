from tkinter import *
import tkinter as tk
root=tk.Tk()



name_var=tk.StringVar()
firstname_var=tk.StringVar()
secondname_var=tk.StringVar()
myemail_var=tk.StringVar()
#grid()=geometry manager that organises widgets in a table like structure in a parent

def submit ():


 firstname=firstname_var.get()
 

 print("my first name is :"+firstname)
 secondname=name_var.get()
 
 print("my second name is :"+secondname)
 Email=myemail_var.get()
 print("my email is :" +Email)

 firstname_var.set("")
 secondname_var.set("")
 myemail_var.set("")
window=Tk() 

titleLabel=Label(window,text="Enter your infor",font=("Arial",25)).grid(row=0,columnspan=2)

firstNameLabel= tk.Label(window,text="firstname :",width=20,bg="red").grid(row=1,column=0)
#name  = Text(window).grid(row=1,column=1)
firstNameEntry=Entry(window).grid(row=1,column=1)
# print(firstNameEntry)
secondnameLabel=Label(window,text="secondname :",bg="blue").grid(row=2,column=0)
secondNameEntry=Entry(window).grid(row=2,column=1)
print(secondNameEntry)                                                                                                                                                                                                                                                                                                                                                                  
EmailLabel=Label(window,text="myemail :",bg="green").grid(row=3,column=0)
Emailentry=Entry(window).grid(row=3,column=1)
print(Emailentry)
submitbutton=Button(window,text="submit",command=submit).grid(row=4,column=0,columnspan=3)
window.mainloop()
