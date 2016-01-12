'''This module filters the rawDF data read into the doped twister project program, based on user inputted values'''
import pandas as pd 		#import the neccessary modules
import numpy as np

def filter(df):
	threshold = input("\n\nWhat is the lowest acceptable baseline value for the double mutants FC value? All sequences below this value are excluded: ")
	thresh_reads = input("\n\nWhat is the minimum acceptable Number of reads for a given Double mutant? All sequences below this value are excluded: ")
	threshold = float(threshold)
	thresh_reads = float(thresh_reads)

	
	single_mutants = df[df["n"] == 1]  #create two secondary dataframes based on mutational occurrence
	double_mutants = df[df["n"] == 2]
	

	filtered = double_mutants[double_mutants["fc"] >= threshold]
	filtered = filtered[filtered["reads"] >= thresh_reads].copy() 	#create the view
	

	filtered["mut1"] = [x.split(",")[0] for x in filtered["mut"]]   #split the mutants column in filtered
	filtered["mut2"] = [x.split(",")[1] for x in filtered["mut"]]
	

	return (filtered, single_mutants)

	
