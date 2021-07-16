## Here will go the List Methods

## Use [ ] and are ordered, mutable and allows duplicate elements

my_list = ['cat', 'dog', 'fish']
print(my_list)
# print = ['cat', 'dog', 'fish']


## .append() = adds an element at the end of the list

my_list.append('cow')
print(my_list)
# print = ['cat', 'dog', 'fish', 'cow']


## .clear() = removes all the elements from the list

my_list.clear()
print(my_list)
# print = []


## .copy() = returns a copy o the list

list_copy = my_list.copy()
print(list_copy)
# print = ['cat', 'dog', 'fish', 'cow']


# .count() = returns the number of elements with the specified value

count = my_list.count('cat')
print(count)
# print = 1


#.extend() = add the elements of list, to the end of the current list

my_list_1 = ['snake', 'pig']
my_list.extend(my_list_1)
print(my_list)
# print = ['cat', 'dog', 'fish', 'cow', 'snake', 'pig']


# .index() = returns the index of the first element with specified value

index = my_list.index('dog')
print(index)
# print = 1


# .insert() = adds an element at the specified position

my_list.insert(3, "tiger")
print(my_list)
# print = ['cat', 'dog', 'fish', 'tiger', 'cow', 'snake', 'pig']


# .pop() = returns and removes the element the last item

my_list.pop()
print(my_list)
# print = ['cat', 'dog', 'fish', 'tiger', 'cow', 'snake']


# .remove() = remove a specific element

my_list.remove('cow')
print(my_list)
# print = ['cat', 'dog', 'fish', 'tiger', 'snake']


# .reverse() = reverses the order of the list

my_list.reverse()
print(my_list)
# print = ['snake', 'tiger', 'fish', 'dog', 'cat']


# .sort() = sort the list

my_list.sort()
print(my_list)
# print = ['cat', 'dog', 'fish', 'snake', 'tiger']