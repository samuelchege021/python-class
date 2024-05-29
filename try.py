class mpesa ():
    def __init__(self,account_balance,phone_number) :
       self.account_balance=account_balance
       self.phone_number=phone_number

    def send_money(self,amount,recipient):
        if self.account_balance>=amount:
            self.account_balance-=amount 
            print(f"{amount}kes sent to {recipient} successfully")

        else:
            print("insufficient funds")

class credo(mpesa):
    def __init__(self, account_balance, phone_number,Id_number):
        super().__init__(account_balance, phone_number)
        self.Id_number=Id_number
    def buy_airtime(self,amount) :
        if self.account_balance>=amount:
           self.account_balance-=amount 
           print(f"{amount}kes airtime bought successfully")
        else:
            print ("inmsufficient funds") 

class bussiness_mpesa(mpesa) :
    def __init__(self, account_balance, phone_number,bussiness_name):
        super().__init__(account_balance, phone_number)  
        self.bussiness_name=bussiness_name

    def receive_money(self,amount):
        self.account_balance+=amount
        print(F"{amount} kes received successfully")

personal=credo(500,713509121,263314195)
personal.send_money=(300,87654321)
personal.buy_airtime=(50)
biz=bussiness_mpesa(2000,713509121,"onaires")
biz.receive_money(3000)
biz.send_money(1500,87654321)





class agriculture :
    def __init__(self,rearing,planting) :
        self.rearing=rearing
        self.planting=planting

    def tuposite (self):
        return "f my job is {rearing} and {planting}"
    
    
    #creating instances of the agriculture class
agriculture1 =agriculture("goats","cabbages")
agriculture2=agriculture("sheep","sukumawiki")

#using methods of class instances
print(agriculture1.tuposite()) #my job is rearing goat and planting cabbages
print(agriculture2.tuposite()) #my job is rearing sheep and planting sukumawikipython






class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages."

# Creating instances of the Book class
book1 = Book("Harry Potter", "J.K. Rowling", 400)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 250)

# Using methods of class instances
print(book1.info())  # Output: Harry Potter by J.K. Rowling, 400 pages.
print(book2.info())  # 

class prolife:
    def __init__(self,vision,mission) :
        self.vision=vision
        self.mission=mission

    def club(self):
        return f" it is our role to {self.vision} and {self.mission} life upto natural death"
    
prolife1=prolife("protect", "promote  ") 
prolife2=prolife("defend","preserve")    

print (prolife1.club())
print (prolife2.club())

class person:
    def __init__(self,firstname,secondname):
        self.firstname=firstname
        self.secondname=secondname
    def printname(self):
        print(self.firstname,self.secondname)
    
x=person("alice","sammy")       
x.printname()


class student(person):
    def __init__(self, firstname, secondname,year):
        super().__init__(firstname, secondname)
        self.graduationyear=year

    def welcome(self):
        print("welcome",self.firstname,self.secondname ,"to the class of" ,self.graduationyear)

x=student("oliva","ndungu",2024)
x.welcome()



class car :
    def __init__(self,make,model,year,color) :
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    def describe_car(self):
        print(f"I own a {self.make} {self.model} manufactured in {self.year} thats painted {self.color}")

  
myobj=car("volkswagen","beetle",2021,"grey")
myobj.describe_car()
myobj2=car("toyota","fj cruiser",2020,"blue")
myobj2.describe_car()

class Gari:
    odometer_reading=0
    model=""
    year=""
    make=""
    def conect(self,odometer_reading,model,year,make):
        self.odometer_reading= odometer_reading
        self.model = model
        self.year=year
        self.make= make
    def describe_gari(self): 
        return f"the {self.make} {self.year} {self.year}"
    
    def read_odometer(self):
        return f"this car has {self.odometer_reading} mileage"
    
    def update_odometer(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you cant roll back an odometer")

    
    def increment_odometer(self,miles):
        self.odometer_reading +=miles
    def main(self,name,model,year,odometer_reading=0):
        self.conect(odometer_reading=odometer_reading,model=model,year=year,make=name)
        print(self.describe_gari())
        print(self.read_odometer())
        self.update_odometer(100)
        print(self.read_odometer())
        self.increment_odometer(50)
        print(self.read_odometer())



if __name__ =="__main__":
    new =Gari()
    new.main("porsche","cayyenne",2006)


#classpolynorshiphism
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
     print("move!")
     
class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
       print("sail")

class plane(vehicle):
    def move(self):
     print("fly!")

car1=car("ford","mustanf") 
boat1=boat("ibiza","torimg20")    
plane1=plane("boeieng","747")     


for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
x.move

x=42
if x<0:
    print("negative chenge to zero")
elif x==0:
    print("zero")
else:
    print("more") 


words=["cat","window","defenestrate"]
for w in words:
    print(w,len(w))






class wingsplumber:
  def __init__nit__(self,plumbing,bio):
    self.plumbing=plumbing
    self.bio=bio


    def plumber (self):
        print( f"quality {self.plumbing} and {self.bio}")
        


x=wingsplumber("houseplumbing","biodigester")
x.plumber()
