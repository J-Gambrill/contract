# basics

food = 'nice'

print ('Hello World')

if 5 < 2: 
    print('shut up liar')


# Multiple values to multiple variables

x, y, z = 1, 2, 3

print(x, y, z)
    # prints (1  2  3)

print(x)
print(y)
print(z)
    #prints on separate lines
    #1
    #2
    #3


# One value to multiple variables

x = y = z = 1


#Unpacking (an array --> variables)

# Array called fruits

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x) #'apple'
print(y) #'banana'
print(z) #'cherry'


#functions
def myfirstfunc():
    global x            # variables created within a function are local stating global changes this 
    x = 'fantastic'

myfirstfunc() # prints fantastic

print("python is " + x) # without the global from earlier would result in an error


#lists

fruits = ["apple", "banana", "cherry"]  # Strings
numbers = [1, 2, 3, 4]  # Integers
mixed = [1, "hello", 3.14]  # Mixed types
empty = []  # Empty list

#indexing

print(fruits[-2])  
print(fruits[-1])  
print(fruits[0]) # 'apple'
print(fruits[1])
print(fruits[2])

#updating
fruits[1] = "blueberry"  # Changes "banana" to "blueberry"

#adding
fruits.append("orange") # adds to end of list
fruits.insert(1, "grape")  # Adds "grape" at index 1

#deleting
fruits.remove("apple") # finds matching item in list and deletes it
del fruits[0] # deletes by index
fruits.pop()  # Removes and returns the last item


#find list length
print(len(fruits))

#combine lists
new_list = fruits + numbers


#slicing
print(fruits[1:3])  # Elements from index 1 to 2
print(fruits[:2])   # First two elements
print(fruits[2:])   # From index 2 to the end


#methods
fruits.sort()
print(fruits.index("cherry"))

#sort(): Sorts the list in place
#reverse(): Reverses the list
#index(value): Finds the first occurrence of a value
#count(value): Counts occurrences of a value


#loops

#while

i=10
while i <= 15: 
    print(i)
    i += 1

#for

# look at a for loop as being for items in sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#double array of NO's using loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]
for number in numbers:
    doubled = number * 2
    print (doubled)

#tuples
Years = (2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)

#dictionaries

mycar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mycar)

#function
def compare(num_1, num_2):
    if num_1 > num_2:
        print('num1 is bigger')
    elif num_1 < num_2:
        print('num2 is bigger')
    else:
        print('They are equal')

try:
    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))

    compare(num_1, num_2)

except ValueError:
    print('It said number you melon')


#modules

import platform #platform is an in-built module

x = dir(platform) # the dir function can be use on all modules even those you have created yourself
print(x)


#function using module

import Module1

name = str(input('Enter your name: '))
print(Module1.Greeting(name))