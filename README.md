# Bayesian-Healthcare-Inefficiencies-
In this repository, I investigate Baye's theorem in Healthcare. Baye's Theorem Elucidates how knowledge about a specific outcome effects the possibility that it will happen. I will apply this train of thought to diagnoses in Healthcare in our to challenge when we make medical interventions. Specifically, I will example the way that increased screening does not lead to better health outcomes. Rather, increased is a huge healthcare ineffiency due to the false positive nature and bayesian probabilities when testing. The large concensus in Healthcare is that more intense screening and testing lead to more effacious results and better long term health outcomes. Surprisingly, this is extremely unture. I am going to uncover this healthcare inefficiency through Bayesian Modeling. Here I propose an algorithm that takes in the positive and false positive data, and returns the estimated unncessary expenditures to the healthcare system. 

To prove the sancitiy of this algorithm, I will preform an example with Mammography's in the united states

This search has wide rangining benefits for health and equity in healthcare. If not reccomended by a doctor, insurance will not always cover the price of a Mammography. A Mammography can cost up to 200 out of pocket for the women of America. Moreover, in light a of positive test, an average of 500+ dollars are spent on the next round of screening. 

In 2023, according to the MQSA (Mammography Quality Standards Act) National Statistics from the FDA, there were a total of 41,040,355 mammography procedures reported in the United States. 
---------------------------------------------------------------------------------------------------------------------------------------
Smaller study for purpose of data analysis : Cost of Breast-Related Care in the Year Following False Positive Screening Mammograms

21,125 women 

160 true positives (0.8%)

2089 false positives (9.9%)

18,884 true negatives (89.2%)

32 false negatives (0.2%).

M : event Mammogrpahy returns positive 
M^c : event Mammography returns Negative

B : Event a woman has breast cancer
B^c : event a woman does not have breast cancer

P(M) : 2249/21,125
P(M^c) : 1 - P(M)

P(B) : 192/21,125
P(B^c) : 20933/21,125

P(B^c | M) = 2089/ 2249

P(Women tests positive given no breast Cancer)

P(M | B^c) = (P(B^c | M)P(M)) / P(B^c)
---------------------------------------------------------------------------------------------------------------------------------------
probability that someone that does not have breast cancer tests positive on a Mammogram : P(M | B^c) = 9.9%

41,040,355 Mammographs per year 

9.9% unnecessary 

500+ additional expenditures 

From our Bayesian analysis of false positives and costs, we see that the healthcare system spends at least 2,158,383,888$ uncessary dollars on mammographies alone

While it is salient to ensure that these women do not have breast cancer, this same pipeline is prevelant all throughout healthcare. We are constantly leaking 
money that could be used to improve patient care and health other healthcare workflows on uncessary expenitures such as this. Furthermore, we start to see 
that more intense screening does not necessarily indicate better healthcare outcomes. Rather, it feeds back into a healthcare inefficiency where we are spending 
uncessary money. Also, to exacerabate the issue, these extra tests are often accompanied with out of pocket expenses.This is prevelant throughout all diagnoses we try to preform.

Final, there are wide ranging ethical concerns for diagnoses such as these. These false positives leave intense mental strain on the these women. Altogether, this calls for a diagnoses pipeline with higher efficacy, not just for mamographs, but for all of healthcare.  