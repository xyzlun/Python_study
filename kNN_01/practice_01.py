import numpy
import kNN
import matplotlib.pyplot as plt
reload (kNN)

'''group,labels=kNN.createDataSet()
datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')''' #1

'''fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
plt.show()''' #2

'''normMat,ranges,minVals=kNN.autoNorm(datingDataMat)
print normMat,ranges,minVals'''

'''print kNN.classify0([0,0],group,labels,3)
print datingDataMat''' #3

kNN.datingClassTest()