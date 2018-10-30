import csv
import pandas as pd
import matplotlib.pyplot as plt


f = open('normal_api_list.csv', 'r', encoding='utf-8')
csvdata = csv.reader(f)
base = [row for row in csvdata]
f.close()

m = open('C:\\Users\\SonMinWoo\\Documents\\카카오톡 받은 파일\\malware_api_output.csv', 'r', encoding='utf-8')
mdata = csv.reader(m)
mmdata = []
for row in mdata:
    mmdata.append(row)
m.close()

n = open('C:\\Users\\SonMinWoo\\Documents\\카카오톡 받은 파일\\normal_api_output.csv', 'r', encoding='utf-8')
ndata = csv.reader(n)
nndata = []
for row in ndata:
    nndata.append(row)

n.close()


count = []
ncount = 0
big = 0
cumul = 0
a = 0
add = 0
adds = []
zocount = 0
for i in range(1, 4001):
    add=0
    ncount = 0
    temp = list(base[i][2])
    for j in range(len(temp)):
        if (temp[j] == '1'):
            ncount = ncount+1
            if(float(nndata[0][zocount]) != 0):
                add = add+(float(mmdata[0][zocount])/float(nndata[0][zocount]))
            zocount = zocount+1
        elif (temp[j] == '0'):
            zocount = zocount+1

    adds.append(add)
    cumul = cumul + ncount
    count.append(ncount)
    zocount=0

for i in count:
    if (i > big):
        big = i
    if (i >= 14):
        a = a+1

print(77*0.9)
nine, eight, seven, six, five, four, three, two, one, down = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in count:
    if (i >= 77*0.9):
        nine = nine+1
    elif (77*0.8 <= i < 77*0.9):
        eight = eight+1
    elif (77*0.7 <= i < 77*0.8):
        seven = seven+1
    elif (77*0.6 <= i < 77*0.7):
        six = six+1
    elif (77*0.5 <= i < 77*0.6):
        five = five+1
    elif (77*0.4 <= i < 77*0.5):
        four = four+1
    elif (77*0.3 <= i < 77*0.4):
        three = three+1
    elif (77*0.2 <= i < 77*0.3):
        two = two+1
    elif (77*0.1 <= i < 77*0.1):
        one = one+1
    else:
        down = down+1

print(nine, eight, seven, six, five, four, three, two, one, down)
ydata = [nine, eight, seven, six, five, four, three, two, one, down]
plt.bar(range(len(ydata)), ydata, width=1)
plt.show()


print(big)
print(cumul)
print(a)
print("Average : %f" %(cumul/4000))
frame = pd.DataFrame(count)
frame.to_csv('normal_api_count.csv', sep=',')
frame2 = pd.DataFrame(adds)
frame2.to_csv('normal_gahung.csv', sep=',')
