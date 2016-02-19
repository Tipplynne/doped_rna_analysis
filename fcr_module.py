'''This module calculates the mutational positions that return high FCR mutants '''

import numpy as np
import pandas as pd
from pandas import ExcelWriter

def remove_dups(dfd):
	#this function pulls the fc values, mutational scope for each position in the sequence and stores the data in a dictionary/df?
	#indexing for dfd: mut1[5], mut2[6], position1[7], native1[8], mut_type1[9], position2[10], native2[11], mut_type2[12], fc[2]
	#indexing for dfs mut[3] position[5], native[6], mut_type[7]
	temp_df = pd.DataFrame()
	new_df = pd.DataFrame()
	pos = 0
	for pos in range(0,60):	
		#convert pos to string
		s = str(pos)
		#retrieve only dpms with first mutational position = pos and second mutational position is greater than pos. This essentially removes any duplicates from the dataset. (In Shungo's original dataset this drops from 9918 to 8769).
		temp_df = dfd[(dfd.position1 == s) & (dfd.position2 > s)]
		new_df = pd.concat([new_df, temp_df])		
		pos = pos + 1
	return new_df

def calc_fcr(dfd, dfs):
	#this function calculates the fcr for each mutation type. This is where it gets tricky. Will be attempting to use the groupBy function
#Ideally, we want to use this information to calculate not only FCR but percentage of type mutations and paired type mutations.

	def fcr1(row):
		mut1 = row[5]
		#define variables that select mutations from filtered df 
		     	
		fc1 = dfs[dfs["mut"] == mut1]["fc"].iat[0] 	#iat provides integer based lookups, pulls fc from corresponding mutant
		 																					   
		fcd = dfd["fc"].iat[0]
		if fcd > fc1:
			return fcd - fc1
		else:
			return 0.0
																								#these two functions calculate fcr for each specific mutant
	def fcr2(row):	
		mut2 = row[6] 
		fc2 = dfs[dfs["mut"] == mut2]["fc"].iat[0]
		fcd = dfd["fc"].iat[0]
		if fcd > fc2:
			return fcd - fc2
		else:
			return 0.0
	
	#dfd["fcr_Mut1"] = [fcr1(row) for row in dfd.itertuples(False)]  	  		#record fcr for each mutant
	#dfd["fcr_Mut2"] = [fcr2(row) for row in dfd.itertuples(False)]
	
	#open an excel file for analysis of the data
	writer = ExcelWriter('groupby_tests.xlsx')
	
	gb1 = (dfd['fc'].groupby([dfd['position1'],dfd['position2'],dfd['mut_type1'], dfd['mut_type2']]).max())

	#try 2 different methods of writing a groupby object to new df
	dfgb1 = pd.DataFrame(gb1)
	#don't need no. 2 for now
	#dfgb2 = gb1.reset_index()

	#write the groupby objects to file
	dfgb1.to_excel(writer,'FC by pos and mut type')
	#dfgb2.to_excel(writer,'redo2')
	
	#looking at relative mutant_type abundance in DPMs
	gb2 = (dfd['fc'].groupby([dfd['mut_type1'], dfd['mut_type2']]).describe())
	dfgb2 = pd.DataFrame(gb2)
	dfgb2.to_excel(writer,'Stats on DPM FC by mut type')

	#looking for relative mutant_type abundance in spms
	gb3 = (dfs['fc'].groupby(dfs['mut_type']).describe())
	dfgb3 = pd.DataFrame(gb3)
	dfgb3.to_excel(writer,'Stats on SPM FC by mut type')

	return dfd
	#BUG: the program is returningID values of fcr for several 2nd pos mutants, also not really grouping the data in the right way yet
	

def fcr_filter(dfd):
	#this function filters the data for some threshold of FCR
	pass
