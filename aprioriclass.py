# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:18:19 2016

@author: abhinandan
"""
from itertools import chain, combinations

class Apriori(object):
    
    def __init__(self, support, confidence, path):
        self.minSup = support
        self.minConf = confidence
        self.file = open(path, 'rU')
        self.globalFItemSet = {}
        self.globalNFItemSet = {}
        self.transactionList, self.itemSet = self.getItemsAndTransactions()
        
    def getItemsAndTransactions(self):
        transactionList = list()
        itemSet = set()    
        for line in self.file:
            line = line.strip().rstrip(';').split(';')
            transaction = frozenset(line)
            transactionList.append(transaction)
            for item in transaction:
                itemSet.add(frozenset([item]))
        return transactionList, itemSet
        
    def getItemsWithMinSupport(self):
            length = len(self.transactionList)
            freqItemSet = set()
            nonFreqItemSet = set()
            freqItemsAndSupport = {}
            itemCounter = {}        
            for item in self.itemSet:
                    itemCounter[item] = 0
                    for transaction in self.transactionList:
                            if item.issubset(transaction):
                                    itemCounter[item] += 1
                    support = float(itemCounter[item])/length
                    if(support >= self.minSup):
                        freqItemSet.add(item)    
                        freqItemsAndSupport[item] = support
                    else:
                        nonFreqItemSet.add(item)
            return freqItemSet, freqItemsAndSupport, nonFreqItemSet
            
    def getCandidateItemSets(self, freqItemSet, k):
        self.itemSet =  set([i.union(j) for i in freqItemSet for j in freqItemSet if len(i.union(j)) == k])
        
    def prune(self, index):
        for i in self.globalNFItemSet[index]:
            for j in self.itemSet.copy():
                if (j.issuperset(i)):
                    self.itemSet.remove(j)

    def getAssociationRules(self):
        assocRules = []
        for key, value in self.globalFItemSet.items()[1:]:
                for item in value:
                    l2 = self.getCombinations(item)
                    l3 = self.getCombinationSets(l2)            
                    for element in l3:
                        diff = item.difference(element)
                        if(len(diff) > 0):
                            confidence = self.getSupport(item)/self.getSupport(element)
                            if(confidence >= self.minConf):
                                assocRules.append((("{} ==> {}".format(tuple(element), tuple(diff))), (confidence)))
        print "{} Association rules have been obtained".format(len(assocRules))
        return assocRules
        
    def getSupport(self, item):
        return (self.globalFItemSet[len(item)][item])
    
    def getCombinations(self, item):
        l1 = []
        l2 = []
        for i in range(0, len(item)):
            l1.append(list(combinations(item, i+1)))
        l2.append(list(chain(*l1)))
        return (l2)
        
    def getCombinationSets(self, l2):
        l3 = []            
        for i in range(0, len(l2)):
            for j in l2[i]:
                l3.append(frozenset(j))
        return (l3)