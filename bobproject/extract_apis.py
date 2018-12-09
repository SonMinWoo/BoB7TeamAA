import os
from dictionary_api import *
from class_parse import *
import csv
import pandas as pd
import itertools

api_list = []


def extract_apis(PATH):
    count = 0
    result = {}
    filenames = os.listdir(PATH)
    for i in maluse_api:
        clas = i
        a = maluse_api[i]
        for j in range(len(a)):
            api_list.append(clas+" "+a[j])

    prt_api = {}
    for filename in filenames:
        count = count+1
        print(count)
        temp_dict = {}

        for i in maluse_api:
            name = i
            temp_list = [0 for i in range(len(maluse_api[i]))]
            temp_dict[name]= temp_list

        try:
            f = open(PATH+"/"+filename+"/"+'classes.dex','rb')
        except IOError as e:
            result[filename] = [-1 for i in range(77)]
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
            for i in maluse_api:
                if class_str[1:].lower().find(i.encode('utf-8')) != -1:
                    if 'NONE' in maluse_api[i]:
                        temp_dict[i][maluse_api[i].index('NONE')]=1
                    if name_str.lower().decode('utf-8', errors = "ignore") in maluse_api[i]:
                        temp_dict[i][maluse_api[i].index(name_str.lower().decode('utf-8'))]=1

        all_list = []
        for i in temp_dict:
            all_list += temp_dict[i]
        result[filename]=all_list
    return result


p = {}
#path = input("input path : ")
path = "D:\\2nd_dataset\\2nd_dataset"
"""C:\\Users\\SonMinWoo\\Desktop\\1st_dataset"""
p = extract_apis(path)
#f = open('malicious_api.csv','w',encoding='utf-8',newline='')
csvdata = pd.DataFrame(p, index=api_list)
csvdata = csvdata.T
csvdata.to_csv("secondnew_apis.csv",sep=',')
