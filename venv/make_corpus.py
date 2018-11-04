#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import re
import statistics
import math

def make_corpus_from_enhanced_by_Word2Vec():
	polarity = {}
	file = open("corpus/corpus.txt", "r").readlines()
	pattern = "\'(.*)\':(.*),"
	repatter = re.compile(pattern)
	for i in file:
		matchOB = repatter.search(i)
		if matchOB:
			polarity[matchOB.group(1)] = int(matchOB.group(2))
	return polarity

def make_corpus_from_integer_corpus():
	polarity = {}
	file = open("corpus2.txt", "r").readlines()
	pattern = "\"(.*)\":(.*),"
	repatter = re.compile(pattern)
	for i in file:
		matchOB = repatter.search(i)
		if matchOB:
			polarity[matchOB.group(1)] = int(matchOB.group(2))
	return polarity

def make_corpus_from_float_corpus():
	polarity = {}
	file = open("corpus3.txt", "r").readlines()
	pattern = "\"(.*)\":(.*)"
	repatter = re.compile(pattern)
	for i in file:
		matchOB = repatter.search(i)
		if matchOB:
			polarity[matchOB.group(1)] = float(matchOB.group(2))
	return polarity


def make_corpus():
	polarity = {}
	verb = open("corpus/wago.121808.pn", "r")
	for line in verb.readlines():
		output = line.rstrip().split("\t")
		try:
			if "ポジ" in output[0]:
				polarity[output[1]] = 1
			else:
				polarity[output[1]] = -1
		except IndexError:
			continue

	# norn = open("corpus/norn.json")
	# file = json.load(norn)
	# for line in file:
	#     if line["Judge"] == "p":
	#         polarity[line["Word"]] = 1
	#     elif line["Judge"] == "n":
	#         polarity[line["Word"]] = -1
	#     else:
	#         polarity[line["Word"]] = 0

	norn = open("corpus/pn.csv.m3.120408.trim", "r")
	for line in norn.readlines():
		output = line.rstrip().split()
		try:
			if output[1] == "p":
				polarity[output[0]] = 1
			elif output[1] == "n":
				polarity[output[0]] = -1
			else:
				polarity[output[0]] = 0
		except IndexError:
			continue

	return polarity


import re


def norn_nature():
	pattern = r"\（(.*)\）"
	repatter = re.compile(pattern)
	norn_nature = {}

	file = open("corpus/pn.csv.m3.120408.trim", "r")

	for line in file.readlines():
		array = re.split("\t|\s", line)
		if len(array) == 4:
			matchOB = repatter.findall(array[2])
		else:
			matchOB = repatter.findall(array[3])
		if matchOB:
			norn_nature.update({array[0]: matchOB[0]})
		else:
			norn_nature.update({array[0]: " "})
	return norn_nature


# make_corpus()

def make_corpus_pn_ja():
	polarity = {}
	word = open("corpus/pn_ja.txt", "r")
	for line in word.readlines():
		output = line.rstrip().split(":")
		try:
			polarity[output[0]] = float(output[3])
		except IndexError:
			continue
	mean = statistics.mean(polarity.values())
	# median = statistics.median(polarity.values())

	for key in polarity.keys():
		polarity[key] += math.fabs(mean)
		print("\""+key+"\""+":"+str(polarity[key]))
	return polarity


################################
##  Word2Vecを用いて辞書を強化  ##
################################

from gensim.models.word2vec import Word2Vec


def update_corpus(polarity):
	# model = Word2Vec.load("/Users/soufuru/pycharmProjects/word2Vec/venv/corpus/word2vec.gensim.model")
	model = Word2Vec.load("/Users/soufuru/pycharmProjects/word2Vec/venv/word2vec.gensim.model")

	file = open("not_in_corpus.txt", "r")
	for line in file.readlines():
		try:
			for similar in model.wv.similar_by_word(line.rstrip(), 10):
				if similar[0] in polarity:
					polarity[line.rstrip()] = polarity[similar[0]]
		except KeyError:
			continue
