import time

print(time.ctime(1000000))  #=conevrt a time expressed in seconds since epoch ato a readable string
        #epoch when your ceiomputre thinks time began(reference time)


print (time.time())   #RETURN CURRENT seconds since epoch using computer clock


print(time.ctime(time.time()))

time_object=time.localtime() #locatime
time_object=time.gmtime()#utc time
print(time_object)

local_time=time.strftime("%B %d %Y %H:%M:%S",time_object)   #visit timemodule

print(local_time)




time_string="20 April, 2020"
time_object=time.strptime(time_string,"%d %B, %Y")

#print(time_object)



#(year,month,day,hours,minutes,secs,#day of the week,#day of the year,dst)

time_tuple=(2020,4,20,4,20,0,0,0,0)
time_string=print(time_string)
print(time_string)


#threading
#thread = a floow of execution like  order of instrucr=tions.
 #however each thread takes a turn ruinning to achieve concurrency.

#Gil=(Global interpretor lock)
#allows only one thread to hold the control iof the python intepretor

#cpu bound =program/task spends most of iots tine waiting for internal events..(cpu intensive)
#() use multiproccessing)

#io bound=program /tasks spend s most of its time waiting for external events (USER input,webscraping)
      #use multithreading


import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")
def drink_coffe():
   time.sleep(4)
   print("you drink coffe")
def study():
    time.sleep(5)
    print("yiu finish studying")

#eat_breakfast()
#drink_coffe()
 #study()


x=threading.Thread(target=eat_breakfast,args=())
x.start()
y=threading.Thread(target=drink_coffe,args=())
y.start()

z=threading.Thread(target=study,args=())
z.start()


x.join    #thread sycronization
y.join()
z.join()
print(threading.active_count())
print(threading.enumerate())



print(time.perf_counter())



#deamon threaad==a thread that runs in the background ,not importantrw for program to run your progeam will not wait for deamon threads to complete before exiting 

#non deamon thread cannot normallly be killed,stay alive until task is complete 

#e.g background tasks,garbagecollections ,waitiing for input,long running proccess


import threading
import time

#def timer():
   # count=0
   # while True:
        #time.sleep(1)
        #count+=1
        #print("loogged in for :",count,"seconds")

#x=threading.Thread(target=timer,deamon=True)
#x.start()

#x.setDeamon(True)
#print(x.isDeamon())

#answer=input("do you wish to exist")





#multiproccessing=in parallel on different cpu cores ,bypasses gIL FOR THREAD 

#MULTIPRIOCCESSING=better for cpu bound tasks(heavy cpu usage)

#multithreading =better  for io bound tasks(waiting around)



from multiprocessing import Process,cpu_count
import time



def counter(num):

    count=0

    while count<num:
        count+=1


def  main():



    print(cpu_count())
    a=Process(target=counter,args=(2500000000,))
    b=Process(target=counter,args=(2500000000,))
    c=Process(target=counter,args=(2500000000,))
    d=Process(target=counter,args=(2500000000,))


    a.start()
    b.start()
    c.start()
    d.start()

    a.join()     #sychronization
    b.join()
    c.join()
    d.join()


    print("finished in:",time.perf_counter() ,"seconds")
 
if __name__=="__main__":
    main()