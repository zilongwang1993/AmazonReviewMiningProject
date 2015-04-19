import re 	
import simplejson

def countWords(str):
	count = len(str.split(' '))
	return count

#f = open('../Books.txt')
f = open('toy.txt')
# out =open('toy.text','w')
# next=f.readline()
# for i in range(1,1000000):
# 	out.write(next)
# 	next = f.readline()
# out.close()
# f.close()
next=f.readline()
next=f.readline()
print (countWords(next))


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


for e in parse("toy.txt"):
	print "start"
	print e["review/helpfulness"]
	print "end"
