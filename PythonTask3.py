#Section 1 : loob Basics
for i in range(1,51):
    print( i, end=" ")

print("\t")

for i in range(2,101,2):
    print(i, end=" ")

print("\t")

for i in range(1,101,2):
    print(i, end=" ")

print("\t")

for i in range(1,11):
    print("7 x",i, "=", 7*i)

print("\t")

total=0
for i in range(1,101):
    total += i
    print(total,end=" ")

print(" ")

for i in range(50,0,-1):
        print(i, end=" ")

print("\t")

count=0
for i in range(1,101):
    if i % 3 ==0:
        count +=1
print(count)

print("\t")

for i in range(1,11):
    print(i*i, end=" ")

print("\t")

for i in range(1,11):
    print(i**3, end=" ")

print("\t")

n=int(input("Enter any number or type stop"))
for i in range(1,n+1):
    print(i)

print("\t")

#Section 2:While loop
i=1
while i <= 20:
    print(i)
    i+= 1

print("\t")

num=5
fact=1
i=1
while i <= num:
    fact=fact * i 
    i += 1
print("factorial:", fact)

print("\t")

num=123
rev=0
while num>0:
    rev= rev*10+(num%10)
    num=num//10    
print("revers using while:",rev)



num=12345
count=0
while num > 0:
    num=num // 10
    count = count + 1  
print(count)

print("\t")

while True:
    user_input=input("Enter Somthing:")
    if user_input=="stop":
        break

#Nested loop

for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end="")
    print()

for i in range(1,6):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}",end="\t")
    print()

for i in range(3):
    for j in["A","B","C"]:
        print(j,end=" ")
    print()

num=1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num += 1
    print()

#String basic
 
name=("Vishnukarthick")
print("count charaters in name",len(name))

name=("VishnukarthIck")
vowels="aeiouAEIOU"
count=0
for char in name:
    if char in vowels:
        count += 1
print("Count vowels",count)

name="Superman"
count=0
for char in name:
    if char.isalpha() and char not in("aeiouAEIOU"):
        count += 1
print("count consonats in superman",count)

name="KARTHICK"
reverse =""
for char in name:
    reverse =char + reverse
print(reverse)

name="level"
reverse=""
for char in name:
    reverse=char+reverse
if name == reverse:
    print("it is palindrome")
else:
    print("Not palindrome")

#Strinf Slicing

name="Kavinkumar"
print(name[0:5])

name="Kavinkumar"
print(name[-3:])

name="Kavinkumar"
print(name[::-1])

name="Kavinkumar"
print(name[::2])

name="Kavinkumar"
print(name[1:-1])

maths_marks=[50,40,30,20,10]
total = sum(maths_marks)
print("sum:",total)

maths_marks=[50,40,30,20,10]
total = max(maths_marks)
print("maximum:",total)

maths_marks=[50,40,30,20,10]
total = min(maths_marks)
print("minimum:",total)

maths_marks=[50,40,30,20,10]
print("count elements:",len(maths_marks))

marks=[50,40,30,20,10]
if 30 in marks:
    print("30 exist in list")
else:
    print("30 does not exist")

#list operations

numbers = [10,20,30]
numbers.append(40)
numbers.append(50)
numbers.append(60)
print(numbers)

numbers = [10,20,30,40]
numbers.insert(2,25)
print(numbers)

numbers = [10,20,30]
numbers.remove(20)
print(numbers)

numbers = [10,20,30,40,50]
reversed_list=numbers[::-1]
print(reversed_list)

numbers= [40,50,20,10,30]
sorted_list=sorted(numbers)
print(sorted_list)
