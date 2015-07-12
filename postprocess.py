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
	else:
		print "not five"


def postProcessHints(hintFile, filename, saveAt, limit):
	global hints

	hints = {}
	result = []
	with open(saveAt + "Passwords/" + filename) as infile:
	    for line in infile:
	        handleLine(line)
	#will output all hints now, even if there is just one....
	# if len(hints) < 10:
	# 	return
	for h in hints:
		if hints[h] > limit:
			result.append({"text":h,"size":hints[h]})
	with open("_data/" + hintFile + '.json') as data_file:    
		jsonData = json.load(data_file)		
	print "saving to: _data/" + saveAt + "Hints/" + filename.split(".")[0] + ".hints"
	filename = "_data/" + saveAt + "Hints/" + filename.split(".")[0]+".hints"
	with open(filename, 'w+') as outfile:
		json.dump(result, outfile)
	jsonData.append(filename)
	with open("_data/" + hintFile + '.json', 'w') as outfile:
		json.dump(jsonData, outfile)

#main
if __name__ == "__main__":
	ans=True
	while ans:
		print ("""
		1.Process known passwords
		2.Process unknown passwords
		3.Exit/Quit
		""")
		ans=raw_input("What would you like to do?")
		if ans=="1": 
			print("\Processing knowns...\n\n")
			#handle known paswords
			with open('_data/knownHintFiles.json', 'w') as outfile:
				json.dump(json.loads("[]"), outfile)
			if len(sys.argv) < 2:
				print "processing all known password files"
				for file in os.listdir("knownPasswords"):
					postProcessHints("knownHintFiles", file, "known", 20)
			else:
				print "processing: " + sys.argv[1]
				postProcessHints("knownHintFiles", sys.argv[1], "known", 20)
		elif ans=="2":
			print("\Process unknowns...\n\n")
			#handle known paswords
			with open('_data/unknownHintFiles.json', 'w') as outfile:
				json.dump(json.loads("[]"), outfile)
			if len(sys.argv) < 2:
				print "processing all unknown password files"
				for file in os.listdir("unknownPasswords"):
					postProcessHints("unknownHintFiles", file, "unknown", 2)
			else:
				print "processing: " + sys.argv[1]
				postProcessHints("unknownHintFiles", sys.argv[1], "unknown", 2)
			
		elif ans=="3":
			print("\n Goodbye") 
			sys.exit(0)
		elif ans !="":
			print("\n Not Valid Choice Try again") 


