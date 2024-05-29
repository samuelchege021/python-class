#variable behave as ac onntainer for a value.


#datatypes
#string is 

name="bro"
#print (name)
first_name="bro"
second_name="code"
full_name=("first_name+ "" +second_name")

#print("HELLO"+full_name)

#integers
age=21
age +=1
#print(age)
#print("your age is : " + str(age))  #typecasting


#float.decimal

height=250.5
#print("your height is :" + str(height) +"cm")#typecasting




#booleaan  #true or false

human=True
#print("are you a human :" +str(human))
#print(type(human))


#multiple assignment,,,aloow to assign multiple variables and same time using one line code



#name="bro"
#age=25
#attractive=True



name,age,attractive="bro","21","True"
print(name)
print(age)
print(attractive)


#spongebob=
#patrick=30
#sandy=30
#squildward=30


spongebob=patrick=sandy=squildward=30
print(spongebob)
print(patrick)
print(sandy)
print(squildward)

#striings method

#methods,tools for string
name="Brocode"
#print(len(name))
print(name.find("o"))
print(name.capitalize())
print (name.lower())
print(name.upper())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*3)



#type casting =convert the data type of a value to another data type


x=1
y=2
z=3

x=str(x)
y=str(y)
z=str(z)

print("x is :" + x)
print("y is : " + y)
print("z is :"+ y)



print(x)
print(y)
print(z*3)


#user input.
#name=(input("what is your name?:"))
#age=int(input("how old are you ? :"))
#height=float(input("how tall are you ? :"))
#age=age+1

#print("hello"+name)
#print("you are "+str(age)+"years old")
#print("you are "+str(height)+"cm tall")







#math function

import math

pi=3.14

print(round(pi))
print (math.ceil(pi))
print(math.floor(pi))

print(abs(pi))
print(pow(pi,2))
print(math.sqrt(49))

x=1
y=2
z=3
print(max(x,y,z))
print (min(x,y,z))

print(x,y,z)





#slicing create a substring by extracting elements from another string

#indexing[] square operators or slice()
#[start:stop:step]

name="bro code"
first_name=name[0:3]
last_name=name[4:8]
funky_name=name[::3]
reversed_name=name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1="http://google.com"   #index count negative from right side
website2="http://wikipedia.com"
slice=slice(7,-4)
print(website1[slice])
print(website2[slice])


         #if statement.execute the code that will be trhue if its condition is tryes.

#age=int(input("how old are you"))
#if age>=100:
    
#  print("you are a century born !")
  
   
#elif age==18: #double equals  
   #  print("you are an adult :")

#elif age<0:
    #print("youn haven't be born yet !")else:
  #print("you are a child !")    





    #logical ioperators.logical operators (and,or,not) =used to check if two or more conditional statements are true.



#temp=int(input("what is the temperature outiside?:"))

#if not(temp>=0 and temp <=30) :
  #  print("the tem is bad today!")
  #  print("stay inside!")
    

#elif  not(temp <0 or temp>30 ):
  #  print("the temp is good today !")
    #print("go outiside!")



    #while loop. a sytemenet that will execute its block of code as long as its condition remains true

    #name=""
    #while len(name)==0:
     #  name=(input("enter name"))
  #  print("hello"+name)


#name="none"
#while len(name)==0:
 #name=(input("enter name"))
 #print("hello"+name)

#for loop  = a statement that will execute its blockof code.
 
 #a limited amount of times
 #while=unlimites
 #for loop=limited

#for i in range(10):
  # print(i+1)

#for i  in range (50,100+1,3):     #inclusive to exclusisive

  # print(i)


#for i in "bro code":
   # print(i)


    #import time

   # for seconds in range (10,0,-1):
       # print (seconds)
        #time.sleep(1)

       # print("happy good friday !")
    
 #nested loop=the inner loop will finish all its iterations before finishing one iteration of the outer loop
    
#rows=int(input("how many rows? :"))
#columns=int(input("how many columns? :"))
#
    #symbol=input("Enter a symbol to use ")

#for i in range (rows):
   #for j in range(columns):
       #print(symbol,end="")
#print()


    #  rows=5
#columns=6
#symbol="$"

#for i in range (rows):
   #for j in range(columns):
    #   print(symbol,end="")
#print()


    
#loop controlstatements =chamgealoops execution fromits normal sequence
#break=used to terminate  trhe loop entirely
#continue=used skips to the next iteration of the loop
#pass=does nothing,acts as a placeholder


#while True:
  # name=input("enter your name")
   #if name!="":
   #   break
   

phone_number="123-456-7890"
for i in phone_number:
   if i =="-":
      continue
print(i,end="")



for i in range (1,21):
 if i ==13:
   pass
else:
  print(i)




  #list.=used to store multtiple inforamation items in a singe variablex
  food=["pizza","hamburger","hotdog","sphaghetti","pudding"]
  food[0]="sushi"
 #print(food[0])
  food.append("icecream")
  food.remove("hotdog")
  food.pop()
  food.insert(0,"cake")
  food.sort()
  #food.clear()

  for x in food:
    print(x)


    #2d list=a list of lists
#multidimensional list
    drinks=["coffe","soda","tea"]
    dinner=["pizzer","hamburger","hotdog"]
    dessert=["cake","icecream"]

    food=[drinks,dinner,dessert]
    print(food[2][1])


#tuple=collection  which is ordered and not unchangeable
      #used to group togetheer related data
    
    student=("sammy",21,"male")
    print(student.count("sammy"))
    print(student.index("male"))


    for x in student:
      print(x)

      if "sammy" in student:
        print("sammy is here")


        #set =collections which is unorderede,unindexed.no duplicate values


utensils={"fork","spoon","knife"}
utensils.add("napkin")
utensils.remove("fork")



dishes={"bowl","plate","cup","knife"}

#disshes.update(utensils)
#dinner_table=utensils.union(dishes)
#for x in dinner_table:
 #print(x)

#print(utensils.difference(dishes))
print(utensils.intersection(dishes))


#dictionary= a changable,unordered collection of uniques key:value pairs fast because they use hashing,allow to acces a value quickly

capitals={"usa":"washngton Dc",
        'india':"newdehl",
        'china':'beijing',
        "russia":"mascow"}


capitals.update({"Germany":"berlin"})
capitals.update({"usa":"lassvaga"})
capitals.pop("china")
#capitals.clear()
#print(capitals['germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
for key,value in capitals.items ():
  print(key,value)
        
      
#index operator []=gives acess to a sequence element (str,list,tuples)
  name="bro code"

  if(name[0].islower()):
    name=name.capitalize()


first_name=name[:3].upper()

last_name=name[4:].lower()
last_character=name[-2]

#print(first_name)

#print(last_name)
#print(last_character)


#function = a block of code which is executed only

def hello(name):   #name is parameter
  print("hello"+name)
  print("have a nice day")

#hello("bro") #bro is an argument
#hello("samidio")

my_name="chege"
#hello(my_name)

def hello(first_name,second_name,age):
  print("hello"+first_name+""+second_name,)
  print("have a wonderful day")
  print("you are "+ str(age)+"years old")



hello("sammy","chege",21)

#RETURN Statemenet=funtions send python values/objects back to the caller.
#these values/oblects are known as teh function return value.

def  multiply(number1,number2 ):
    result=number1*number2
    return result
#print(multiply(6,8))

x=multiply(6,8)
#print(x)


def  multiply(number1,number2 ):
  
    return number1* number2
#print(multiply(6,8))

x=multiply(6,8)
print(x)



#positional argument


#keyword argument=arguments preceded by the indentifier when we passed them to a funtion.The order of the arguments doesnt matter,unlike positional arguments,python knows the names of the arguments that our funtions receives 

def hello(first,middle,last):
  print("hello" "  " +first+ "  "+middle+"  " +last)
  
  
hello(last="code",middle="dude",first="bro")


#nested function call=function calls inside other function calls
#inner most funtion calls are resolved first
#returned value is used as argument for the outer function


#num=input("enter a whole number ")
#num=float(num)
#num=abs(num)
#num=round(num)
#print(num)

#round(abs(float(input=("enter a whole positive number :"))))



#scope=the region that variable is recognized
#variable is only available from inside  the region it is  created.
#global and locally sciped versions of cvariable can be created




name ="bro"              #global scope (availabele inside $outiside the function)
def display_name():
  name="code"                #localscope
  print(name)
                            #legb=local,enclosing,global,built-in
display_name()
print(name)


#args  =parameter that will pack arguments into a tuple useful so that a function can accept a varying amount of arguments
def add(*stuff):  #asterisk
  sum=0
  stuff=list(stuff)
  stuff[0]=0
  for i in stuff:
       sum+=i
  return sum


  

print(add(1,2,3,4,5,6))



#kwargs=parameter that will pack all argumnents into a dictionary useful so that a function can accept a varying amount of keyword argument

#def hello(**kwargs):
 # print("hello"+ kwargs['first'], + "" kwargs[last])
  
   #for key,value in kwargs.items():
   #  print(value,end="    ")   #print on the same line
#hello(title="Mr." ,first="bro",middle="dude",last="code")


def hello(**names):      #common naming convection
 # print("hello"+ kwargs['first'], + "" kwargs[last])
  
   for key,value in names.items():
     print(value,end="    ")   #print on the same line
#hello(title="Mr." ,first="bro",middle="dude",last="code")



#string formart()=optional method gives users more control when displaying output


animal="cow"
item="moon"

#"print("The "+animal+" jumped over the"+item)


#print("The {} jumped over the {}".format("cow","moon"))
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item))#positional argument
#print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))#keywordargument

text="the {} jump over the {} "
print (text.format(animal,item))

name="bro"
print("hello,my name is {}".format(name))
print("hello,my name is {:^10} nice to meet you".format(name))   #center align, :>left align :<right align

number=3.1450
print("the number pi is {:.2f}".format(number))

number=1000
print("the number pi is {:,}".format(number))
number=1000
print("the number pi is {:b}".format(number))
print("the number pi is {:o}".format(number))
print("the number pi is {:E}".format(number))




 # pseudo random numbers



import random 

x=random.randint(1,6)
y=random.random()

mylist=["rock","paper","scissor"]
z=random.choice(mylist)
print(z)

cards=[1,2,3,4,5,6,7,8,9,"j","Q","k","A"]
random.shuffle(cards)
print(cards)


#exception =events detected during execution  that interrupt the flow of a program
try:
   # numerator=int(input("enter a number to divide"))
    #denominator=int(input("enter a number to divide by : "))
   ## result=numerator/denominator
    #print(result)

#except ZeroDivisionError as e:
   print(e)
   print("you cant divide by zero idiot")
except ValueError:
     print("eneter only number pliz")
except Exception as e:
  print("something went wrong")
  print(e)
else:
   print(result)

finally:
 print("this is will always execute")


 #file dection


import os
path="C:\\Users\\Admin\\Desktop\\tech"
if os.path.exists(path):
   print("that loaction exists")
   if os.path.isfile(path):
      print("that is a file")
else:
   print("that location does not exist")



   #read file
try:
    with open ("sammy.txt") as file:
      print(file.read())

except FileNotFoundError:
   print("that file not found")


   #write file in python


text="have a noce day/n it was pleasure to meet you/n i wish to meet you next time"

with open ("sammy.txt","w") as file: #w write    #r read
    file.write(text)




#copying the file.
    


#copy file()=copy contents of a file
#copy()=copyfile() +permission mode+destination can be a directory
#copy2=copy()+ copies matadata (files creation and modificatioj times)

import shutil

#shutil.copyfile('sammy.txt','copy.txt')#src.dst
shutil.copyfile('sammy.txt','C:\\Users\\Admin\\Desktop\\christmas\\copy.txt')#src.dst
   
    
import os
source='folder'
destination='C:\\Users\\Admin\\Desktop\\folder'

try:
   if os.replace(source,destination):
      print(source+"was moved")
   

   else:
      os.path.exists(destination)
      print("there is already a file there")

     
except FileNotFoundError:
   print(source+"was not found")
   
   
   #delete file.

import os
#path="course.txt"

#try:
  #os.remove(path)
#except FileNotFoundError:
  # print("that was not found")

path="corse.ptxt"

try:
  #os.remove(path)#delete a file
 # os.rmdir(path) #deletedelete am empty directory
  shutil.rmtree(path)#delete a dirrectorfy containing files
except FileNotFoundError:
   print("that was not found")
except PermissionError:
   print("you dont have a permission to delete that ")
else:
   print(path+"was deleted")  




   





#basic games
#import random


#while true:
   
 #choices=["rock","paper","scissors"]

##computer=random.choice(choices)
#player=None
#while player  not in  choices:
   #player=input("rock,paper or scissors").lower()

#if player ==computer:
   
  #print("computer:",computer)
  #print("player",player)
 # print("tie")
#elif player =="rock":
 #  if computer =="paper":
      # print("computer:",computer)
    #   print("player",player)
    #   print("you lose")
      
   #if computer =="scissors":
      # print("computer:",computer)
     #  print("player",player)
      # print("you win")
       
#elif player=="paper":
 #  if computer =="scissors":
    #   print("computer:",computer)
     #  print("player",player)
    #   print("you lose")
      
   #if computer =="rock":
       #print("computer:",computer)
     #  print("player",player)
     #  print("you win")


#play_again=input("play again? (yes/no):").lower()
#if play_again!="yes":
  

 # print("bye")



#-----------------------------------
def new_game():
 guesses=[]
 correct_guesses=0
 question_num=1



 for key in questions:
   print("----------------")
   print(key)

   for i in options[question_num-1]:
      print(i)

   guess=input("enter(A,B,C,D)")
   guess=guess.upper()
   guesses.append(guess)
   question_num+=1 
   check_answer(questions.get(key),guess)


   correct_guesses+=check_answer(questions.get(key),guess)

   question_num+=1
   
   display_score(correct_guesses,guesses)



#------------------------------
def check_answer(answer,guess):
  if answer==guess:
     print("Correct")
     return 1

  else:
     print("wrong")
     return 0
     
#--------------------------
def display_score(correct_guesses,guesses):
   print("---------------------")

   print('Results')
   print("----------")
   print("Answers:=",end="")
   for i in questions:
      print(questions.get(i),end=" ")
      print()

      print("Guesses:=",end=" ")
   for i in guesses:
      print(i,end="")
   print()
   score=int(correct_guesses/len((questions))*100)
   print("your score is :"+str(score)+"%")


   

#def play_again():
   


   
   



questions={
   
   "who created python ?": "A"
   "what year was python created: ""B"
   "python is tributed to which comedy group:""c"
   "is the round ?:""A"

}                           #list of lists

#2DLIST
options=[["A.Guldo van Rossum","B.Elon musk","c.Billgates","D.mark zuckerberg"],
        ["A.1989","B.1991","c.2000","D.2016"],
        [  "A.lonely island","B.smooth","c.montypython","D.SNL" ],
        [ "A.True","B.false","c.sometimes","D.whats earth"  ]]
         

new_game()
          
print()
  
#--------------------

  #objects object oriented in python pop
#objects is an instance of class what it hasor methods

#it have class

