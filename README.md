
## Layout of how this works:

* the file `sampleKnownPasswords` is the file that is read to find all matching hints for a specific password
* `extractPasswords.py` is then run. Choose '1' at the menu to extract all known password hints.
	* It will extract them all into files named `[password].pass` and put them in the directory `knownPasswords`
* `postprocess.py` is then run. It will go through all of the files in `knownPasswords` counting the occurances of hints and adding them to json. 
	* Currently hardcoded to add any hint with more than `20` occurances to the json.
	* It then saves these in knownHints as `[password].hints`. 
	* It also adds an array entry to the json in the file `hintFiles.json`
		* These are the json files that the d3 randomly chooses from.

* `index.html` contains the javascript that randomly chooses a hints file from the array in `hintFiles.json` and displays a word cloud

### To Do:

* Work out a layout that shows you the word cloud for the known passwords and records your guess. 
* Somehow work out the best way of storing the guess

