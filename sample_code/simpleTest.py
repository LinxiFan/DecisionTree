'''
@author: Jim
'''
from learning import *
test_set = DataSet(name='../data/test_data', attrnames='X1 X2 Y', target = 'Y')
learner = DecisionTreeLearner()
learner.train(test_set)
learner.dt.display()

learner.prune(test_set, 5)