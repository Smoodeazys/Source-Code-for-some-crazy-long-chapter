"""
This is the entire section of Accessing Data summarised
Please note that you can't actually just copy everything and slam it into your IDE
They're all here, you just need to find which one you actually need
Enjoy : )
"""

""" Making a text file and Reading data off it ------------------------------------------------------------------------------------------------------------------ > """
file = open("myFirstTxtFile", "w")

file.write("Test text")
file.close()

# this is the code for reading from the .txt file
file = open("myFirstTxtFile", "r")
data = file.read()
file.close()
print(data) # output: Test text