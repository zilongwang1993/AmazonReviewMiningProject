import simplejson
import nltk
import string
import re

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


#need to run nltk.download('all') to download all the files
def generateFeatures(filename,cnt):
    raw = parse(filename)
    #raw = parse("smaller.txt")
    reviews="";
    for e in raw: 
        #print ((e["review/text"]))
        try:
            reviews = reviews+ (e["review/text"])
        except KeyError:
            pass
    #reviews= [(e["review/text"]) for e in raw]
    #all_words = nltk.word_tokenize(reviews.lower())

    #Tokenize the words in each review. 
    #We also get rid of capitalized words and symbols in this step.
    all_words=[e for e in map(string.strip, re.split("(\W+)", reviews)) if len(e) > 0 and not re.match("\W",e) and not e[0].isupper()]
    print("finished all words")
    print (len (all_words))
    wordcounts={}
    for word in all_words:

        if word in wordcounts:
            wordcounts[word]+=1
        else:
            wordcounts[word]=0
    #wordcounts = dict([ [t, all_words.count(t)] for t in set(all_words) ])
    #items = [(v, k) for k, v in wordcounts.items()]
    print("finished word counts")
    stopwords = nltk.corpus.stopwords.words('english')

    terms = {}
    for word, count in wordcounts.iteritems():
        if count > 2  and word not in stopwords and word.isalpha():
            terms[word] = count

    # Change the ordering of value and key for sorting
    items = [(v, k) for k, v in terms.items()]
     
    featureCnt=0 
    features=[]
    for count, word in sorted(items, reverse=True):
        if featureCnt ==cnt:
            break
        wordWithTag=nltk.pos_tag([word])
        if len(wordWithTag[0][1])<2:
            continue
        tag=wordWithTag[0][1][0:2]
        if tag == 'VB' or tag == 'RB' or tag == 'JJ':
            features.append(word)
            featureCnt=featureCnt+1
            #print("%5d %s" % (count, word))

    return features

def main():
    #features = generateFeatures("Books.txt")
    features = generateFeatures("toy.txt",1000)
    #print features
    f= open("textFeatures.txt",'a')
    for word in features:
        f.write(word+'\n')
    f.close()

if __name__ == '__main__': # If this file is run directly
    main()




