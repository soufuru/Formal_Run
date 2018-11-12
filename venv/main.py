#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import MeCab
import json
import make_corpus as mc
import check as ch
import numpy as np


def file_output(json_file):
	for index in range(len(json_file)):
		print(json_file[index]["ID"])
		print(json_file[index]["Topic"])
		print(json_file[index]["Utterance"])


# 極性辞書
polarity = mc.make_corpus_from_enhanced_by_Word2Vec()
# polarity = mc.make_corpus()

# 強化後の辞書
# polarity = mc.make_corpus_from_float_corpus()

# 実数の辞書
# polarity = mc.make_corpus_pn_ja()

# 単語の属性
norn_nature = mc.norn_nature()

# with open("corpus/000-343-Classification-Tsukiji-A.json", "r") as file_A, \
# 		open("corpus/000-343-Classification-Tsukiji-B.json", "r") as file_B:
# 	json_A = json.load(file_A)
# 	json_B = json.load(file_B)
# 	for x in range(len(json_A)):
# 		if json_B[x]["Class"] == 1 or json_B[x]["Class"] == 2:
# 			if json_A[x]["Class"] == 0:
# 				json_A[x]["Class"] = json_B[x]["Class"]
# 	json_file = json_A

json_file = json.load(open("corpus/Classification-2018-JA-FormalRun-Training-02-カジノを含む統合型リゾートを推進するべきである-1165-J.json", "r"))
# json_file = json.load(open("corpus/Classification-2018-JA-FormalRun-Training-04-集団的自衛を認めるべきである-1515-A.json", "r"))
tmp_topic = json_file[0]["Topic"]

# classの数
classnumber = {"0": 0, "1": 0, "2": 0}
ratio = {"Correct": 0, "Wrong": 0}
correct_sentence = {"Class 1": [], "Class 2": []}

# 極性辞書が1,0,-1の3値のとき用
negative_threshold = -1.7
positive_threshold = 1

wrong_sentence = []
m = MeCab.Tagger("-Ochasen")

# 出力を入れる配列
# output = [{"Relevance":0, "Fact-checkability":0, "Stance":0}, ・・・]
output = []

i = 0

topic = m.parse(tmp_topic).split("\n")
topic_array = []
for to in topic[:-2]:
	to = to.split("\t")
	if "名詞" in to[3]:
		topic_array.append(to[0])

print(topic_array)




for number in range(len(json_file)):

	# 対象の文章だけ抽出
	# if json_file[number]["ID"] != "Classification-2018-JA-FormalTraining-00002":
	# 	continue

	# 入力文を形態素解析
	input = json_file[number]["Utterance"]
	sentence = m.parse(input).split("\n")
	kyokusei = []
	for word in sentence[:-2]:
		# hinshi[2]: 単語の基本形 , hinshi[3]: 品詞
		hinshi = word.split("\t")
		if "動詞" in hinshi[3] or "形容詞" in hinshi[3] or "名詞" in hinshi[3] or "助動詞" in hinshi[3]:
			kyokusei.append([hinshi[2], hinshi[3]])

		i += 1

	# print(sentence)

	tmp_output = {"Relevance": 0, "Fact-checkability": 0, "Stance": 0, "Class": 0}

	#############
	# Relevance #
	#############
	tmp_kyokusei_array = [tmp[0] for tmp in kyokusei if "名詞" in tmp[1]]

	for tango in topic_array:
		if tango in tmp_kyokusei_array:
			tmp_output["Relevance"] = 1
			break

	##########
	# Stance #
	##########
	result = {}
	hyouka = 0
	for i in range(len(kyokusei)):

		# {”単語” : {評価値 , "単語の性質"}}
		# 単語の性質が"出来事"なら除外

		# if polarity[kyokusei[i][0]] != 0 and norn_nature[kyokusei[i][0]] != "出来事":
		if kyokusei[i][0] in polarity:
			hyouka += polarity[kyokusei[i][0]]
			result[kyokusei[i][0]] = polarity[kyokusei[i][0]]

	if hyouka > positive_threshold:
		tmp_output["Stance"] = 1
	elif hyouka < negative_threshold:
		tmp_output["Stance"] = 2
	else:
		tmp_output["Stance"] = 0

	#####################
	# Fact-checkability #
	#####################
	lis = ["おり", "例", "から", "であり", "理由"]
	for l in lis:
		if l in input:
			tmp_output["Fact-checkability"] = 1
			break

	#########
	# Class #
	#########
	if tmp_output["Fact-checkability"] == 1:
		if tmp_output["Stance"] == 1:
			tmp_output["Class"] = 1
		elif tmp_output["Stance"] == 2:
			tmp_output["Class"] = 2
	else:
		tmp_output["Class"] = 0
	output.append(tmp_output)

# print(json.dumps(output))
ch.factcheckability_check(output, json_file)
ch.relevance_check(output,json_file)
ch.stance_check(output, json_file)
ch.class_check(output, json_file)

# file_output(json_file)
