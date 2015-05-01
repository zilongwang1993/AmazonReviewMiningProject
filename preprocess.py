import re 	
import simplejson
import generateFeature
import string

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import csv

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



def getYScore(m,n):
	a=3.0
	if n ==0:
		return 0
	else:
		return a*m*m/n


def preprocess():
	textFeatureCnt=1000 
	#key features include: helpfulness,score, review wordcount,
	keyFeatureCnt=4
	totalCnt=keyFeatureCnt+textFeatureCnt
	ftrMatrix=[]
	raw = parse("toy.txt")

	#use dict and set to speed up text feature values generation
	preload=True
	reviewF=[]
	if preload:
		with open("textFeatures.txt") as openfileobject:
			for line in openfileobject:
				reviewF.append(line.strip())
	else:
		reviewF =generateFeature.generateFeatures("toy.txt",1000)
	reviewSet=set(reviewF)
	reviewDic={}
	for i in range(len(reviewF)):
		reviewDic[reviewF[i]]=i

	#get values for each feature
	for e in raw:
		entry= getEmptyEntries(totalCnt)
		hp=e["review/helpfulness"].split('/')
		m=int(hp[0])
		n=int(hp[1])
		entry[0]=getYScore(m,n)
		entry[1]=n
		entry[2]=int(e["review/score"][0])
		tempTxt=e["review/text"]
		entry[3]=countWords(tempTxt)
		tempWords = [e for e in map(string.strip, re.split("(\W+)", tempTxt)) if len(e) > 0 and not re.match("\W",e) and not e[0].isupper()]
		for word in tempWords:
			if word in reviewSet:
				entry[keyFeatureCnt+reviewDic[word]]+=1
		ftrMatrix.append(entry)
	#print ftrMatrix[:3]
	return ftrMatrix

def main():
	dataLists = preprocess()
	dataMatrix=np.array(dataLists)
	print dataMatrix.shape
	with open("output.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(dataMatrix)
	#print dataMatrix
	# Y=dataMatrix[:,0]
	# X=dataMatrix[:,1:]
	# print X.shape
	# print Y.shape
	# bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
 #                         	algorithm="SAMME",
 #                         	n_estimators=1)
	# bdt.fit(X, Y)



if __name__ == '__main__': # If this file is run directly
    main()