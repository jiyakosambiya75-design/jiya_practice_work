# Control flow in python
# Statement in python
'''
1.if statement
2.if...else statement
3.if.elif.else statement
4.match statement
5.continue statement
6.break statement
'''
#The if statement executes a block of code only if specified condition is true if the condition is false the code inside the if block is skipped.
'''
if condition
  #code
'''
age=20
if age>=18:
 print("Your Eligible to vote")
#the if...else statement is used when they are two possible outcomes:
#if the condition is true the if block executes:
#if the condition is false the else block execute:
 '''
if condition:
   #code(True)
else:
   #code(False)
'''
number=-5
if number>=0:
    print("Positive number")
else:
    print("Negative number")
#if...elif...else statement
#if.elif.else statement is used when multiple condition need to be chaked
'''
if condition1:
   #code
elif condition2:
   #code
elif condition3:
   #code
else:
   #code
'''
marks=82
if marks>=90:
   print("Grade A")
elif marks>=75:
   print("Grade B")
elif marks>=60:
   print("Grade C")
else:
   print("Fail")
#match-case statement
num1=10
num2=5

operator="+"
match operator:
  case"+":
   print("Adition:",num1+num2)
  case"-":
   print("Substriction:",num1-num2)
  case"/":
   print("Divition:",num1/num2)
  case"*":
   print("Multiplication:",num1*num2)
  case _:
   print("Invalid Operater")
#Multiple value in one case use
char="a"
match char:
    case"a"|"e"|"i"|"o"|"u":
        print("Vowel")
    case _:
        print("Consoents")
