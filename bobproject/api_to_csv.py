from api_dict import *
from parse_dex import *
import csv
import pandas as pd


label_list = []
for i in suspicious_api_dict:
	for j in i
		label_list.append("class : %s method : %s"%(i,suspicious_api_dict[i]) )
api_list = {"api name":label_list}
csvapi = pd.DataFrame(api_list)
csvapi.to_csv("name of api.csv",sep=',')
