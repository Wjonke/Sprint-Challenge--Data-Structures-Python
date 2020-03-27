import time
from binary_search_tree import BinarySearchTree

# base time to run for me is 9ish seconds with 0 modifications
# this function has a run time of O(n^2)
# after modification we are running consecutive for loops through our binary search which itself is O(N)
# each for loop is O(N) so O(N+N)
# at the end of the day, new Big O is still O(N)
# now it runs in about .15 seconds

# binary search tree to optimize?

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

'''
You may not use the built in Python list, set, or dictionary in your solution 
for this problem. However, you can and should use the provided duplicates list to 
return your solution.

'''

# Replace the nested for loops below with your improvements

binary = BinarySearchTree('names')
# insert each name from list 1
for a in names_1:
    binary.insert(a)

# compare each name from second list to each name in first
# if present, add to the list of dupes
for b in names_2:
    if binary.contains(b):
        duplicates.append(b)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)









end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
