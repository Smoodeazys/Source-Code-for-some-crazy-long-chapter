"""
This is the entire section of Visualisation summarised
Please note that you can't actually just copy everything and slam it into your IDE
They're all here, you just need to find which one you actually need
Enjoy : )
"""

""" Using Pie charts to display data ------------------------------------------------------------------------------------------------------------------ > """

import matplotlib.pyplot as plt
num = [1, 2.5, 4, 3, 2.5, 2]
names= ["Kyotsu 1", "Kyotsu 2", "Kyotsu 3", "Kyotsu 4", "Kyotsu 5", "Gerog and cills"]
plt.pie(num, labels=names)
plt.title("Different Kyotsus + random")
plt.show() # output is in one of the file folders


""" Using Bar charts to display data ------------------------------------------------------------------------------------------------------------------ > """

import matplotlib.pyplot as plt
num = [1, 2.5, 4, 3, 2.5, 2]
names= ["Kyotsu 1", "Kyotsu 2", "Kyotsu 3", "Kyotsu 4", "Cillians naillic", "Gerog Conpaku"]
plt.bar(names,num)
plt.title("Kyotsus, Cillians, and Conpakus")
plt.xlabel("Kyotsus, Cillians, and Conpakus")
plt.ylabel("Numbers :(")
plt.show()

