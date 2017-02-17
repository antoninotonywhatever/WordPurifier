import re
frequency = {}
unique = {}
book = open("huckleberry.txt", "r", encoding="utf8")
out1 = open("allwords.txt", "w")
out2 = open("uniquewords.txt", "w")
out3 = open("wordfrequency.txt", "w")
for line in book:
    split = line.split()
    for i in range(0, len(split)):
        split[i] = split[i].lower()

        split[i] = re.sub(r'_','',split[i])
        split[i] = re.sub(r'[^\w]','',split[i])


        out1.write(split[i] + '\n')
        if unique.get(split[i]) == None:
            unique[split[i]] = 1
            out2.write(split[i] + '\n')

        else:
            unique[split[i]] += 1

for key, value in unique.items():
    if frequency.get(unique[key]) == None:
        frequency[unique[key]] = 1
    else:
        frequency[unique[key]] += 1
for key,value in frequency.items():
    out3.write(str(key) + ": " + str(frequency[key]) + "\n")

