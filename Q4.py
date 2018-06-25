f = open("allbp.data")
data = f.read()
lines = data.split('\n')

# print(len(lines[0].split(',')))
attr = len(lines[0].split(','))
count = [0]*attr
total = len(lines)

def roundUp(x):
    if x == '?':
        return 0
    x = float(x)
    if (x-int(x))<=0.5:
        x = int(x)
    else:
        x = int(x+0.5)
    return x

for line in lines:
    x = line.split(',')
    if(len(x)<30):
        continue
    x[17] = roundUp(x[17])
    x[19] = roundUp(x[19])
    x[21] = roundUp(x[21])
    x[23] = roundUp(x[23])
    x[25] = roundUp(x[25])

    for each in x:
        print(str(each)+',',end='')
    print('')
    