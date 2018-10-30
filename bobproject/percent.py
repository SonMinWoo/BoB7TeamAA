import csv
import pandas as pd

"""
malicious app : 1997 (error : 2)
normal app : 4000
all app : 5997
"""
nogrouplist = []
dividelist = []
countcorrect = []
correct = []
countdivide = []

f = open('ja15\\analysislist_all.csv', 'r', encoding='utf-8')
csvdata = csv.reader(f)
base = [row for row in csvdata]
f.close()
mapcount=[]
print(len(base))

for i in range(2,5998):
# row 2 ~ 1998 : malicious app, 1999~5998 : normal app, 0,1 and 5999 is index
    napp, mapp = 0, 0
    print(i)
    if(base[i][1] != ""):
        for j in range(1, len(base[i])):
            #mal : 0~1996 , nor : 1997~5996
            if(base[i][j] == ""):
                pass
            else:
                if(float(base[i][j]) <= 1996):
                    mapp = mapp+1
                else:
                    napp = napp+1

        if(float(base[i][0]) <= 1998):
            correct.append(float(mapp))
            countcorrect.append(float(napp))
            mapcount.append('m')

        else:
            correct.append(float(napp))
            countcorrect.append(float(mapp))
            mapcount.append('n')

    else:
        nogrouplist.append(i-1)

lnogroup = len(nogrouplist)

for i in range(len(correct)):
    x = correct[i] + countcorrect[i]
    if(mapcount[i] == 'm'):
        dividelist.append((correct[i]/x)*(3.0/2.0)*100)
    else:
        dividelist.append((correct[i]/x)*(2.0/3.0)*100)
#    countdivide.append((countcorrect[i]/x)*100)
    print(x)


nine, eight, seven, six, five, four, three, two, one, down = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in dividelist:
    if (i >= 90):
        nine = nine+1
    elif (80 <= i < 90):
        eight = eight+1
    elif (70 <= i < 80):
        seven = seven+1
    elif (60 <= i < 70):
        six = six+1
    elif (50 <= i < 60):
        five = five+1
    elif (40 <= i < 50):
        four = four+1
    elif (30 <= i < 40):
        three = three+1
    elif (20 <= i < 30):
        two = two+1
    elif (10 <= i < 20):
        one = one+1
    else:
        down = down+1
dsum = 0.0
for i in dividelist:
    dsum = dsum+i
ldlist = float(len(dividelist))
avg = dsum/ldlist
frame = pd.DataFrame(dividelist)
frame.to_csv('correctpercentlist.csv', sep=',')


print("No group : %d" % (lnogroup))
print("nine : %d\neight: %d\nseven: %d\nsix:%d\nfive:%d\nfour:%d\nthree:%d\ntwo:%d\none:%d\ndown:%d\n" % (nine, eight, seven, six, five, four, three, two, one, down))
print("Average correct : %f" %(avg))
