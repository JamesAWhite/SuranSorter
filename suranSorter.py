import fileinput

#take file input
arrayToSort = [];

for line in fileinput.input():
    arrayToSort.append(line.rstrip())

#sort alphabetically
arrayToSort.sort()

#sort by length
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
