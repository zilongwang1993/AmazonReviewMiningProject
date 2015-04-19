#gagagagaga
#Mike 
import simplejson

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