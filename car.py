class Car:
  

 wheels=4 #class variable declared otisde constructor
 
 def __init__(self,make,model,year,color):
      self.make=make
      self.model=model             #constructor method
                              #assifg the attributes     instance,,,,,declared inside construcor
      self.year=year
      self.color=color

 def drive(self):
   print("this "+self.make+" "+self.model+" car is driving")        #methods
   
   
 def stop(self):
    print("this "+self.model+" is stopped")




    #class inheritance


    #parent and children
class Animal:
   alive=True

   def eat(self):
      print("This animal is eating")

   def slumber(self):
      print("this animal is sleping")

class Rabbit(Animal):
   def run(self):
      print("this rabbit is running")

class Fish(Animal):
   def swim (self):
      print("this fish is swimming")

class Hawk(Animal):
   def fly(self):
      print("this hawkis flying")


rabbit=Rabbit()
fish=Fish()
hawk=Hawk()


#print(rabbit.alive)
#fish.eat()
#hawk.slumber()


rabbit.run()
fish.swim()
hawk.fly()





#multilevel of inheritance is when a derived (child) calss inherits anotjher derived (child) 



class organism:
   alive=True


class Animal(organism):
   
   def eat(self):
      print("this animl is eating")


class Dog(Animal):
   def bark(self):
       print("This dog is barking")



dog=Dog() 
print(dog.alive)
dog.eat()
dog.bark()




#multiple inheritance is when a cshild classsis derived from one than parent class



class prey:
   
  def flee(self):
     print("this animal flees")

class predator:
   
   def hunt(self):
     print("this animal is hunting")


class Rabbit(prey):
   pass

class Hawk(predator):
   pass


class Fish(prey,predator):
   pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()



#method overriding

class Animal:
   def eat(self):
      print("this animal is eating")


class Rabbit(Animal):
   def eat(self):
      print("this rabbit is eating a carrot")

rabbit=Rabbit()
rabbit.eat()



#method chaining
#calling multiple methods sequentially.
  # each call performs an action on the same objects and returns self


class car:
   def turn_on(self):
      print("you start the engine")
      return self 


   def drive(self):
      print("you drive the car")
      return self
    

   def brake(self):
      print("you stops on the breaks")
      return self

   def turn_off(self):
      print("you turn off the engine")
      return self
car=car()
#car.turn_on().drive()
#car.brake().turn_off()
#car.turn_on().drive().brake().turn_off

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()


#super function
#super ()= function is used to giive acces to the methods parent class.returns a temporary objects of a parent when used.

class Rectangle:
    def __init__(self,length,width):
       self.length=length
       self.width=width
    def area(self):
       return self.length*self.width
   
class square (Rectangle):
   def __init__(self,length,width):
       super().__init__(length,width)


class cube(Rectangle):
   
   def __init__(self,length,width,height):
      super().__init__(length,width)
      self.height=height

   def volume(self):
       return self.length*self.width*self.height
   
square=square(3,3)
cube=cube(3,3,3)
print(square.area())
print(cube.volume())



#abstract classes
#prevent a user from creating an object of that class
#prevent a user fromto override abstractmethods in a child class.
#abstaract class===a classwhich contains  oneor more abstaract methods...
#abstract method=method that has declaration but doesnot have an implememntation



from abc import ABC,abstractmethod
class vehicle(ABC):
   @abstractmethod
   def go(self):
      pass
   
   @abstractmethod
   def stop(self):
      pass
   
class car (vehicle):
   
   def go(self):
      print("you drive the car")

      
   def stop(self):
      print("this car is stopped")

class Motorcycle(vehicle):
   def go(self):
      print("you ride the motorcycle")

      
   
   def stop(self):
      print("this motorcycle is stopped")


#vehicle=vehicle()
car=car()
motorcycle=Motorcycle()

#vehicle.go
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()



#objects as arguments

class Car:
   color=None

class motorcycle:
   color=None
def change_color(vehicle,color):
   vehicle.color=color

car_1=Car()
car_2=Car()
car_3=Car()


bike_1=motorcycle


change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)




#ducktyping
#concept where the class of an object is less important than the methods/attributes that class might have
#class type is not checked if minumum methods,attributes are present
#if it walks likea duck and it quacks llike a duck,thenit must be aduck."'"


class Duck:
   def walk(self):
      print("this duck is walking")


   def talk(self):
      print("print duck is is quacking")


class   Chicken:
   def walk(self):
      print("print this duck is walking ")


   def talk(self):
      print("this chicken is clucking")

class Person():
   def catch(self,duck):
      duck.walk()
      duck.talk()
      print("youcaught the critter")

duck=Duck()
chicken=Chicken()
person=Person()
person.catch(chicken)  #since chicken can walk and talkas suck,canb a substitute of aduck


