import json

# define list with values
basicList = [[1, "Cape Town", 4.6],[1, "Cape Town", 4.6],[1, "Cape Town", 4.6],[1, "Cape Town", 4.6],[1, "Cape Town", 4.6]]

# open output file for writing
import json
with open('listfile.txt', 'w') as filehandle:
    json.dump(basicList, filehandle)
"""    
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile.txt', 'w') as filehandle:
    for listitem in places:
        filehandle.write('%s\n' % listitem)
"""

# open output file for reading
with open('listfile.txt', 'r') as filehandle:
    basicList = json.load(filehandle)
"""
placess = []
with open('listfile.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        places.append(currentPlace)
"""
print(basicList)
