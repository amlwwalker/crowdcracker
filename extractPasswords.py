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
#the below will handle all unknowns. Need to make it handle a specific few
def handleUnknown():
	with open("rawAdobeData") as infile: #if you just want to test, swap for testRawData
		for line in infile:	
			lineCounter = 0
			split = line.split('-|-')
			if len(split) >=5:
				cipher = split[3]
				print ". " + cipher
				canWrite = True
				with open("knownpasswords") as checkKnowns:
					for p in checkKnowns:
						split = p.split(' ')
						if cipher in split[0]:
							canWrite = False
							break
				#its not a known password:
				if canWrite:
					#need to start looking for it in the raw data file
					#currently the rawAdobeData file is not the same file as the passwords to hunt for
					with open("rawAdobeData") as rawData:
						for r in rawData:
							if cipher in r: #the cipher is in the line:
								lineCounter += 1
								cipher = cipher.replace("/", "")
								with open("unknownPasswords/"+cipher+".pass",'a+') as f: f.write(r)
				print "		----	Found " + str(lineCounter) + " matches"

def handleKnown():
	with open("knownPasswords") as infile: #if you just want to test, swap for sampleKnownPasswords
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
			print("\nExtracting knowns...\n\n")
			handleKnown() 
		elif ans=="2":
			print("\nExtracting unknowns...\n\n")
			handleUnknown() 
		elif ans=="3":
			print("\n Goodbye") 
			sys.exit(0)
		elif ans !="":
			print("\n Not Valid Choice Try again") 
