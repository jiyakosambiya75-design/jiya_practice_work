#Arbitrary
#Write a Python function that accept any number of argument and return their sum.
def addition(*args):
     total=0
   
     for i in args:
         total += i
       
     return total
print(addition(10 , 80 , 10))
#Keyword Arguments (**kwargs)
#write a python function that accept student information using keywargs arguments and prints all student details.
def student(**kwargs):
    print("Student Details")

    for key , value in kwargs.items():
        print(f"{key}: {value}")
        
print(student(name = "jiya", age=18 , city = "surat" , course = "Python" ))

#doc (Documentation string)
#write a python function to calculate the area of a rectangle and display its documentation.

def rectangle(lenth , width):
    """
    Function Name : rectangle

    purpose:
           calculate rectangle area.

    parameter:
             lenth : int
             width : int

    Return:
          Area of ractangle
    """
    return lenth * width
print("Area : " , rectangle(20,10))
print(rectangle.__doc__)

#Lambda with map()
numbers=[10,20,30,50]
result=list(map(lambda x : x **2 , numbers))

print(result)
 # Lambda with filter()

numbers = [10 , 15 , 20 , 25 , 30 , 35]

even = list(filter(lambda x : x % 2 != 0 , numbers))

print(even)

# Lmbda with sorted()

students = [("jiya" , 18) , ("janvi" , 10) , ("yashvi" , 22) , ("Raveena" , 5)]

print(students)

result = sorted(students , key = lambda x : x [1])

print(result)



