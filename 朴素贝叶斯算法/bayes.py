#coding=utf-8
from numpy import *

# 创建训练集合
def loadDataSet():
    postingList = [['my','dog','has','flea','problems','help','please'],\
                 ['maybe','not','take','him','to','dog','park','stupid'],\
                 ['my','dalmation','is','so','cute','I','love','him'],\
                 ['stop','posting','stupid','worthless','garbage'],\
                 ['mr','licks','ate','my','steak','how','to','stop','him'],\
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1]  #1 代表侮辱性文字，0代表正常言论
    return postingList,classVec

# 文本去重
def creatVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 词集模型
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print 'the word: %s is not in my Vocabulary!' % word
    return returnVec

# 词袋模型 vocabList词汇表，inputSet输入文档，返回元素为0或1的向量，表示词汇表中的词汇是否在输入文档中出现
def bagOfWords2VecMN(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

#分类函数
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify*p1Vec) + log(pClass1)
    p0 = sum(vec2Classify*p0Vec) + log(1.0-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

# 朴素贝叶斯分类器算法 trainCategory为文档标签向量（用0,1表示是否为侮辱性文档）
def trainNBO(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)  # 测试文档片段数
    numWords = len(trainMatrix[0])  # 单词数
    pAbusive = sum(trainCategory)/float(numTrainDocs)  # 是侮辱性文档的概率
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:  # 当文档为侮辱性文档时
            p1Num += trainMatrix[i]  # 单词在侮辱性文档的向量加1
            p1Denom += sum(trainMatrix[i])  # 侮辱性文档的文字的总数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)  # change to log()  # 该单词在侮辱性文档中出现的条件概率
    p0Vect = log(p0Num/p0Denom)  # change to log()  # 该单词在非侮辱性文档中出现的条件概率
    return p0Vect,p1Vect,pAbusive

# 创建测试集，并调用分类算法
def testingNB():
    listOPosts,listClasses = loadDataSet()  # 创建训练文档和文档类型列表
    myVocabList = creatVocabList(listOPosts)  # 由训练文档创建词汇表
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = trainNBO(array(trainMat),array(listClasses))  # 计算词汇是侮辱性词汇的概率、非侮辱性词汇的概率、文档为侮辱性文档的概率

    testEntry = ['love','my','dalmation']  # 测试文档
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb)  # classifyNB分类函数
    testEntry = ['stupid','garbage']
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb)

# 字符串解析
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

# 对贝叶斯垃圾邮件分类器进行自动化处理
def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = creatVocabList(docList)
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNBO(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rates is :',float(errorCount)/len(testSet)


if __name__ == '__main__':
    # listOPosts,listClasses = loadDataSet()
    # myVocabList = creatVocabList(listOPosts)
    # trainMat = []
    # for postinDoc in listOPosts:
    #     trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    # p0V,p1V,pAb = trainNBO(trainMat,listClasses)
    # # print setOfWords2Vec(myVocabList,listOPosts[0])
    # # print setOfWords2Vec(myVocabList,listOPosts[1])
    # # print setOfWords2Vec(myVocabList,listOPosts[2])
    # # print setOfWords2Vec(myVocabList,listOPosts[3])
    # print p0V  # 单词属于非侮辱性文档的概率向量
    # print p1V  # 单词属于侮辱性文档的概率向量
    # print pAb  # 任意文档属于侮辱性文档的概率
    # testingNB()
    spamTest()
