
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
 marks = int(input("Enter marks: ")):

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#4logical operator
#1. check number is between 1-100
num=int(input("Enter your number: "))
if num>=1 and num <=100:
  print(True)
else:
  print(False)
#2. login system (username+password)
name=input("Enter your username: ")
password=input("Enter your password: ")
print(name == "jiya_k" and password == "jiyu123")

#3. Check leap year (multiple conditions)
year=int(input("Enter year: "))
if year%4==0 and year%100!=0:
  print("leap year")
else:
  print("Not a leap year")

#4. check if number is divisible by 3 and 5
num=int(input("Enter your num: "))
print(num%3==0 and num%5==0)
  
#5.validate input(age>18 and city=="surat")
age=int(input("Enter your age: "))
city=input("Enter your city name: ")
print(age>=18 and city=="surat")
5.assignment operator 

#1 Increment and decrement a number
num=int(input("Enter your num: "))
num+=1
print("After increasing number:",num)
num-=1
print("After decreasing number:",num)

#2 Use +=,-=;*= in calculation
a=23
b=5
a+=b
print(a)
print(b)
a-=b
print(a)
print(b)
a*=b
print(a)
print(b)

#3. Create running total (add numbers step by step) 
total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    total = total + num
    print("Running Total =", total)

print("Final Total =", total)

#4.Salary increment calculation 
salary=int(input("Enter your salary: "))
increment=int(input("Enter your incrment: "))
salary+=increment
print("New salary:",salary)

#5.Discount calculation using assignment perators
rate=int(input("Enter your rate: "))
discount=int(input("Enter your discount: "))
rate-=discount 
print(rate)


#7.Mixed practice 

#1.studen marks--> calculate total & average 
subject1=input("Enter your subject1: ")
marks1=int(input("Enter your marks1: "))
subject2=input("Enter your subject2: ")
marks2=int(input("Enter your marks2: "))
subject3=input("Enter your subject3: ")
marks3=int(input("Enter your marks3: "))
total=marks1+marks2+marks3
print(total)
average=total/3
print(average )

#2.Bill generator (price+tax)
price=int(input("Enter price: "))
tax=int(input("Enter tax: ")) 
price += tax
print(price)

#3.age calculator (current - birth year)
year=int(input("Enter current year: "))
birthyear=int(input("Enter your birth year: "))
year-=birthyear
print("Your current age: ",year)

#4. Even/Odd + positive/negative check
num=int(input("Enter your number: "))
if num%2==0:
  print("Even")
else:
  print("Odd")
  
num=-5
if num>=0:
  print("Positive")
else:
  print("Negetive")
  

#5.Mini calculator with all operator
a=10
b=20
print("additiona",a+b)
print("substriction",a-b)
print("division",a/b)
print("multiplication",a*b)
print("modulus",a%b)
print("exponention",a**b)
print("floor division",a//b)
