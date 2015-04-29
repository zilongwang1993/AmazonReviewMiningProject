import re 	
import simplejson

def countWords(str):
	count = len(str.split(' '))
	return count

def parse(filename):
	f = open(filename, 'r')
	entry = {}
	for l in f:
		l = l.strip()
		colonPos = l.find(':')
		if colonPos == -1:
			yield entry
			entry = {}
			continue
		eName = l[:colonPos]
		rest = l[colonPos+2:]
		entry[eName] = rest
	yield entry


#f = open('../Books.txt')
raw = parse("toy.txt")

for e in raw:
	p=""
	
	print (e["review/text"])

