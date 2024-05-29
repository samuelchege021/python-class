from tkinter import *

from tkinter .ttk import *

import time
def start ():
   # tasks=10
    GB=50
    #x=0
    download=0
    speed=2
   # while(x<tasks):
    while(download<GB):
      time.sleep(0.05)
    #  bar["value"]+=10
      bar["value"]+=(speed/GB)*100
     # x+=1
      #x+=1
      download=+1
      Percent.set(str(int(download/GB)*100)+"%")
      text.set(str(download)+"/"+str(GB)+"GB completed ")
      window.update_idletasks()
window=Tk()



Percent=StringVar()
text=StringVar()
button=Button(window,text="download",command=start).pack()

bar=Progressbar(window,orient=HORIZONTAL,length=300)   #vertical
bar.pack(pady=10)

Percentlabel=Label(window,textvariable=Percent).pack()

tasklabel=Label(window,textvariable=text).pack()
window.mainloop()