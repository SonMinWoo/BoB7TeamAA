import csv
import pandas as pd

f = open('jaccard_distance_all.csv', 'r', encoding='utf-8')
csvdata = csv.reader(f)
base = [row for row in csvdata]
f.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
a = [[] for i in range(5997)]
zeros = 0
zerolist = []
                                                                                                                                                                                                                                                                                    
for i in range(1, 5997):
    for j in range(1, len(base[i])):
        if(base[i][j] == ""):
            pass
        else:
            if(float(base[i][j])==0):
                zerolist.append(base[i][j])
                zeros = zeros+1
            elif(float(base[i][j])<0.15):
                a[i].append(j)
            else:
                pass
    print(i)

frame = pd.DataFrame(a)
frame.to_csv('analysislist_all.csv', sep=',')
