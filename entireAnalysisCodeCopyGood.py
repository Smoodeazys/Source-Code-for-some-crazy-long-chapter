"""
This is the entire section of Analysing summarised
Please note that you can't actually just copy everything and slam it into your IDE
They're all here, you just need to find which one you actually need
Enjoy : )

"""



""" Finding MIN and MAX values ------------------------------------------------------------------------------------------------------------------ > """

list = [1, 19, 27, 8, 5, 9]
min = list[0]
max = list[0]
for item in list:
    if item < min:
        min = iteam
    elif item > max:
        max = item


print(min) #output 1
print(max) #output 27

""" Calculating Mean >> Manual Method and Cheesy ( statistics module ) method <<  ------------------------------------------------------------------------------------------------------------------ > """

# Manual Method

list = [1, 19, 27, 8, 5, 9]
sum = 0
for item in list:
    sum += item

avg = sum/ len(list)
print(avg) # output 11.5
 
 # Of course, we need the cheesy method of doing it
 
import statistics
list = [1, 19, 27, 8, 5, 9]
avg = statistics.mean(list)
print(avg) # output 11.5

""" Calculating Median >> Manual Method and Cheesy ( statistics module ) method <<  ------------------------------------------------------------------------------------------------------------------ > """

# Manual Method

list = [1, 19, 27, 8, 5, 9]
list.sort()
if (len(list) % 2 ) == 0:
    middle = len(list) // 2
    median = (list[middle - 1] + list[middle]) /2
else:
    middle = len(list) // 2
    median = list[middle]

print(median) # ouput 8.5
 
# Of course, we need the cheesy method of doing it

import statistics

list = [1, 19, 27, 8, 5, 9]
median = statistics.median(list)
print(median) # output 8.5 

""" Calculating Mode ( although the mode and frequency have very similar code, with a slight difference ) >> Manual Method and Cheesy ( statistics module ) method <<  ------------------------------------------------------------------------------------------------------------------ > """
  
# Manual Method

list = ["red", "blue", "blue", "red", "green", "red", "red"]

colors = []
colorCount = []

for item in list:
    if item not in colors:
        colors.append(item)
for color in colors:
    total = list.count(color)
    colorCount.append(total)

print(colors) # output ['red', 'blue', 'green']
print(colorCount) #output [4, 2, 1]

#                                            But that's just frequency, so lets actually find the mode now

# using the same code as above but adding a few extra lines...

maxFreq = max(colorCount)
maxFreqIndex = colorCount.index(maxFreq)
mode = colors[maxFreqIndex]
print(mode) # prints red

""" Yeah, that's pretty much it to be honest """

