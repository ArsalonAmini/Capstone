#supervised learning tutorial
from pybrain.datasets import SupervisedDataSet
from pybrain.datasets import ClassificationDataSet
# DS = SupervisedDataSet(3,2)
# DS.appendLinked([1,2,3], [4,5])
# print(len(DS))
# DS['input']
# array([[1., 2., 3.]])

DS = ClassificationDataSet(2, class_labels=['Urd', 'Verdandi', 'skuld'])
DS.appendLinked([0.1, 0.5] , [0])
DS.appendLinked([1.2, 1.2] , [1])
DS.appendLinked([1.4, 1.6] , [1])
DS.appendLinked([1.6, 1.8] , [1])
DS.appendLinked([0.10, 0.80] , [2])
DS.appendLinked([0.20, 0.90] , [2])

print(DS.calculateStatistics())
print(DS.classHist)
print(DS.nClasses)
print(DS.getClass(1))
print(DS.getField('target').transpose())

