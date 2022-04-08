"""
This is the entire Pre-Processing chapter summarised
Please note that you can't actually just copy everything and slam it into your IDE
They're all here, you just need to find which one you actually need
Enjoy : )

"""

""" Sorting ------------------------------------------------------------------------------------------------------------------ > """

list = [1, 19, 27, 8, 5, 9]

list.sort()
print("Sorting ascending...", list) # output: Sorting ascending... [1, 5, 8, 9, 19, 27]
list.sort(reverse = True)
print("Sorting descending...", list) # output: Sorting descending... [27, 19, 9, 8, 5, 1]

""" Removing Data ------------------------------------------------------------------------------------------------------------------ > """

# Just a method of removing all negative Values

list = [1, -19, 27, 8, -5, 9]

for item in list:
    if item < 0:
        list.remove(item)

print(list) # output: [1, 27, 8, 9]

""" Imputation ------------------------------------------------------------------------------------------------------------------ > """

# A code that leaves negative values and calculates the average of the postive numbers
non0 = 0
coutNon0 = 0

list = [1, -19, 27, 8, -5, 9]
for item in list:
    if item >= 0:
        totalNon0 += item
        countNon0 += 1
avgNon0 = totalNon0/countNon0

print(avgNon0)
