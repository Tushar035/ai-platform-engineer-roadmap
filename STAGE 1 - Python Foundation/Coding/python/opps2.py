## Encapsulation - public, protected, private variables
# class student:
#     def __init__(self, name, age):
#         self.name = name # public variable
#         self.__age = age # private variable

#     def get_name_age(self):
#         #print(self.name)
#         #print(self.__age) # we can print beacuse we are accessing private varaible internally
#         #return self.__age  # throws error 'student' object has no attribute '__age'

# studentObj= student("Tushar",32)
# print(studentObj.__age)  # throws error 'student' object has no attribute '__age'      
# print(studentObj._student__age)   # Bypassing protection name mangling 
# print(studentObj.get_name_age())    

## Inheritance
# single inheritance
# class Animal:
#     def speak(self):
#         print("all animal speak")

# class dog(Animal):
#     def bark(self):
#         print("bho bho")

# dogObj = dog()
# dogObj.speak()
# dogObj.bark()     

# multiple inheritance
# class father:
#     def father_skill(self):
#         print("teach")

# class mother:
#     def mother_skill(self):
#         print("cook")

# class child(father, mother):  ## comma seprated 
#     def child_skill(self):
#         print("Dance")

# childObj = child()
# childObj.father_skill()
# childObj.mother_skill()
# childObj.child_skill()

# print(child.mro())

## Diamond problem without super
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()
# print(D.mro())

## Diamond problem with super
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show() # super() does NOT mean call parent It means → call next class in MRO

# d = D()
# d.show()