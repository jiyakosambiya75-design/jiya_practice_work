'''
#2. Arithmetic Operators
#1. Simple calculator (+, -, *, /)
a=10
b=20
print("addition",a+b)
print("subtraction",a-b)
print("multiplication",a*b)
print("division",a/b)
#2. Find remainder using % 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
remainder=a%b
print("Remainde =",remainder)

#3. Calculate area of rectangle/circle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)

#4. Calculate simple interest 
a = float(input("Enter Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time: "))

si = (a * r * t) / 100

print("Simple Interest =", si)




'''
#3. Comparison Operators 
#1. Check greater number between two inputs

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")

#2.cheak if number are equal or not
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

#3.voting eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

#4.find largest of 3 number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")

#5.cheak pass/fail based on marks
 marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
    

    

