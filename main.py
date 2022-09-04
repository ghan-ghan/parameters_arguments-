


'''Python function Arguments: it is placed inside the calling function:'''
'''Python parameters are added or used in the defineing the function:'''



def my_first_function():           #function without parameter 
    print("Hello world !")
    
my_first_function()                #doesnot have arguments : so function may use parameter or  may be without parameter

    
    
    
    
def my_first_function(name):       #function with the only one parameter
    print(f"Hello ,my friend, {name}")
    
    
my_first_function("Anil")
my_first_function("Sailesh")
my_first_function("Jeevan")
my_first_function("Gyan")
my_first_function("Arun")



def my_first_function(first_name,last_name):     #simple positional arguments
    print(f"First name:{ first_name} ; Last name:{ last_name}")

my_first_function("Anil ", " Gaire")
my_first_function("Arun ", " Gaire")
my_first_function("Gyan ", " Neupane")
my_first_function("Jeevan ", " Pandey")
my_first_function("Sailesh ", " Rawal")



'''keywords arguments: key and value is mandatory in keyword arguments '''
def my_first_function(first_name,age):
    print(f"{first_name} is {age} years old .")
    
my_first_function(first_name="Anil",age =22)
my_first_function(first_name="Arun",age =20)
my_first_function(first_name="Anil",age =22)
my_first_function(age = 26 ,first_name="Gyan")
my_first_function(age =22, first_name ="sailesh")


'''default arguments :parameters value is made default , unless and until the arguments passed 
is different than the default value  it gives the default value '''

def my_first_function(first_name , college="Trichandra"):
    print(f"{first_name} has done the bachelor's degree from {college}")
    
my_first_function("Anil")
my_first_function("saman")
my_first_function("Anil", "St.Xavier")
my_first_function("jeevan","Kathmandu University")

'''Non default arguments follow default arguments'''
# if we keep the second item as parameter of undefault type but assign the value to first one as below it prompt out error

# def my_first_function(first_name ="Ram" , college):
#     print(f"{first_name} has done the bachelor's degree from {college}")
    
# my_first_function("Anil")
# my_first_function("saman")
# my_first_function("Anil", "St.Xavier")
# my_first_function("jeevan","Kathmandu University")


'''arbitrary arguments'''

def my_first_function(*friends):
    print(f"My friends are {friends}")
    print(f"My friends are {friends[0]}")
    print(f"My friends are {friends[1]}")
    print(f"My friends are {friends[2]}")
    
my_first_function("ram","shyam","hari")