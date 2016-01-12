#Based on a script written by Valentin Churavay, 19 November 2015, modified by Crys

import pandas as pd 		#import the neccessary modules
import numpy as np

df = pd.read_csv("Shungo doped twister.csv")          #read in data and set data thresholds
threshold = input("What is the lowest acceptable baseline value for the double mutants FC value? All sequences below this value are excluded: ")
thresh_reads = input("What is the minimum acceptable Number of reads for a given Double mutant? All sequences below this value are excluded: ")
threshold = float(threshold)
thresh_reads = float(thresh_reads)

labels = ["sequence", "number of mutation" ,"Fraction cleaved", "mutate position", "Total"] #find the labels of data needed
df = df.loc[:, labels]  #assign data and labels to data frame
df.rename(columns= {"sequence" : "seq", "number of mutation" : "n" ,"Fraction cleaved" : "fc", "mutate position" : "mut", "Total" : "reads"}, inplace=True)
#print df.head()   #rename the data labels and check

single_mutants = df[df["n"] == 1]  #create two secondary dataframes based on mutational occurrence
double_mutants = df[df["n"] == 2]

filtered = double_mutants[double_mutants["fc"] >= threshold]
filtered = filtered[filtered["reads"] >= thresh_reads].copy() 	#create the view
#print filtered.head()

filtered["mut1"] = [x.split(",")[0] for x in filtered["mut"]]  #split the mutants column in filtered
filtered["mut2"] = [x.split(",")[1] for x in filtered["mut"]]
#print filtered.head()

def fcproduct(row):          														#create a fxn for calculating mutant products
	mut1 = row[5]
	mut2 = row[6]            														#define variables that select mutations from filtered df
	
	fc1 = single_mutants[single_mutants["mut"] == mut1]["fc"].iat[0] 	#iat provides integer based lookups, pulls fc from corresponding mutant
	fc2 = single_mutants[single_mutants["mut"] == mut2]["fc"].iat[0]  #at [0] because is the first location in "fc" 
	return fc1 * fc2
	
filtered["fcp"] = [fcproduct(row) for row in filtered.itertuples(False)] 
#call the fxn, using .itertuples(), which iterates over the rows of filtered df as tuples, with index value as first element of the tuple 
#using itertuples(False) seems to call all but index to tuple

#print filtered.head()

def fcr1(row):
	mut1 = row[5]   																	#define variables that select mutations from filtered df        	
	fc1 = single_mutants[single_mutants["mut"] == mut1]["fc"].iat[0] 	#iat provides integer based lookups, pulls fc from corresponding mutant
	 																					   #at [0] because is the first location in "fc"
	fcd = filtered["fc"].iat[0]
	if fcd > fc1:
		return fcd - fc1
	else:
		return 0.0
																							#these two functions calculate fcr for each specific mutant
def fcr2(row):	
	mut2 = row[6] 
	fc2 = single_mutants[single_mutants["mut"] == mut2]["fc"].iat[0]
	fcd = filtered["fc"].iat[0]
	if fcd > fc2:
		return fcd - fc2
	else:
		return 0.0
	
filtered["fcr_Mut1"] = [fcr1(row) for row in filtered.itertuples(False)]  	  		#record fcr for each mutant
filtered["fcr_Mut2"] = [fcr2(row) for row in filtered.itertuples(False)] 

def pullpos1(row):
	import re	
	mut1 = row[5]   
	pos1 = 0
	i = 0
	for i in range(10,56):
		string = str(i)
		RegexID = re.compile(string)
		if RegexID.search(mut1):
			pos1 = i
			break
	return pos1
																											#these two functions calculate pos for each specific mutant																		
def pullpos2(row):
	mut2 = row[6] 	
	import re																			
	pos2 = 0
	i = 0
	for i in range(10,56):
		string = str(i)
		RegexID = re.compile(string)
		if RegexID.search(mut2):
			pos2 = i
			break
	return pos2
	
filtered["Mut_pos1"] = [pullpos1(row) for row in filtered.itertuples(False)]  	#record pos for each mutant
filtered["Mut_pos2"] = [pullpos2(row) for row in filtered.itertuples(False)] 

###################################################################################
## Creating a Normalised data set of filtered products: based on code from http://chrisalbon.com/python/pandas_normalize_column.html	




import matplotlib.pyplot as plt
import pylab


filtered.plot(kind='scatter', x='fcp', y='fc');
pylab.show()
																							

def rem_rows(row):
	val1 = row[8]
	val2 = row[9]
	
	return val1 + val2																			#to remove empty rows
			
filtered["row_checker"] = [rem_rows(row) for row in filtered.itertuples(False)] 
filtered = filtered[filtered.row_checker > 0.0]

import matplotlib.pyplot as plt
import pylab

filtered.plot(kind='scatter', x='fcp', y='fc');


plt.ylim((-0.01,1.01))
plt.xlim((-0.01,1.01))
plt.ylabel('Double Mutant FC Value')
plt.xlabel('Product of corresponding Single Mutant FC Values')


z = np.polyfit(x, y, 1)
p = np.poly1d(z)
pylab.plot(x,p(x),"r-")
# the line equation:
#print "y=%.6fx+(%.6f)"%(z[0],z[1])

from scipy.stats import pearsonr
pearsonr(x, y)
#print pearsonr(x, y)
plt.suptitle(pearsonr(x, y))

pylab.show()
																							
#print filtered.head()

filtered.to_csv('Products_All.csv', sheet_name='Sheet1') 										#print to file



