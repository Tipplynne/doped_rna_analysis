'''This module calculates the positions of the mutants for the SP and DP mutants '''

import numpy as np
import pandas as pd

def str_slicer(row):
	s = row
	position = 0
	native = ''
	mut_type = ''
	
	#this function chops up the string with Mutant info, and retrieves mutational scope, position and native base as a packed column. string may be composed of 3 or 4 chars eg. A9C or A25C, where A is the native base, A-> C is scope and 9 and 25, are the respective mutation positions 
	if len(s) == 4:
		position = s[1:3]
		native = s[0]
		mut_type = s[0] + s[3]
	elif len(s) == 3:
		position = s[1:2]
		native = s[0]
		mut_type = s[0] + s[2]
	else:
		print("\n\nError reading mutant positional values")
	
	return position, native, mut_type 

def find_posD(dfd):
	 
	#this fxn focuses on the DPmutant DF, uses the string slicer to extract info; indexing for mut1 is dfd[5] and for mut2 is dfd[6], dfd[7] contains the SPmutants FC product value
	dfd["packed1"] = ([str_slicer(row[5]) for row in dfd.itertuples(False)])
	dfd["packed2"] = ([str_slicer(row[6]) for row in dfd.itertuples(False)])
	unpack1 = ('position1', 'native1', 'mut_type1')
	unpack2 = ('position2', 'native2', 'mut_type2')

	#unpack etc is new column names, create new dfs for each mutation
	df1 = dfd.packed1.apply(lambda loc: pd.Series(loc, index = unpack1))
	df2 = dfd.packed2.apply(lambda loc: pd.Series(loc, index = unpack2))

	#appends new df to dfd, and drops temporarly packed output columns
	dfd = pd.concat([dfd, df1, df2], axis=1, join_axes=[dfd.index])
	dfd = dfd.drop('packed1',axis=1)
	dfd = dfd.drop('packed2',axis=1)
	
	return dfd

def find_posS(dfd):
	 
	#this fxn focuses on the DPmutant DF, uses the string slicer to extract info; indexing for mut1 is dfd[5] and for mut2 is dfd[6], dfd[7] contains the SPmutants FC product value
	dfd["packed"] = ([str_slicer(row[3]) for row in dfd.itertuples(False)])
	unpack = ('position', 'native', 'mut_type')

	#unpack etc is new column names, create new dfs for each mutation
	df1 = dfd.packed.apply(lambda loc: pd.Series(loc, index = unpack))
	
	#appends new df to dfd, and drops temporarly packed output columns
	dfd = pd.concat([dfd, df1], axis=1, join_axes=[dfd.index])
	dfd = dfd.drop('packed',axis=1)
	
	return dfd
