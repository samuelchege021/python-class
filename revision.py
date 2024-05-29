class myclass:
   def __init__(self,value):
      self.value=value
      print(self.value)
   def my_method(self):
         return f"value is {self.name}"


obj=myclass(10)
      #accesing method attribute
print(obj.my_method)

myclass(70)


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

      result=c1.add(c2)
      print(result.real,"+",result.imag,"i"())



      
      


