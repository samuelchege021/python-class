
print(1)

for n in range (2,10):
    for x in range (2,n):
        if n % x ==0:
            print(n,"equals",x,"+",n//x)

            break
        else:
            #loop fell through without finding a factor
            print (n,'is a prime number')
for num in range(2,10):
    if num % 2 ==0:
        print("found an even",num)
        continue
    print("found a number",num)

#argument
def greet(name='world'):
    print(f"hello,{name}!")
    greet()
    greet ("alice")


class MyClass:
        
        def __init__(self, name='World'):
         self.name = name

        def greet(self):
         print(f"Hello, {self.name}!")





def fib(n): #write fibonacci series up to n
    "print a Fibonacci series up to n"
    while a < n:
        print(a,end='')
        a,b=b,a+b
        print(fib)



def ask_ok(prompt,retries=4,remimder='pleasetry again'):
        while True:
           ok=input(prompt)
           if ok in ('y','ye','yes'):
               return True
           if ok in ('n','no','nop','nope'):
               return False
           retries=retries-1
           if retries<0:
               raise ValueError('invalid user response')
               print(reminder)
# def my_list():
        
#  my_list=[1,2,3]
#  my_list.append(4)
# print(my_list) # output[1,2,3,4]


# my_list=[1,2,3]
# my_list.extend([4,5.6])
# print(my_list) #output:[1,4,2,3]

# my_list(1,2,3)
# my_list.insert(1,4)
# print(my_list)  # output:[1,4,2.3]

# my_list=[1,2,3]
# removed_item=my_list.pop(1)

# print(my_list) #output:[1,3]
# print(removed_item) #output:2

# my_list=[1,2,3]
# my_list.clear()
# print(my_list) #output:[]

# my_list=[1,2,3,2]
# index=my_list.index(2)
# print(index) #output:1

# my_list=[1,2,3,2,2]
# count=my_list.count(2)
# print(count) #output:3

# my_list=[3,1,2]
# my_list.sort()
# print(my_list) #output:[1,2,3]\

# my_list=[1,2,3]
# my_list.reverse()
# print(my_list) #output :[3,2,1]

# my_list=[1,2,3]
# copied_list=my_list.copy
# print(copied_list) #output :[1,2,3]



#list as stacks
# stack=[3,4,5]
# stack.append(6)
# stack.apppend(7)

# print(stack)

# stack.pop()
# stack.pop()


#Queues

from collections import deque
queue =deque(['eric','john','michael'])
queue.append("terry")
queue.append("Graham")
queue.popleft()


#list comprehensions

squares=[]
for x in range (10):
   squares.append(x**2)
   print()

   squares=[x**2 for x in range(10)]

   print()


   combs=[]
   for x in (1,2,3) :
      for y in (3,1,4):
         if x !=y:
            combs.append((x,y))

            print()


            #sets
   def basket (fruits):
               baskets={"apple",'orange',"apple",'pear','orange','banana'}

               for fruit in baskets :
                print ()
               if fruit== 'orange':
                
                print('found my orange')
               else:
                print('this is not a orange')



                basket= {'apple','orange','apple','pear','orange','banana'}
                print(basket)
            


        #dictionaries
                  
def contacts ():
   contacts={
      "john":"john@gmail.com",
      "alice":"alice@gmail.com",
      "bob":"bob@gmail.com"

   }

   #acccessing values
   print(contacts["john"])

   #add a new contact
   contacts['eve'] ="eve@gmail.com"

   #modifying the existing contact
   contacts['bobs']="bob_new@gmail.com"

   #removing contact
   del contacts ['alice']

#printing all contacts

for name,email in contacts.items():
   print(f"{name} : {email}")



def sentence (word_frequency):
 sentence=('this is a simple sentence with words.this is just an eXAMPLE')
word_frequency={}
word=sentence.split()
for word in word :
   word=word.lower()
   if word in word_frequency:
    word_frequency[word] +=1

   else:
      word_frequency[word]=1

      print(word_frequency)

    


#method attribute.
      


         

class complex:
   def _init_(self,real,imag):
      self.real=real
      self.imag=imag

   def add(self,other):
         return complex(self.real+other.real,self.imag+other.real)
      
   def subtract(self,other):
         return complex(self.real-other.real,self.imag-other.real)
   def multiply(self,other):  
         real_part=(self.real*other.real-self.imag*other.real)
         imag_part=(self.real*other.real+self.real*other.real)
         return complex(real_part,imag_part)
   
   def divide (self,other):
       denominator=other.real**2+other.imag**2
       real_part=(self.real*other.real+self.imag*other.imag)/denominator
       imag_part=(self.real*other.real-self.imag*other.real)/denominator
       return complex(real_part,imag_part)
   
   def get_real_part(self):
       return(self.real)
   def get_imag_part(self):
       return (self.imag)
   
   def __str__(self) :
      return f"{self.real} + {self.imag}i"
   
   #example usage
   c1=complex(3,2)
   c2=complex(1,5)

   #addition

   result_addition=c1.add(c2)
   print("Addition:",result_addition)



      
      

import random


class Card:
    def __init__(self, kind, rank, deck):
        self._kind = kind
        self._rank = rank
        self.deck = deck
        self.where = None

    def __repr__(self):
        return 'Card(kind={}, rank={}'.format(self.kind, self.rank)

    @property
    def kind(self):
        return self._kind

    @property
    def rank(self):
        return self._rank


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        kinds = ['H', 'C', 'D', 'S']
        self.cards = [Card(kind, rank, self) for kind in kinds for rank in ranks]

    def deal(self, players, n=None):
        if any(p.deck is not self for p in players):
            raise RuntimeError('Player {} is not playing the deck'.format(p.id))

        n = n if n is not None else len(self.cards)
        random.shuffle(self.cards)

        for i, card in enumerate(self.cards[:n * len(players)]):
            card.where = players[i % len(players)]


class Player:
    def __init__(self, id, deck):
        self.id = id
        self.deck = deck

    @property
    def hand(self):
        return [card for card in deck.cards if card.where is self]
