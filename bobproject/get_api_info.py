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
            f = open(PATH+"/"+filename+"/"+'classes.dex','rb')
        except IOError as e:
            result[filename] = [-1 for i in range(78)]
            continue
        mm = f.read()
        f.close()
        hdr = header(mm)

        string_ids = string_id_list(mm, hdr)
        type_ids = type_id_list(mm, hdr)
        method_ids = method_id_list(mm, hdr)

        apilist = []
        for i in range(len(method_ids)):
            (class_idx, proto_idx, name_idx) = method_ids[i]
            class_str = string_ids[type_ids[class_idx]]
            name_str = string_ids[name_idx]
            apilist.append([class_str[1:], name_str])
            prt_api[class_str[1:]] = name_str.lower()
#            print('[file : %s, class : %s, name : %s, method : %s]' % (filename, class_str[1:], name_str,method_ids[i]))
            for i in suspicious_api_dict:
                if class_str[1:].lower().find(i.encode('utf-8')) != -1:
                    if 'NONE' in suspicious_api_dict[i]:
                        temp_dict[i][suspicious_api_dict[i].index('NONE')]=1
                    if name_str.lower().decode('utf-8', errors = "ignore") in suspicious_api_dict[i]:
                        temp_dict[i][suspicious_api_dict[i].index(name_str.lower().decode('utf-8'))]=1

        all_list = []
        for i in temp_dict:
            all_list += temp_dict[i]
        result[filename]=all_list
    return result


p = {}
#path = input("input path : ")
path = "C:\\Users\\SonMinWoo\\Desktop\\KU-Android-pre-train\\1-malware"
p = get_api_info(path)
#f = open('malicious_api.csv','w',encoding='utf-8',newline='')

label_list = []
for i in suspicious_api_dict:
	label_list.append(i)
bilabel = []
for i in p.keys():
	bilabel.append(i)
raw = {"filename":list(p.keys()),"binary_label":bilabel}
csvdata = pd.DataFrame(p)
csvdata.to_csv("mal_apis.csv",sep=',')
