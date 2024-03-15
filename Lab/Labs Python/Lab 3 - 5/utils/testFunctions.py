'''
Created on Nov 5, 2017

@author: iuan
'''
import domain.activities as da
import domain.changes as dc

#Iteration 1 - procedural
#p2, feature 1
da.test_addScore()
da.test_insertScore()

#p2, feature 2
da.test_removeScore()
da.test_removeFrom()
da.test_replaceScore()

#ITERATION 2 - procedural
#p2, feature 3
da.test_less40()
da.test_sort()
da.test_sortG90()

#p2, feature 4
da.test_avgFrom()
da.test_minFrom()
da.test_mulScoreFrom()

#ITERATION 3 - modular
#p2, feature 5
dc.test_filMul()
dc.test_filGT()