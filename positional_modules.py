'''This module calculates the positions of the mutants for the SP and DP mutants '''

import numpy as np
import pandas as pd

def str_slicer(string):
	position = 0
	native = ''
	mut_type = ''
	#this function chops up the string with Mutant info, and retrieves mutational scope, position and native base
	if len(string) == 3:
		position = int(string[1:2])
		native = string[0]
		mut_type = string[0] + string[3]
	elif len(string) == 2:
		position = int(string[1])
		native = string[0]
		mut_type = string[0] + string[2]
	else:
		print("\n\nError reading mutant positional values")
	print(position)
	return {position, native, mut_type} #set not working out

def find_pos(dfd):
	 
	#this portion of the modules focuses on the DPmutant DF

	#indexing for mut1 is dfd[5] and for mut2 is dfd[6], dfd[7] contains the SPmutants FC product value
	print(dfd.head)
	dfd["pos1"], dfd["native1"], dfd["mut_type1"] = [str_slicer(dfd["mut1"])(row) for row in dfd.itertuples(False)]
	dfd["pos2"], dfd["native2"], dfd["mut_type2"] = [str_slicer(dfd["mut2"])(row) for row in dfd.itertuples(False)]
	print(dfd.head)
	return dfd
