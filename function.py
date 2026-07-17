# global keyword in python
total=0
def increment():
    global total
    total+=1
increment()
increment()
increment()
print(total)

#Multiple return value
def calculation(a,b,c):
    total=a+b+c
    average=total/3
    maximum=max(a,b,c)
    minimum=min(a,b,c)
    return total,maximum,average,minimum
total,average,maximum,minimum = calculation(10,20,30)
print(total)
print(average)
print(maximum)
print(minimum)
