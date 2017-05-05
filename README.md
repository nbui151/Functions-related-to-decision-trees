# Functions-related-to-decision-trees
simple_disorder(category, outcome)

This function calculates the disorder (or also called entropy) for two vectors

for binary outcome, max disorder = 1, min disorder = 0 

formula comes from MIT Professor Patrick Winston's book Artificial Intelligence p. 429 
 

one_layer(data, Y_column_name)

this function takes as input the dataframe and the column name that signifies the outcome variable 

returns the first feature in the decision tree based on which one has the lowest disorder 


two_layer(data, Y_column_name)

this function takes as input the dataframe and the column name that signifies the outcome variable 

returns the first feature in the decision tree based on which one has the lowest disorder 

then based on the first feature, returns for each value the second feature that should be chosen by the decision tree 
