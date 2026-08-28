#Variables
x=5
y="john"
print(type(x))
print (type(y))

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Data_Types
b = "Hello, World!"
print(b[:5])
print(b[2:5])
print(b[2:])

#Negative indexing
b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip())
#split
a = "Hello, world!"
print(a.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno, price ))

#python_operator

#python_if else condition
a=6
b=4
if b>a:
    print("hi")
elif a==b:
 print("haha")
else:
    print("nice")

 #ifnot
e = 5
t = 4

if not t > e:
    print("correct")




 #LIST
fruits = ["apple", "banana", "peach", "mango"]
#print(fruits)
print(fruits[0]);
print(fruits[1]);
print(fruits[2]);
print(fruits);

# add item to the list
fruits.append("grapes")
print(fruits)
# Remove item
fruits.remove("peach")
print(fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)





# RAM store byte
# offset = index*element_size(4 Byte)
# Address = 1000 + 8
#         =1008;



# Dictionary
# stores values in key value pair
man={
    "name": "ram",
    "age": "21",
    "city": "aus"
}

print(man["age"])

nums = [1, 2, 3]

for num in nums:
    print(num)


x = lambda a : a + 10
print(x(5))
