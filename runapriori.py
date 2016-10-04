# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:39:36 2016

@author: abhinandan
"""
import argparse
import pandas as pd
from aprioriclass import Apriori

def checkValue(value):
    val = float(value)
    if(val<=0 or val>1.0):
        raise argparse.ArgumentTypeError("%s is an invalid value. Must be between 0 and 1." % value)
    return val
    
def writeRules(rules): 
    d = {}
    df = pd.DataFrame(d, index=[0])       
    for rule in rules:
        d['association_rule'] = rule[0]
        d['confidence'] = rule[1]
        df = df.append(d, ignore_index=True)
    df.to_csv('rules.csv')    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", required=True, type=checkValue, help="Minimum support value (between 0-1)")
    parser.add_argument("-c", required=True, type=checkValue, help="Minimum confidence value (between 0-1)")
    parser.add_argument("-p", required=True, help="Path to the directory that contains the file")
    args = parser.parse_args()
    
    obj = Apriori(args.s, args.c, args.p)
    freqItemSet, frequentItemsAndSupport, nonFreqItemSet = obj.getItemsWithMinSupport()
    
    i=1
    while(True):
        obj.globalFItemSet[i] = frequentItemsAndSupport
        obj.globalNFItemSet[i] = nonFreqItemSet
        obj.getCandidateItemSets(freqItemSet, i+1)    
        obj.prune(i)
        freqItemSet, frequentItemsAndSupport, nonFreqItemSet = obj.getItemsWithMinSupport()
        if(len(freqItemSet) != 0):
                i = i+1
        else:
            print "Found all frequent itemsets till length: {}".format(i)
            break
    rules = obj.getAssociationRules()
    
    writeRules(rules)
