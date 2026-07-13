'''
print("Introduction & Fundamrntals")

#Introduction & fundamental
#1.
print("Name : Jiya ")
print("Age : 18 ")
print("City : Surat ")

#2.
name=(input("Enter your name : "))
print(f"'Hello, [{name}]! Welcome to Pythpn!'")

#3.
num=int(10)
num2=float(20)
num3=bool(100)
print(type(num))
print(type(name))
print(type(num2))
print(type(num3))

#4.
a=10
b=20
c=10
print(id(a))
print(id(b))
print(id(c))
'''
'''
#5.
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print("Addition: " , a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Devision: ", a/b)
print("Modulus: ", a%b)
print("Exponemtion: ", a**b)
print("Floor division: ", a//b)
'''
'''
#6.
float1=12.14
float2=int(float1)
print(type(float2))
int1=2
int2=str(int1)
print(type(int2))
str1="jiya"
str2=float(int1)
print(type(str2))
'''
'''
#7.
C=int(input("Enter temperature in calcius: "))
F=(C*9/5)+32
print("Temperature in fahrenheit: ", F)
'''
print("Control & Looping")
#1.
'''
num=int(input("Enter a number: "))

if num>0 :
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
'''
#2.
marks=67
if marks>=90:
  print("Grade A")
elif marks>=75:
  print("Grade B")
elif marks>=60:
  print("Grade C")
else:
  print("Grade D")



