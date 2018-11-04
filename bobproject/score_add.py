import pandas as pd
import os

malpath = input("input malware binary name : ")
norpath = input("input normal binary name : ")

malp = pd.read_csv("./"+malpath, sep=",")
norp = pd.read_csv("./"+norpath, sep=",")

num_mal = []
num_nor = []

mal_appname_list = list(malp.columns)
mal_err = []
mal_score = []
for i in range(78):
	mal_score.append(0)
for i in mal_appname_list:
	temp_list = list(malp[i])
	if(temp_list[1] != -1):
		for x in range(len(temp_list)):
			if(temp_list[x] == 1):
				mal_score[x] = mal_score[x]+1
	else:
		mal_err.append(i)
for i in range(78):
	mal_score[i] = mal_score[i] / 78.0

nor_appname_list = list(norp.columns)
nor_err = []
nor_score = []
for i in range(78):
	nor_score.append(0)
for i in nor_appname_list:
	temp_list = list(norp[i])
	if(temp_list[1] != -1):
		for x in range(len(temp_list)):
			if(temp_list[x] == 1):
				nor_score[x] = nor_score[x]+1
	else:
		nor_err.append(i)
for i in range(78):
	nor_score[i] = nor_score[i] / 78.0

divide = 0.0
total_score = []
for i in range(len(mal_score)):
	if(nor_score[i]==0):
		nor_score[i] = 1.0
	divide = float(mal_score[i])/float(nor_score[i])
	total_score.append(divide)

print(total_score)

mal_score_list = []
for i in mal_appname_list:
	app_score = 0.0
	temp_list = list(malp[i])
	if(temp_list[1] != -1):
		for x in range(len(temp_list)):
			if(temp_list[x] == 1):
				app_score = total_score[x]*1
	else:
		app_score = -1
	mal_score_list.append(app_score)

nor_score_list = []
for i in nor_appname_list:
	app_score = 0.0
	temp_list = list(norp[i])
	if(temp_list[1] != 1):
		for x in range(len(temp_list)):
			if(temp_list[x] == 1):
				app_score = total_score[x]*1
	else:
		app_score = -1
	nor_score_list.append(app_score)

new_mal = pd.DataFrame({"score":mal_score_list},index=mal_appname_list, columns=["score"])
new_nor = pd.DataFrame({"score":nor_score_list},index=nor_appname_list, columns=["score"])

one = []
for i in range(len(mal_appname_list)):
	one.append(1)
mal_val = pd.Series(one, index=mal_appname_list)
new_mal["label"] = mal_val

zero = []
for i in range(len(nor_appname_list)):
	zero.append(0)
nor_val = pd.Series(zero, index=nor_appname_list)
new_nor["label"] = nor_val

score_data = pd.concat([new_mal, new_nor])
score_data.to_csv("api_scores.csv",sep=",")
