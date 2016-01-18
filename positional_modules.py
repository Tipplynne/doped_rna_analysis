'''This module calculates the positions of the mutants for the SP and DP mutants '''

import numpy as np
import pandas as pd

def str_slicer(row):
	s = row[5]
	position = 0
	native = ''
	mut_type = ''
	
	#this function chops up the string with Mutant info, and retrieves mutational scope, position and native base
	if len(s) == 4:
		position = int(s[1:3])
		native = s[0]
		mut_type = s[0] + s[3]
	elif len(s) == 3:
		position = int(s[1:2])
		native = s[0]
		mut_type = s[0] + s[2]
	else:
		print("\n\nError reading mutant positional values")
	return position, native, mut_type #BUG1p1 tried and failed as tuple, list, need to try tostring() then split method?

def find_pos(dfd):
	 
	#this portion of the module focuses on the DPmutant DF
	global position
	global native
	global mut_type
	#indexing for mut1 is dfd[5] and for mut2 is dfd[6], dfd[7] contains the SPmutants FC product value
	#print(dfd.head)

	###BUG1p2 serious issues with unpacking to pandas df - laaaame
	dfd["packed1"] = ([str_slicer(row) for row in dfd.itertuples(False)])
	
	#dfd["pos1"], dfd["native1"], dfd["mut_type1"] = ([str_slicer(row) for row in dfd.itertuples(False)])
	#(dfd["pos2"], dfd["native2"], dfd["mut_type2"]) = [str_slicer(dfd["mut2"])(row) for row in dfd.itertuples(False)]
	#print(dfd.head)
	return dfd
