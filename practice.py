
#warlus operator also is called asignement expression
#new python 3.8
#assignment expression aka warlus operator
#assigs values to variables as part of larger expressions



#happy=True
#print(happy)
#print(happy:=True)


#foods=list()
#while  True:
    #food=input("what food doto like")
    #if food =="quit":
      #  break
   # foods.appen(food)


#foods=list()

#
#while food:=input("what food do like:")!="quit":
   #foods.append(food)


   #function to variable.


def hello():
   print("hello")

#hi=hello
#hello()
#hi()

say=print
say("whoa! i cant believe this works!:o ")


#higher order  function in python function either:
#                      1.accepets a function as argument
          
#]                       return a function
#                           in python function are also treatted as objects
#



def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()


def hello(func):
   text=func("Hello")
   print(text)

hello(loud)   #passing loud as an argument
hello(quiet)


def divisor(x):
   def dividend(y):
      return y/x

   return dividend

divide=divisor(2)

print(divide(10))




# Define a higher-order function that takes another function as an argument
def apply_operation(func, x, y):
    return func(x, y)

# Define some simple functions to be used as arguments
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Using the higher-order function with different operations
result1 = apply_operation(add, 5, 3)       # Adds 5 and 3
result2 = apply_operation(subtract, 7, 2)  # Subtracts 2 from 7
result3 = apply_operation(multiply, 4, 6)  # Multiplies 4 and 6
result4 = apply_operation(divide, 8, 2)    # Divides 8 by 2

print("Result of addition:", result1)
print("Result of subtraction:", result2)
print("Result of multiplication:", result3)
print("Result of division:", result4)




#lamda function

#function written in line 1 using lamda keyword.
#excepts any nuber of arguments ,but only one expressions

#        (thinl of it as a shortcuts)

#      (Useful  if needed for a short period of time,throw away)
#lamda parameters:: expressions



#def double(x):
  #  return x*2
#print(double(5))

double=lambda x :x*2
multiply=lambda x,y:x*y
print(double(5))
print(multiply(5,6))

add=lambda x,y,z :x+y+z
print(add(3,4,6))

full_name=lambda first_name,last_name:first_name+""+last_name
print(full_name("bro","code"))
age_check=lambda age:True if age>=18 else False
print(age_check(18))



#sort () method=used with the lsists
#sort() function =used with iterables


#students=["chege","samido","oliver","brian","wangundu"]

#students.sort(reverse=True)

#for i in students:
   # print(i)


    #doess not support tupples,but

students=("chege","samido","oliver","brian","wangundu")

sorted_students=sorted(students,reverse=True)

for i in sorted_students:
    print(i)

   

   #keyword arguments
    
#students =  [ ("squildward","F",60),
         #    ("sandy","A", 33),
          #   ("patrick","D",36),
         #    ("spongebob","B",20),
          ##   ("mr.krabs","c",78)
    
#]

#grade=lambda grades:grades[1]

#students.sort(key=grade)
#for i in students:
   # print(i)


#tuple
students = (  ("squildward","F",60),
             ("sandy","A", 33),
             ("patrick","D",36),
             ("spongebob","B",20),
             ("mr.krabs","c",78))
    


grade=lambda grades:grades[1]

sorted_student=sorted(students,key=grade)
for i in sorted_students:
   
   print(i)




   #Map applies a function to each item in an iterable (list,tuple)
  # map(function,iterable)
   
store=[("shirt",20.00),
       ("pants",25.00),
       ("jacket",50.00),
       ("socks",10.00)]

to_euros=lambda data:(data[0],data[1]*0.82)
to_dollars=lambda data:(data[0],data[1] /0.82)

store_dollars=list(map(to_dollars,store))


for i in store_dollars:
    print(i)



#filter()=creates a collection of elements from a which a fuction returns true.
    
#filter(function,iterable)
    
friends=[("rachael",19),
         ("monica",18),
         ("phoebe",17),
         ("joey",16),
         ("chandler",21),]
age=lambda data:data[1]>=18
drinking_buddies=list(filter(age,friends))

for i in drinking_buddies:
    print(i)

#REDUCE
#reduce=apply a function to an iterable and reduce it to a single cumulative value.
  #  performs a function on first two elements and repeats until 1 value remains
#reduce(function,iterable)
    

import functools
letters=["h","E","l","l","o"]
word=functools.reduce (lambda x,y,:x+y,letters) 
print(word)



factorial=[5,4,3,2,1]
result=functools.reduce(lambda x,y, :x*y,factorial)
print(result)



#list comprehensions=is a way to cfeate a new list with less syntax can mmic certain lamda function,easir to read

#list=[expression for item in iterable.if (if/else)conditional]


squares=[]
for i  in range (1,11):
    squares.append(i*i)
#print(squares)


squares=[i*i for i in range (1,11) ]
print(squares)



students=[100,90,80,60,60,50,40,40,0]

#passed_students=list(filter(lambda x:x>=60,students))  #filter programs

#passed_students=[i for i in students if i >=60]
passed_students=[i for i in students if i >=60]

passed_students=[i if i>=60 else "failed" for i in students]

print(passed_students)



#dictionary comprehension 
#creates a dictionaries using an expression ,can replace for loops and certain lambda functions

#dictionary={key:expression for (key,value) in iterable}
#dictionary=[key:expression for (key,value) in iterable if conditional]
#dictionary={key:(if/else)for (key,value in iterable)}
#dictionary={key:function (value)} for (key,value) in iterable

#cities_in_f={"newyork":32,"boston":75,"los Angeles":100,"chocago":50}

#cities_in_c={key: round((value-32)*(5/9)) for(key,value) in cities_in_f.items () }

#print(cities_in_c)


#weather={"Newyork":"snowing","boston":"sunny","losAngels":"sunny","chicago":"cloudy"}
#sunny_weather={key:value for (key,value) in weather.items() if value=="sunny"}
#print(sunny_weather)

cities={"newyork":32,"boston":75,"los Angeles":100,"chocago":50}

desc_cties= {key:("warm"if value >=40 else "cool")for (key,value) in cities.items()}

print(desc_cties)

def check_temp(value):

    if value>=70 :
      return "Hot"
    
    elif 69>=value >=40:

        return "warm"
    
    else:

        return "cold"
cities={"newyork":32,"boston":75,"los Angeles":100,"chocago":50}

desc_cities={key:check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
    

#zip function


#aggregate elements fromtwo ore more iterables (list,tuples,sets.etc)
#creates a zip object  with paired elements stored in tuplesfor such elements


#usernames=["dude","bro","mister"]
#passwords=("pa@ssword","abc123","quest")


#users=zip(usernames,passwords)
#users=dict(zip(usernames,passwords))

#print (type(users))


#for key,value in  users.items():
   # print(key+ " :  +"+value)



usernames=["dude","bro","mister"]
passwords=("pa@ssword","abc123","quest")
login_date=["1/1/2121","1/2/2021" ,"1/3/2021"      ]

users=zip(usernames,passwords,login_date)

for i in users:
    print(i)




#if name=='_main_'

#module can be as stabnd alone program
    #module can be imoorted and used by other modules
    #python interpretor set "special variables" one one which is _name_
    #python will assign _name_variable a value of '_main_" if it is the initial module beibng run
    #then python will execute the code found within _main_
    
