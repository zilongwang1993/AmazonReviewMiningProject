import re 	

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


