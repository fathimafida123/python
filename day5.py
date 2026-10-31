# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self): #__str__() defines how the object should be represented as a string.
#         return f"name:{self.name} age:{self.age}"    
# student1=student("fida",18)
# print(student1.name)     
# print(student1.age)   
# print(student1)

# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def display(self):
#         return f"""color:{self.color}
# brand:{self.brand}"""    
# car1=car("black","BMW")
# car2=car("blue","benz")

# print(car1.display())
# print(car1.display())

# class student:

#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def display(self):
#         print(f"{self.name} get {self.mark} mark")
# student1=student("fida",77) 
# student2=student("finu",66)
# student1.display()
# student2.display()       

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance = self.balance+amount   
#         return self.balance 
# p1=BankAccount("fida",1000)
# total=p1.deposit(2000)
# print(total)

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def increase_salary(self,amount):
#         self.salary=self.salary+amount    
#         return self.salary
# p1=Employee("fida",3000)        
# result=p1.increase_salary(3000)
# print(result)

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def apply_discount(self,discount):
#         self.price=self.price-discount
#         return self.price
# lap=Product("laptop",40000)
# result=lap.apply_discount(1000)
# print(result)

# class Student:
#     def __init__(self,name,mark):
#         self.name=name 
#         self.mark=mark
#     def check_result(self):
#         if self.mark>=40:
#             return "pass"
#         else:
#             return "fail"
# stu1=Student("fida",75)
# stu2=Student("finu",25)
# res1=stu1.check_result()
# res2=stu2.check_result()         
# print(res1)
# print(res2)       

# class Student:
#     def __init__(self,name,age,mark):
#         self.name=name
#         self.age=age
#         self.mark=mark
#     def studet_details(self):
#         print(f"name is{self.name} age is {self.age} mark is {self.mark}") 

#     def passornot(self):
#         return self.mark>=80  
# s1=Student("fida",18,78)
# s2=Student("shamna",17,89)
# s3=Student("rinsha",18,78)
# s4=Student("hiba",18,90)
# s1.studet_details()
# s2.studet_details()
# s3.studet_details()
# s4.studet_details()
# print(s1.passornot())

# #CLASS VARIABLE
# class Student:
#     School="ABS School"
#     student_count=0
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#         Student.student_count +=1 
#     def show_details(self):
#         print(f"""Name: {self.name}     
# Mark: {self.mark} 
# School: {self.School}""")
#     def change_school(self,change):
#         self.School=change

# s1 = Student("Fida", 90)
# s2 = Student("Shamna", 85)
# s3 = Student("Rinsha", 78)   
# s2.change_school("ABC School")
# s1.show_details()
# s2.show_details()
# s3.show_details()
# s2.show_details()
# print("Total number of students :",Student.student_count)

# STATICMETHODS
# class Student:
#     @staticmethod
#     def is_valid_mark(mark):
#         return 0<= mark <=100

# print(Student.is_valid_mark(90))  
# print(Student.is_valid_mark(120))      

# CLASSMETHOD

# class Student:
#     school="ABS SCHOOL"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
# Student.show_school()        

# if we want to change school name for every student

# class Student:
#     School="ABS school"
#     def __init__(self,name):
#          self.name=name
#     def show_school(self):
#          print(f"{self.name} : {self.School}")   
#     @classmethod
#     def change_school(cls,newschool):
#         cls.School=newschool
# s1=Student("fida")
# s2=Student("shamna")

# Student.change_school("ABC SCHOOL")

# s1.show_school()
# s2.show_school()

# INHERITENCE

# class Animal:
#     def eat(self):
#         print("animal is eating")
#     def sleep(self):
#         print("animal is sleeping")    
# class Dog(Animal):  #class Dog(Animal) ennu parayumbol, Dog class-in Animal class-ile methods use cheyyan kazhiyum.
#     def bark(self):
#         print("dog is barking")        
# dog1=Dog()
# dog1.eat()
# dog1.bark()
# dog1.sleep()        

# INHERITS with __init__()
# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def  bark(self):
#         print(f"{self.name} is barking")   
# class Cat(Animal):
#     def eat(self):
#         print(f"{self.name} is eating")
# dog1=Dog("Bruno")  
# cat1=Cat("kittu")      
# dog1.bark()#Dog class-il constructor illa. Athukondu Animal class-il ninnum constructor inherit cheyyum. "Bruno" name store cheythittu bark() call cheyyumbol name print aavum.
# cat1.eat()

# MULTIPLE INHERITENCE

# class father:
#     def skills(self):
#         print("father is driving")
# class mother:        
#     def talent(self):
#         print("mother is singing")
# class child(father,mother):        
#     def hobby(self):
#         print("child is drawing")
# c=child()
# c.skills()
# c.talent()
# c.hobby()  

# class Father:
#     def __init__(self):
#        self.father_name="subair"
# class Mother:
#     def __init__(self):
#        self.mother_name="salma"
# class Child(Mother,Father) :
#     pass
       
# c1=Child()
# # print(c1.father_name) 
# print(c1.mother_name)   

# class Father:
#     def __init__(self):
#        self.father_name="subair"
# class Mother:
#     def __init__(self):
#        self.mother_name="salma"
# class Child(Mother,Father) :
#     def __init__(self):
#         Father.__init__(self)#This calls the Father class constructor and creates the father_name attribute for the child object.
#         Mother.__init__(self)
# c1=Child()
# print(c1.father_name) 
# print(c1.mother_name)   

# MULTILEVEL INHERITENCE
# class Grandfather:
#     def farming(self):
#         print("grandfather do farming")
# class Father(Grandfather):
#     def driving(self):
#         print("father do driving")        
# class Child(Father):
#     def skills(self):
#         print("children do drawing")     
# c1=Child()
# c1.skills()        
# c1.driving()
# c1.farming()

# class Grandfather:
#     def skills(self):
#         print("grandfather do farming")
# class Father(Grandfather):
#     def skills(self):
#         print("father do driving")        
# class Child(Father):
#     def skills(self):
#         print("children do drawing")     
# c1=Child()
# c1.skills()        

# class Grandfather:
#     def __init__(self):
#         self.skills="farming"
# class Father(Grandfather):
#     def __init__(self):
#         Grandfather.__init__(self)
#         self.job="driving" 
# class Child(Father):
#         def __init__(self):
#             Father.__init__(self)
#             self.hobby="drawing"
# c1=Child()
# print(c1.skills)
# print(c1.hobby)
# print(c1.job)                       

# class A:
#     def __init__(self):
#         self.x = 10

# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.y = 20

# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.z = 30

# obj = C()
# print(obj.x + obj.y + obj.z)

# class A:
#     def __init__(self,name):
#         self.name=name
# class B(A):
#     def __init__(self,name):
#         A.__init__(self,name)
# class C(B):
#     def __init__(self,name):
#         B.__init__(self,name)
# obj=C("fida")
# print(obj.name)#the value travels from C → B → A.

# HIERARICAL INHERITENCE

# class Animal:
#     def eat(self):
#         print("animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
# class Cat(Animal):
#     def meow(self):
#         print("cat is meowing")
# d=Dog()
# c=Cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()                        
# print(Dog.mro())

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()

# # HYBRIDE INHERITENCE
# class Person:
#     def introduce(self):
#         print("I am a person")

# class Student(Person):
#     def study(self):
#         print("I am studying")

# class Teacher(Person):
#     def teach(self):
#         print("I am teaching")

# class Assistant(Student, Teacher):
#     def help(self):
#         print("I help students")
# a = Assistant()

# a.introduce()
# a.study()
# a.teach()
# a.help()        

# mroR()

# class Parent():
#     def work(self):
#         print("parent ")
# class Child(Parent):
#     def work(self):
#         print("child")    #it only print child    
# c=Child()
# c.work()

# class Parent():
#     def work(self):
#         print("parent ")
# class Child(Parent):
#     def work(self):
#         super().work() #super().work() calls the work() method from Parent
#         print("child")    #it print both    
# c=Child()
# c.work()

# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,course):
#         super().__init__(name)#super() handles passing the current object automatically. That's why you only pass name, not self.
#         self.course=course
#     def display(self):
#         print('NAME:', self.name)
#         print("COURSE:", self.course)            
# s=Student("fida","python")
# s.display()