from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inx, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}  # 1
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # 2
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)  # 3
    return sortedClassCount[0][0]  # 4


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLables = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(
            normMat[i, :], normMat[numTestVecs:m, :], datingLables[numTestVecs:m], 3)
        print "the classifier came back with : %d, the real answer is: %d" % (classifierResult, datingLables[i])
        if(classifierResult != datingLables[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))


def classifyPerson():
      resultList = ['not at all', 'in small doses', 'in large doses']
      percentTats = float(
          raw_input("percentage of time spent playing video games?"))
      ffMiles = float(raw_input("frequent flier miles earned per year?"))
      iceCream = float(raw_input("liters of ice cream consumed per yaer?"))
      datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
      normMat, ranges, minVals = autoNorm(datingDataMat)
      inArr = array([ffMiles, percentTats, iceCream])
      classifierResult = classify0( (inArr - minVals) / ranges, normMat, datingLabels, 3)
      print "You will probably like this person:",resultList[classifierResult-1]


