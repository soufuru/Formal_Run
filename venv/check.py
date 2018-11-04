#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def relevance_check(output, json_file):
	# 正しくジャッジできたか
	judge = {"correct": 0, "wrong": 0}
	# 正解のラベル
	correct_judge = {"0": 0, "1": 0}
	# 出力のラベル
	classnumber = {"0": 0, "1": 0}

	# 正しく出力できた数
	correct0 = 0
	correct1 = 0
	correct2 = 0

	# 間違って出力した数
	wrong0 = 0
	wrong1 = 0
	wrong2 = 0

	for out, ans in zip(output, json_file):

		# 正しい答えの分類
		if ans["Relevance"] == 0:
			correct_judge["0"] += 1
		else:
			correct_judge["1"] += 1

		# 出力
		if out["Relevance"] == 0:
			classnumber["0"] += 1
		else:
			classnumber["1"] += 1

		# 出力と答えがあっていれば
		if out["Relevance"] == ans["Relevance"]:
			if out["Relevance"] == 0:
				correct0 += 1
			else:
				correct1 += 1
			judge["correct"] += 1
		else:
			if out["Relevance"] == 0:
				wrong0 += 1
			else:
				wrong1 += 1
			judge["wrong"] += 1

	print("#############")
	print("# Relevance #")
	print("#############")

	# precision
	print("Precision 0")
	try:
		print(correct0 / classnumber["0"])
	except ZeroDivisionError:
		print("0 or ERROR")
	print()
	print("Precision 1")

	print(correct1 / classnumber["1"])
	print()

	# recall
	print("Recall 0")
	try:
		print(correct0 / correct_judge["0"])
	except ZeroDivisionError:
		print("0 or ERROR")
	print()
	print("Recall 1")
	print(correct1 / correct_judge["1"])
	print()


def factcheckability_check(output, json_file):
	# 正しくジャッジできたか
	judge = {"correct": 0, "wrong": 0}
	# 正解のラベル
	correct_judge = {"0": 0, "1": 0}
	# 出力のラベル
	classnumber = {"0": 0, "1": 0}

	# 正しく出力できた数
	correct0 = 0
	correct1 = 0
	correct2 = 0

	# 間違って出力した数
	wrong0 = 0
	wrong1 = 0
	wrong2 = 0

	for out, ans in zip(output, json_file):

		# 正しい答えの分類
		if ans["Fact-checkability"] == 0:
			correct_judge["0"] += 1
		else:
			correct_judge["1"] += 1

		# 出力
		if out["Fact-checkability"] == 0:
			classnumber["0"] += 1
		else:
			classnumber["1"] += 1

		# 出力と答えがあっていれば
		if out["Fact-checkability"] == ans["Fact-checkability"]:
			if out["Fact-checkability"] == 0:
				correct0 += 1
			else:
				correct1 += 1
			judge["correct"] += 1
		else:
			if out["Fact-checkability"] == 0:
				wrong0 += 1
			else:
				wrong1 += 1
			judge["wrong"] += 1

	print("#####################")
	print("# Fact-checkability #")
	print("#####################")

	# precision
	print("Precision 0")
	print(correct0 / classnumber["0"])
	print()
	print("Precision 1")
	print(correct1 / classnumber["1"])
	print()

	# recall
	print("Recall 0")
	print(correct0 / correct_judge["0"])
	print()
	print("Recall 1")
	print(correct1 / correct_judge["1"])
	print()


def stance_check(output, json_file):
	# 正しくジャッジできたか
	judge = {"correct": 0, "wrong": 0}
	# 正解のラベル
	correct_judge = {"0": 0, "1": 0}
	# 出力のラベル
	classnumber = {"0": 0, "1": 0}

	# 正しく出力できた数
	correct0 = 0
	correct1 = 0
	correct2 = 0

	# 間違って出力した数
	wrong0 = 0
	wrong1 = 0
	wrong2 = 0

	for out, ans in zip(output, json_file):

		# 正しい答えの分類
		if ans["Stance"] == 0:
			correct_judge["0"] += 1
		else:
			correct_judge["1"] += 1

		# 出力
		if out["Stance"] == 0:
			classnumber["0"] += 1
		else:
			classnumber["1"] += 1

		# 出力と答えがあっていれば
		if out["Stance"] == ans["Stance"]:
			if out["Stance"] == 0:
				correct0 += 1
			elif out["Stance"] == 1:
				correct1 += 1
			else:
				correct2 += 1
			judge["correct"] += 1
		else:
			if out["Stance"] == 0:
				wrong0 += 1
			elif out["Stance"] == 1:
				wrong1 += 1
			else:
				wrong2 += 1
			judge["wrong"] += 1

	print("#####################")
	print("# Stance #")
	print("#####################")

	# precision
	print("Precision 0")
	print(correct0 / classnumber["0"])
	print()
	print("Precision 1")
	print(correct1 / classnumber["1"])
	print()

	# recall
	print("Recall 0")
	print(correct0 / correct_judge["0"])
	print()
	print("Recall 1")
	print(correct1 / correct_judge["1"])
	print()


def class_check(output, json_file):
	# 正しくジャッジできたか
	judge = {"correct": 0, "wrong": 0}
	# 正解のラベル
	correct_judge = {"0": 0, "1": 0, "2": 0}
	# 出力のラベル
	classnumber = {"0": 0, "1": 0, "2": 0}

	# 正しく出力できた数
	correct0 = 0
	correct1 = 0
	correct2 = 0

	# 間違って出力した数
	wrong0 = 0
	wrong1 = 0
	wrong2 = 0

	for out, ans in zip(output, json_file):

		# 正しい答えの分類
		if ans["Class"] == 0:
			correct_judge["0"] += 1
		elif ans["Class"] == 1:
			correct_judge["1"] += 1
		else:
			correct_judge["2"] += 1

		# 出力
		if out["Class"] == 0:
			classnumber["0"] += 1
		elif out["Class"] == 1:
			classnumber["1"] += 1
		else:
			classnumber["2"] += 1

		# 出力と答えがあっていれば
		if out["Class"] == ans["Class"]:
			if out["Class"] == 0:
				correct0 += 1
			elif out["Class"] == 1:
				correct1 += 1
			else:
				correct2 += 1
			judge["correct"] += 1
		else:
			if out["Class"] == 0:
				wrong0 += 1
			elif out["Class"] == 1:
				wrong1 += 1
			else:
				wrong2 += 1
			judge["wrong"] += 1

	print("###############")
	print("# Class-check #")
	print("###############")
	# precision
	print("Precision 0")
	print(correct0 / classnumber["0"])
	print()
	print("Precision 1")
	print(correct1 / classnumber["1"])
	print()
	print("Precision 2")
	print(correct2 / classnumber["2"])
	print()
	# recall
	print("Recall 0")
	print(correct0 / correct_judge["0"])
	print()
	print("Recall 1")
	print(correct1 / correct_judge["1"])
	print()
	print("Recall 2")
	print(correct2 / correct_judge["2"])
	print()
