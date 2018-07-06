# 8K to 7K naive conversion
# Remember to change .osu to .txt if you are working directly on osu file

import re

def move(tokens):
    ''' takes a line of 8K format tokens and returns in 7K formats(deleting the sp column). '''
    new = []
    temp = re.split(',', tokens)
    if int(temp[0]) == 96:
        temp[0] = '36'
    elif int(temp[0]) == 160:
        temp[0] = '109'
    elif int(temp[0]) == 224:
        temp[0] = '182'
    elif int(temp[0]) == 288:
        temp[0] = '256'
    elif int(temp[0]) == 352:
        temp[0] = '329'
    elif int(temp[0]) == 416:
        temp[0] = '402'
    elif int(temp[0]) == 480:
        temp[0] = '475'

    t = ''
    for part in temp:
        t += part + ','

    new.append(t[:-1]) # remove if you don't want hitsound

    line = ''
    for i in new:
        line += i
        
    return line

filename = "6yen  G   - Cynic(THE another) (Degeneracy) [Lv.22].txt" # Change as needed
file = open(filename, "r")
newfile = "[7K]" + filename
output = open(newfile, "w+")
for line in file:
    newline = move(line)
    output.write(newline)

file.close()
output.close()
print("Done.\n")
