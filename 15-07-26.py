# python functions
#built in functions

print("="*20)
print("functions with Python")
print("="*20)

numbers=[1,10,20,30,40]

print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(sum(numbers))

print("="*20)
print("UDF functions")
print("="*20)
 
def add(a,b):
    print(a+b)

add(10,30)

'''
1.Reusability
2.Cleanner Code
3.Batter Organization
4.Reduce repetition
'''
print("="*20)
print("Recursion")
print("="*20)
#a function calling itself.
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#sum of numbers
def total(n):
    if n == 0:
        return 0
    return n + total(n-2)
print(total(10))

#Anonymous Function lambda functions
square=lambda x : x * x
print(square(10))

add=lambda x,y : x+y
print(add(12,34))

mul=lambda a,b : a*b
print(mul(12,4))
