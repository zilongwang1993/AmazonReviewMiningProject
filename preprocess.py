import re 	
import simplejson
import generateFeature
import string

def countWords(str):
	count = len(str.split(' '))
	return count
def getEmptyEntries(featureCnt):
	return [0]*featureCnt

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


def main():
#f = open('../Books.txt')
	#text features include: review text feature
	textFeatureCnt=1000 
	#key features include: helpfulness,score, review wordcount,
	keyFeatureCnt=3
	totalCnt=keyFeatureCnt+textFeatureCnt
	ftrMatrix=[]
	raw = parse("toy.txt")

	#use dict and set to speed up text feature values generation
	reviewF =generateFeature.generateFeatures("toy.txt")
	reviewSet=set(reviewF)
	reviewDic={}
	for i in range(len(reviewF)):
		reviewDic[reviewF[i]]=i

	#get values for each feature
	for e in raw:
		entry= getEmptyEntries(totalCnt)
		entry[0]=int(e["review/helpfulness"][0])
		entry[1]=int(e["review/score"][0])
		tempTxt=e["review/text"]
		entry[2]=countWords(tempTxt)
		tempWords = [e for e in map(string.strip, re.split("(\W+)", tempTxt)) if len(e) > 0 and not re.match("\W",e) and not e[0].isupper()]
		for word in tempWords:
			if word in reviewSet:
				entry[3+reviewDic[word]]+=1
		ftrMatrix.append(entry)
	print ftrMatrix






if __name__ == '__main__': # If this file is run directly
    main()