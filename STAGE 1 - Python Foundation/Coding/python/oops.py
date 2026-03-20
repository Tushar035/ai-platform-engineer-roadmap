## class example
# class car:
#     brand ="toyoto"
#     speed = 120

# carObj =  car() 
# print(carObj.brand)   
# print(carObj.speed)   

## class constructor to initialise properties
# class car:
#     def __init__(self, color, brand):
#         self.color = color
#         self.brand = brand

# carObj2 = car("red","maruti")
# print(carObj2.brand)
# print(carObj2.color)

## class and instance variables
# class employee:
#     company = "Microsoft" # class variable
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary # instance variable

# empObj = employee("Tushar", 5000000)
# empObj2 = employee("Rahul", 1000000)

# print(empObj.company)
# print(empObj2.company)

## methods in class : class method, instance method, static method
# class employee:
#     company = "Microsoft"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def getEmployeename(self):
#         print(self.name)   

#     @classmethod
#     def change_companyname(cls, companyname):
#         cls.company = companyname
#         print(cls.company)

#     @staticmethod
#     def calculate_salary_withbonus(salary):
#         salaryWithBonus = salary+ (salary * 0.20)    
#         print("salaryWithBonus : ", str(salaryWithBonus))
        
# empObj = employee("Tushar", 50000)
# empObj.getEmployeename()        
# empObj.change_companyname("Google")
# employee.calculate_salary_withbonus(50000)
