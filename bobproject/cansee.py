import matplotlib.pyplot as plt
import csv

bins = [x*10 for x in range(10)]
f = open('ja15\\correctpercentlist.csv', 'r', encoding='utf-8')
csvdata = csv.reader(f)
distancedata = [row for row in csvdata]

f.close()

ydata = [0,0,0,0,4785,771,0,0,0,0]
"""
for i in range(2, len(distancedata)-1):
    histo.append(int(distancedata[i][1]))
"""

plt.bar(range(len(ydata)), ydata, width=1)
"""
tick_val = [0,10,20,30,40,50,60,70,80,90,100]
tick_lab = ['0','10','20','30','40','50','60','70','80','90','100']
plt.xticks(tick_val,tick_lab)
"""
plt.show()
