#!/usr/bin/env python
import os
import operator
import json
import sys
'''
This file handles cleaning the data and extracting the hints
* There is a bug when trying to process all at once rather than
specifying the file to process on the command line
'''
hints = {}
def handleLine(line):

	split = line.split('-|-')
	if len(split) >= 5:
		hint = split[4].split('|--')[0]
		if hint != "":
			if hint != ' ':
				hint = hint.replace("'", "").replace('"', '').lower()
				if hint in hints:
					hints[hint] += 1
				else:
					hints[hint] = 1


def postProcessHints(filename, jsonData):
	global hints
	hints = {}
	result = []
	saveTo = filename.split("/")[1].split(".")[0]
	with open(filename) as infile:
	    for line in infile:
	        handleLine(line)
	for h in hints:
		if hints[h] > 50:
			result.append({"text":h,"size":hints[h]})
	print "saving to: " + "knownHints/"+saveTo+".hints"
	saveTo = "knownHints/"+saveTo+".hints"
	with open(saveTo, 'w') as outfile:
		json.dump(result, outfile)
	jsonData.append(saveTo)
	with open('hintFiles.json', 'w') as outfile:
		json.dump(jsonData, outfile)

if __name__ == "__main__":
	with open('hintFiles.json', 'w') as outfile:
		json.dump(json.loads("[]"), outfile)
	if len(sys.argv) < 2:
		print "processing all known password files"
		for file in os.listdir("knownPasswords"):
			with open('hintFiles.json') as data_file:    
				data = json.load(data_file)
			postProcessHints("knownPasswords/"+file, data)
	else:
		print "processing: " + sys.argv[1]
		with open('hintFiles.json') as data_file:    
			data = json.load(data_file)
			postProcessHints(sys.argv[1], data)