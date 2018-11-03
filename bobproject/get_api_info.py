import os
from api_dict import *
from parse_dex import *
import csv
import pandas as pd
import itertools
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard

def get_api_info(PATH):
    count = 0
    result = {}
    filenames = os.listdir(PATH)
    prt_api = {}
    for filename in filenames:
        count = count+1
        print(count)
        temp_dict = {}

        for i in suspicious_api_dict:
            name = i
            temp_list = [0 for i in range(len(suspicious_api_dict[i]))]
            temp_dict[name]= temp_list

        try:
            fp = open(PATH+"/"+filename+"/"+'classes.dex','rb')
        except IOError as e:
            result[filename] = [-1 for i in range(78)]
            continue
        mm = fp.read()
        fp.close()
        hdr = header(mm)

        string_ids = string_id_list(mm, hdr)
        type_ids = type_id_list(mm, hdr)
        method_ids = method_id_list(mm, hdr)

#        print(filename)
        list_api = []
        for i in range(len(method_ids)):
            (class_idx, proto_idx, name_idx) = method_ids[i]
            class_str = string_ids[type_ids[class_idx]]
            name_str = string_ids[name_idx]
            list_api.append([class_str[1:], name_str])
            prt_api[class_str[1:]] = name_str.lower()
#            print('[file : %s, class : %s, name : %s, method : %s]' % (filename, class_str[1:], name_str,method_ids[i]))
            for i in suspicious_api_dict:
                if class_str[1:].lower().find(i.encode('utf-8')) != -1:
#                    print("found", class_str[1:], i.encode())
                    if 'NONE' in suspicious_api_dict[i]:
#                        print('NONE')
#                        print("front back:",i, 'NONE')
                        temp_dict[i][suspicious_api_dict[i].index('NONE')]=1
                    if name_str.lower().decode('utf-8', errors = "ignore") in suspicious_api_dict[i]:
#                        print("front back:",i, name_str)
#                        print(suspicious_api_dict[i].index(name_str.lower()))
                        temp_dict[i][suspicious_api_dict[i].index(name_str.lower().decode('utf-8'))]=1

        all_list = []
        for i in temp_dict:
            all_list += temp_dict[i]
        result[filename]=all_list
    return result


p = {}
p = get_api_info("C:\\Users\\SonMinWoo\\Desktop\\KU-Android-pre-train\\full")
f = open('malware_api_listtest.csv','w',encoding='utf-8',newline='')
wr = csv.writer(f)
for i in p:
    print("apk name : {} \n{}\n\n".format(i,p.get(i)))
    wr.writerow("{} {}".format(i,p.get(i)))
f.close()
wr.to_csv('malware.csv',sep=',')
"""
squareform(res)
distance = pd.DataFrame(squareform(res),index=df.index,columns=df.index)
print(distance)
distance.to_csv('jaccard_distance_all.csv')
frame = pd.DataFrame(list_result)
frame.to_csv('real_malware_list_all.csv', sep=',')
"""
