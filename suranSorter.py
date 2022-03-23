import fileinput, argparse

parser = argparse.ArgumentParser(description= "Test")

#add argument for file name
parser.add_argument("filename")
#add argument for reverse sorting
parser.add_argument("-r", "--reverse", help = "Sort in reverse order of length.", action = "store_true")

args = parser.parse_args()

#take file input
arrayToSort = [];

for line in fileinput.input(args.filename):
    arrayToSort.append(line.rstrip())

#sort alphabetically
arrayToSort.sort()

#sort by length
#sort in descending order
if args.reverse:
    for index in range(0, len(arrayToSort)):
        currentName = arrayToSort[index]
        position = index

        while position >= 1 and len(arrayToSort[position - 1]) < len(currentName):
            arrayToSort[position] = arrayToSort[position - 1]
            position = position - 1
            
        arrayToSort[position] = currentName
#sort in ascending order
else:
    for index in range(0, len(arrayToSort)):
        currentName = arrayToSort[index]
        position = index

        while position >= 1 and len(arrayToSort[position - 1]) > len(currentName):
            arrayToSort[position] = arrayToSort[position - 1]
            position = position - 1
            
        arrayToSort[position] = currentName

#write to file
file = open("Sorted Names.txt", "w")
for name in arrayToSort:
    if len(name) > 0:
        file.write("\n")
        file.write(name)
file.close
