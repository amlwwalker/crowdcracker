import re
import sys
'''
This script extracts passwords from cred file and extracts the raw data
It has two functions:
handleUnknown:
	* extract every line of the file putting each cipher into the right file
handleKnown:
	* extracts lines that come from a list (i.e the known password list)
'''
#grep function does a search for lines containing some string
def grep(ciphertext, plaintext):
	lines = []
	filename = "knownPasswords/"+plaintext.rstrip()+".pass"
	fo = open(filename, "w+")
	print "Saving to: "+ fo.name
	with open("rawAdobeData") as infile:
	    for line in infile:
		    if ciphertext in line:
	        	lines.append(line)
	fo.writelines( lines )

def handleUnknown():
	with open("rawAdobeData") as infile:
		for line in infile:	
			split = line.split('-|-')
			if len(split) >5:
				cipher = split[3]
				cipher = cipher.replace("/", "")
				with open("unknownPasswords/"+cipher+".pass",'w+') as f: f.write(line)

def handleKnown():
	with open("sampleKnownPasswords") as infile:
	    for line in infile:
	    	print ".",
	    	split = line.split(' ')
	        grep(split[0], split[1])

if __name__ == "__main__":
	ans=True
	while ans:
		print ("""
		1.Extract known passwords
		2.Extract unknown passwords
		3.Exit/Quit
		""")
		ans=raw_input("What would you like to do?")
		if ans=="1": 
			print("\Extracting knowns...\n\n")
			handleKnown() 
		elif ans=="2":
			print("\nExtracting unknowns...\n\n")
			handleUnknown() 
		elif ans=="3":
			print("\n Goodbye") 
			sys.exit(0)
		elif ans !="":
			print("\n Not Valid Choice Try again") 
