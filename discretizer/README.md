### Discretizer

This module is responsible for creating the data to be fed into the classifier and decision tree.  `discreteize_data.py` controls the creation of CSV files (to be converted into ARFF by Weka). The raw data has all of the attributes trained on as well as the non-discretized price variable. 

The labels tested are all `buy`, `sell`, and `hold`. However the package is set up to handle 