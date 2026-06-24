#python basics
#print your name
'''
print("Hello, my name is jiya")
#add two number
a=5
b=10
sum=a+b
print("the sum is : ",sum)
 #ask users name
name = input("What is your name : ")
print(name)
'''
'''
#simple calculater
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
print("addition :", a+b)
print("substraction :", a-b)
print("Multipication :", a*b)
print("divison :", a/b)


#print()formting using sep and end
print("Apple","banana","cherry",sep = "|",end="<---End of list\n")


#formating msg from user input
name =input("Enter your name:")
age =int(input("Enter your age:"))
hobby =input("Enter your favourit hobby: ")


#f-string
print(f"Hello,{name},At{age},enjoying{hobby}sounds fun!!")

#declare variable of diffrent data type and show their types
a = 10
b = 3.14
c = "python"
d = True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
'''
#pythn program
subject1 = input("Enter 1st subject name:")
marks1 = int(input("enter your marks: "))

subject2 = input("Enter 2nd subject name:")
marks2 = int(input("enter your marks: "))

subject3 = input("Enter 3rd subject name:")
marks3 = int(input("enter your marks: "))


 
total = marks1 + marks2 + marks3
average = total/3
#deside grade
if average>=90:
   grade ="A"
elif average>=75:
     grade = "B"
elif average>=60:
     grade ="C"
elif average>=40:
     grade ="D"
else:
    graade ="fail"
    
print("\n---------Result---------")

print(f"{subject1}:{marks1}")
print(f"{subject2}:{marks2}")
print(f"{subject3}:{marks3}")
print(f"Total Marks:{total}")
print(f"Grade: {grade}")

