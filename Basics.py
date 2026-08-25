from idlelib.autocomplete_w import LISTUPDATE_SEQUENCE
from selectors import SelectSelector

a=1;
b=5;
if a>b:
    print("hello")
elif a==b:
    print("ok")
else:
 print("hi");


 #LIST
fruits = ["apple", "banana", "peach", "mango"]
#print(fruits)
print(fruits[0]);
print(fruits[1]);
print(fruits[2]);

# add item to the list
fruits.append("grapes")
print(fruits)
# Remove item
fruits.remove("peach")
print(fruits)

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
