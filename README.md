# AprioriPython
A python implementation of the Apriori algorithm for finding frequent item sets and association rules from transaction data.

1) Data: 

  Make sure the file that contains the list of transactions is in the following format:
	
      T1item1;T1item2;T1item3;......;T1itemN
      T2item1;T2item2;T2item3;......;T2itemN
      T3item1;T3item2;T3item3;......;T3itemN
      ......................................
      ......................................
      ......................................
      TNitem1;TNitem2;TNitem3;......;TNitemN
    
    
2) Running in python:

  $ python runapriori.py -s S -c C -p P

		-s, Minimum support value (0-1)
		-c, Minimum confidence value (0-1)
		-p, Path to the input data file
