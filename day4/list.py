states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina"]

print(states_of_america[0])
print(states_of_america[-1])

#change the item in to a list
states_of_america[4] = "hawaii"

#Add an item to the end of the list.
states_of_america.append("anushkalondon")

#Extend the list by appending all the items from the iterable
states_of_america.extend(["anu", "phieria", "classy"])

#Insert an item at a given position. T
# he first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)
states_of_america.insert(1, "london")


#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item
states_of_america.remove("hawaii")

#Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
# It raises an IndexError if the list is empty or the index is outside the list range
print(states_of_america)
states_of_america.pop()

#Remove all items from the list. Similar to del a[:].
states_of_america.clear()

print(states_of_america)