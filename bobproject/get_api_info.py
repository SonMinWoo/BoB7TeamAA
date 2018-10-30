import os
from api_dict import *
from parse_dex import *
import csv
import pandas as pd
import itertools
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard

def jaccard(labels1, labels2):
    """
    Computes the Jaccard similarity between two sets of clustering labels.
    The value returned is between 0 and 1, inclusively. A value of 1 indicates
    perfect agreement between two clustering algorithms, whereas a value of 0
    indicates no agreement. For details on the Jaccard index, see:
    http://en.wikipedia.org/wiki/Jaccard_index
    Example:
    labels1 = [1, 2, 2, 3]
    labels2 = [3, 4, 4, 4]
    print jaccard(labels1, labels2)
    @param labels1 iterable of cluster labels
    @param labels2 iterable of cluster labels
    @return the Jaccard similarity value
    """
    n11 = n10 = n01 = 0
    n = len(labels1)
    # TODO: Throw exception if len(labels1) != len(labels2)
    for i, j in itertools.combinations(xrange(n), 2):
        comembership1 = labels1[i] == labels1[j]
        comembership2 = labels2[i] == labels2[j]
        if comembership1 and comembership2:
            n11 += 1
        elif comembership1 and not comembership2:
            n10 += 1
        elif not comembership1 and comembership2:
            n01 += 1
    return float(n11) / (n11 + n10 + n01)


def get_api_info(PATH):
    count = 0
    result = {}
    filenames = os.listdir(PATH)
    prt_api = {}
    for i in suspicious_api_dict:
        print(suspicious_api_dict[i])
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
#f = open('malware_api_listtest.csv','w',encoding='utf-8',newline='')
#wr = csv.writer(f)


#for i in p:
#    print("apk name : {} \n{}\n\n".format(i,p.get(i)))
#    wr.writerow("{} {}".format(i,p.get(i)))
#f.close()

list_result = []
for key in p:
    list_p = []
    ap = p[key]
    for i in ap:
        list_p.append(str(i))
    if(list_p[0] != "-1"):
        list_result.append({"Name":key,"restartpackage":list_p[0],"getsystemservice":list_p[1],"getoutputstream":list_p[2],"execute":list_p[3],"NONE":list_p[4],"getinputstream":list_p[5],"getoutputstream2":list_p[6],"sendtextmessage":list_p[7],"createfrompdu":list_p[8],"getdisplaymessagebody":list_p[9], \
                                        "getdefault":list_p[10],"sendtextmessage":list_p[11],"createfrompdu2":list_p[12],"getdisplaymessagebody2":list_p[13],"getmessagebody":list_p[14],"getoriginatingaddress":list_p[15],"getuserdata":list_p[16],"getconnectioninfo":list_p[17],"getwifistate":list_p[18],"loadclass":list_p[19], \
                                        "tostring":list_p[20],"NONE2":list_p[21],"startrecording":list_p[22],"getmacaddress":list_p[23],"endcall":list_p[24],"equalsignorecase":list_p[25],"split":list_p[26],"execute2":list_p[27],"isadminactive":list_p[28],"locknow":list_p[29], \
                                        "exec":list_p[30],"getruntime":list_p[31], "NONE3":list_p[32],"getbroadcast":list_p[33],"abortbroadcast":list_p[34],"setvibratesetting":list_p[35],"setringermode":list_p[36],"dofinal":list_p[37],"getinstance":list_p[38],"getcontenturi":list_p[39],\
                                        "insertimage":list_p[40],"getbitmap":list_p[41],"getdeclaredmethod":list_p[42],"getsubscriberid":list_p[43],"getline1number":list_p[44],"getnetworkoperator":list_p[45],"getsimoperatorname":list_p[46],"getsimoperatorname2":list_p[47],"getsimserialnumber":list_p[48],"getcallstate":list_p[49],\
                                        "setcomponentenabledsetting":list_p[50],"NONE4":list_p[51],"getoutputstreamf":list_p[52],"getexternalstoragedirectory":list_p[53],"getexternalstoragestate":list_p[54],"getcontenturiforpath":list_p[55],"getlastknownlocation":list_p[56],"requestlocationupdates":list_p[57],"NONE5":list_p[58],"NONE6":list_p[59],\
                                        "getcontenturi2":list_p[60],"getcontentresolver":list_p[61],"setaccessible":list_p[62],"parse":list_p[63],"NONE7":list_p[64],"load2":list_p[65],"loadlibrary":list_p[66],"put":list_p[67],"NONE8":list_p[68],"generateKey":list_p[69],\
                                        "start":list_p[70],"stop":list_p[71],"NONE9":list_p[72],"NONE10":list_p[73],"getassets":list_p[74],"query":list_p[75],"delete":list_p[76],"close2":list_p[77]})
#    list_result.append([key,list_p])
#    list_result = list_result + list_p
df = pd.DataFrame(list_result)
res = 1-pdist(df[['restartpackage','getsystemservice','getoutputstream','execute','NONE','getinputstream','getoutputstream2','sendtextmessage','createfrompdu','getdisplaymessagebody','getdefault','sendtextmessage','createfrompdu2','getdisplaymessagebody2','getmessagebody','getoriginatingaddress','getuserdata','getconnectioninfo','getwifistate','loadclass',\
                'tostring','NONE2','startrecording','getmacaddress','endcall','equalsignorecase','split','execute2','isadminactive','locknow','exec','getruntime','NONE3','getbroadcast','abortbroadcast','setvibratesetting','setringermode','dofinal','getinstance','getcontenturi',\
                'insertimage','getbitmap','getdeclaredmethod','getsubscriberid','getline1number','getnetworkoperator','getsimoperatorname','getsimoperatorname2','getcallstate','setcomponentenabledsetting','NONE4','getoutputstreamf','getexternalstoragedirectory','getexternalstoragestate','getcontenturiforpath','getlastknownlocation','requestlocationupdates','NONE5','NONE6',\
                'getcontenturi2','getcontentresolver','setaccessible','parse','NONE7','load2','loadlibrary','put','NONE8','generateKey','start','stop','NONE9','NONE10','getassets','query','delete','close2']],'jaccard')
squareform(res)
distance = pd.DataFrame(squareform(res),index=df.index,columns=df.index)
print(distance)
distance.to_csv('jaccard_distance_all.csv')
frame = pd.DataFrame(list_result)
frame.to_csv('real_malware_list_all.csv', sep=',')
