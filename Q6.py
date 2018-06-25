import matplotlib.pyplot as plt

f = open("allbp.data")
data = f.read()
lines = data.split('\n')

X = []
Y = []

for line in lines:
    temp = line.split(',')
    if len(temp)<22:
        continue
    print(temp)
    if temp[0]!='?' and temp[21]!='?':
        X.append(int(temp[0]))
        Y.append(float(temp[21]))

plt.plot(X,Y)
plt.show()  