import pandas as pd 
import math 

#The probability we test positive for the condition at hand 
Prob_pos_test = (2249/21125)
Prob_neg_test = (18876/21125)

#Prior belief that you had the test will come back positive 
Prior = (2249/21125)

#Likelihood of a positive test given no affliction to condition 
Likelihood = (2089/ 2249)

#Normalize, event that they do not have the condition
Norm = (20933/21125)

#Probability that a women, given a positive test, does not have breast cancer : 
Posterior = (Likelihood * Prior)/Norm

print(Posterior * 100)

#Cost per unncessary case 
Cost = 527

#num uneeded tests, 41,040,355 mammographs preformed each year
#posterior percentage of follow up expednitures that are uncessary 
numUneeded = 41040355 * Posterior

excessHealthExpedntures = numUneeded * Cost

print("Unnecessary Healhcare expenditures from Mammographies alone amount to : ", excessHealthExpedntures)