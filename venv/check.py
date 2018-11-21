#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.metrics import classification_report
import warnings
import matplotlib.pyplot as plt
import numpy as np

output_arr = []
def grapher():
	c0pre = []
	for output in output_arr:
		c0pre.append(output['class 0']['precision'])
	left = [i+1 for i in range(len(c0pre))]
	plt.bar(np.array(left), np.array(c0pre))
	plt.show()

def print_output(pred, ansarr, target_names):
	output = classification_report(pred, ansarr, target_names=target_names, output_dict=True)
	output_arr.append(output)
	# print(output['class 0']['precision'])
	# print(output['class 1']['precision'])
	# if 'class 2' in output:
	# 	print(output['class 2']['precision'])


def relevance_check(output, json_file):
	# 出力
	pred = []
	# 正しい答え
	ansarr = []
	target_names = ['class 0', 'class 1']
	for out, ans in zip(output, json_file):

		pred.append(out["Relevance"])
		ansarr.append(ans["Relevance"])

	print("#############")
	print("# Relevance #")
	print("#############")

	warnings.simplefilter("ignore")
	print_output(pred, ansarr, target_names)


def factcheckability_check(output, json_file):
	# 出力
	pred = []
	# 正しい答え
	ansarr = []
	target_names = ['class 0', 'class 1']
	for out, ans in zip(output, json_file):

		pred.append(out["Fact-checkability"])
		ansarr.append(ans["Fact-checkability"])

	print("#####################")
	print("# Fact-checkability #")
	print("#####################")

	warnings.simplefilter("ignore")
	print_output(pred, ansarr, target_names)



def stance_check(output, json_file):
	# 出力
	pred = []
	# 正しい答え
	ansarr = []
	target_names = ['class 0', 'class 1', 'class 2']
	for out, ans in zip(output, json_file):

		pred.append(out["Stance"])
		ansarr.append(ans["Stance"])

	print("##########")
	print("# Stance #")
	print("##########")

	warnings.simplefilter("ignore")
	print_output(pred, ansarr, target_names)



def class_check(output, json_file):
	# 出力
	pred = []
	# 正しい答え
	ansarr = []
	target_names = ['class 0', 'class 1', 'class 2']
	for out, ans in zip(output, json_file):

		pred.append(out["Class"])
		ansarr.append(ans["Class"])

	print("#########")
	print("# Class #")
	print("#########")

	warnings.simplefilter("ignore")
	print_output(pred, ansarr, target_names)
