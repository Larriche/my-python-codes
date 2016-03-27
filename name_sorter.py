# Author - Richman Clifford
# A small program that reads names.txt which contains
# a collection of names in unordered manner(probably of people
# in an organisation),arranges the names in alphabetical order
# and writes it back to the file.
#
# I actually wrote this script to re-order the names of my
# classmates which were in random fashion in a text file
 

data_src = open("names.txt")

names = []

data = data_src.read()
data_src.close()

for i in data.split("\n"):
    names.append(i)

names.sort()

output = ""
for i in names:
    output += i + "\n"

out_file = open("names.txt","w")
out_file.write(output)
out_file.close()
