#sets

# once a set is created, you cannot change its items, but you can add new items.
# this is one of the four data types --> see basic

set = {"apple", "banana", "cherry"}
print(set)

# You cannot access items in a set by referring to an index or a key.
# you need to use a for loop
for item in set:
  print(item)


print("banana" in set) # prints true 

print("banana" not in set) # prints false

# how to add an item

set.add("orange")
print(set)

# add items from one set into another  !!Messed up existing order!! 

newset = {"pineapple", "mango", "papaya"}
set.update(newset)
print(set)

# you can also add tuples, lists and dictionaries

mylist = ["kiwi", "Pear"]
set.update(mylist)
print(set)

# you can remove an item using .remove or .discard

set.remove("orange") # .remove will raise an error if the item doesnt exist, .discard will not 
print(set)

# or a random item (value stored in .pop)

removedItem = set.pop()
print(removedItem)
print(set)


# clear all items from the set

set.clear()
print(set)

# del will delete the set completely

del set
print(set)

# How to freeze my set 

# you can change frozenSet to whatever you like

frozenSet = frozenset(set)