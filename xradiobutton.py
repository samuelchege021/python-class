#radiobutton=similiar tocheckbox,but yiou can only select one frpm a grou
from tkinter import *
from PIL import ImageTk
from PIL import Image as img
  




food=["pizza","hamburger","hotdog"]


def order ():
   if (x.get()==0):
      print("you orderd pizza")
   elif(x.get()==1):
      print("you ordered a hamburger")

   elif(x.get()==2):
    print('you orderd a hotdog')


   else:
      print("huh")
window=Tk()
pizzaImage=img.open("pizza.jpeg")
pizzaImage= ImageTk.PhotoImage(img.open("pizza.jpeg"))  # PIL solution

hamburgerImage=img.open("hamburger.jpeg")
hamburgerImage=ImageTk.PhotoImage(hamburgerImage)

hotdogImage=img.open("hotdog.jpeg")
hotdogImage=ImageTk.PhotoImage(hotdogImage)

foodImages=[pizzaImage,hamburgerImage,hotdogImage]
x=IntVar()

for index in range (len(food)):
   radiobutton=Radiobutton(window,text=food[index],#text to radibutton
                           variable=x,   #group the radio button if they share the same variable
                           value=index,    #assing each radio button a differnt value
                           padx=25, # add more radi button   #adds padding on x-axis
                           font="impact,50",
                           image=foodImages[index],
                           compound="left",
                           indicatoron=0,   #eliminate circle indicator
                           width=375,
                           command=order  #set command of radiobutton to function
                           )
       #set width radiobutton
   
   
   
   
   
   
   
   
   #radiobutton.config()#comments
   #radiobutton.config()
  # radiobutton.config()







   radiobutton.pack(anchor=(W))#wesst
window.mainloop()