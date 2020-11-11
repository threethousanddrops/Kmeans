import matplotlib.pyplot as plt

colour = ['cyan', 'plum', 'brown', 'yellow', 'Thistle', 'green', 'HotPink', 'plum', 'red']

output = []
with open("outputk6.txt", "r") as inf:
    for information in inf.readlines():
        information = information.strip('\n')
        r1 = information.split(",")
        r2 = r1[1].split("\t")
        res = [r1[0], r2[0], r2[1]]
        output.append(res)

n = len(output)
clusternum = 0
for i in range(n):
    output[i][0] = int(output[i][0])
    output[i][1] = int(output[i][1])
    output[i][2] = int(output[i][2])
    if(output[i][2]> clusternum):
        clusternum = output[i][2]

for i in range(clusternum):
    x = []
    y = []
    for j in range(n):
        if(output[j][2]==(i+1)):
            x.append(output[j][0])
            y.append(output[j][1])
    plt.scatter(x, y, color=colour[i], label="cluster "+str(i+1))

plt.legend(loc='lower left')
plt.show()


