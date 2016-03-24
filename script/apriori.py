from itertools import chain, combinations

def getSupportConfidence():
    flag1 = True
    flag2 = True
    sup = 0
    conf = 0
    while(flag1):
        sup = float(raw_input("\nPlease enter the minimum support value (between 0 and 1): "))
        if(sup>0 and sup<=1):
            while(flag2):
                conf = float(raw_input("\nPlease enter the minimum confidence value (between 0 and 1): "))
                if(conf>0 and conf<=1):
                    flag1 = False
                    flag2 = False
                else:
                    print "\nMinimum Confidence Must Be Between 0 and 1" 
        else:
            print "\nMinimum Support Must Be Between 0 and 1"
    return sup, conf

def getItemsAndTransactions(file_iter):
    transactionList = list()
    itemSet = set()    
    for line in file_iter:
        line = line.strip().rstrip(';').split(';')
        #line = line.strip().rstrip(',').split(',')
        transaction = frozenset(line)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))
    return transactionList, itemSet

def getItemsWithMinSupport(itemSet, transactionList, minSupport):
        length = len(transactionList)
        freqItemSet = set()
        nonFreqItemSet = set()
        freqItemsAndSupport = {}
        itemCounter = {}        
        for item in itemSet:
                itemCounter[item] = 0
                for transaction in transactionList:
                        if item.issubset(transaction):
                                itemCounter[item] += 1
                support = float(itemCounter[item])/length
                if(support >= minSupport):
                    freqItemSet.add(item)    
                    freqItemsAndSupport[item] = support
                else:
                    nonFreqItemSet.add(item)
        print "\t\t{} Non Frequent Itemsets Have Been Pruned".format(len(nonFreqItemSet))
        return freqItemSet, freqItemsAndSupport, nonFreqItemSet

def getCandidateItemSets(set1, k):
    mySet =  set([i.union(j) for i in set1 for j in set1 if len(i.union(j)) == k])
    return mySet
    
def prune(set1, nonFreqItemSet):
    lenBefore = len(set1)
    for i in nonFreqItemSet:
        for j in set1.copy():
            if (j.issuperset(i)):
                set1.remove(j)
    print "\t\t{} ItemSets Have Been Pruned".format(lenBefore - len(set1))
    return set1
    
def getSupport(item):
    return (globalFItemSet[len(item)][item])

def getCombinations(item):
    l1 = []
    l2 = []
    for i in range(0, len(item)):
        l1.append(list(combinations(item, i+1)))
    l2.append(list(chain(*l1)))
    return (l2)
    
def getCombinationSets(l2):
    l3 = []            
    for i in range(0, len(l2)):
        for j in l2[i]:
            l3.append(frozenset(j))
    return (l3)
    
def printFrequentItemSets():
    for key, value in globalFItemSet.items()[1:]:
        for item, support in value.items():
            print "\t\t{} : {}".format(tuple(item), support)
            #print tuple(item), support
            
def printItemSets(itemset):
    count = 0
    print "\t\t{} Frequent Itemsets Have Been Obtained".format(len(itemset))
    for key, value in itemset.items():
        print "\t\t%s ==> %0.2f" %(tuple(key), value)
        count += 1
        if(count >=5):
            print "\t\t..........................."
            break


def getAssociationRules():
    assocRules = []
    for key, value in globalFItemSet.items()[1:]:
            for item in value:
                l2 = getCombinations(item)
                l3 = getCombinationSets(l2)            
                for element in l3:
                    diff = item.difference(element)
                    if(len(diff) > 0):
                        confidence = getSupport(item)/getSupport(element)
                        if(confidence >= minConfidence):
                            assocRules.append((("{} ==> {}".format(tuple(element), tuple(diff))), (confidence)))
    print "\t\t{} Association Rules Have Been Generated".format(len(assocRules))
    return assocRules

def printAssociationRules(rules):
    rules = sorted(rules, reverse=False)
    for i in range(0, len(rules)):
        print "\t\t{} : %0.2f".format(rules[i][0])%rules[i][1]


#filename = 'sample.csv'
#filename = 'trnlist2.csv'
#filename = 'trnlist2.txt'

if __name__ == "__main__":

    filenames = []
    filenames.append('electronics.txt')
    filenames.append('grooming.txt')
    filenames.append('officeproducts.txt')
    filenames.append('kitchen.txt')
    filenames.append('amazonbasics.txt')

    
    run_count = 0
    for current_file in filenames:
        run_count += 1    
        print "------------------------------------------------------------------------"
        print "\nStarting Run {}".format(run_count)
        
        print "\nProcessing File: {}".format(current_file)
        file_iter = open(current_file, 'rU')
        
        minSupport = 0
        minConfidence = 0
        globalFItemSet = {} #A dictionary of all frequent itemsets.
        globalNFItemSet = {} #A dictionary of all non-frequent itemsets.
        
        minSupport, minConfidence = getSupportConfidence()
        print "\nThe minimum support value is: {}".format(minSupport)
        print "\nThe minimum confidence value is: {}".format(minConfidence)
    
        print "\nObtaining Items And Transactions."
        transactionList, itemSet = getItemsAndTransactions(file_iter)
        for i in transactionList:
            print "\t\t{}".format(tuple(i))
        print "\n\t\t{} Transactions Obtained\n".format(len(transactionList))
        wait = raw_input("\nPress Return Key To Continue.")
        
        print "\nObtaining Initial Items With Support >= {}".format(minSupport)
        freqItemSet, frequentItemsAndSupport, nonFreqItemSet = getItemsWithMinSupport(itemSet, transactionList, minSupport)
        
        i = 1
    
        while(True):
            print "------------------------------------------------------------------------"
            print "\nBeginning Pass {}".format(i)
            globalFItemSet[i] = frequentItemsAndSupport
            globalNFItemSet[i] = nonFreqItemSet
            
            print "\nPrinting Frequent Items From Pass {}".format(i)
            printItemSets(globalFItemSet[i])
            
            print "\nMerging Frequent {}-itemsets To Form Candidate {}-itemsets".format(i, i+1)
            itemSet = getCandidateItemSets(freqItemSet, i+1)
            count = 0
            print "\t\t{} Candidate {}-itemsets Have Been Formed".format(len(itemSet), i+1)
            for item in itemSet:
                print "\t\t{}".format(tuple(item))
                count += 1
                if(count > 3):
                    break
            print "\t\t..........................."
            
            print "\nPruning {}-itemsets".format(i+1)
            itemSet = prune(itemSet, globalNFItemSet[i])
            
            print "\nPruning {}-itemsets Based On Minimum Support".format(i+1)
            freqItemSet, frequentItemsAndSupport, nonFreqItemSet = getItemsWithMinSupport(itemSet, transactionList, minSupport)
                
            if(len(freqItemSet) != 0):
                i = i+1
            else:
                print "------------------------------------------------------------------------"
                print "\nFound All Frequent Itemsets Till Length: {}".format(i)
                break
            
        print "------------------------------------------------------------------------"
        print "\nGenerating Association Rules\n"
        assocRules = getAssociationRules()
        print "------------------------------------------------------------------------"
        print "\nPrinting Frequent ItemSets\n"
        printFrequentItemSets()
        print "------------------------------------------------------------------------"
        print "\nPrinting Association Rules\n"
        printAssociationRules(assocRules)
        
        wait = raw_input("\nPress Return Key to Start the Next Run")
        
    print "\n\nProgram Has Completed {} Runs Successfully!\n".format(run_count)
