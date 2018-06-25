f = open("./Data/completeDataset.txt")
data = f.read()
lines = data.split('\n')

# print(len(lines[0].split(',')))
attr = len(lines[0].split(','))
count = [0]*attr
total = len(lines)

for line in lines:
    lst = line.split(',')
    for x in range(len(lst)):
        if lst[x] != '?':
            count[x] = count[x]+1

for x in range(attr):
    count[x] = 100*(count[x]/float(total))

print(count)