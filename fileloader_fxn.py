#Based on a script written by Valentin Churavay, 19 November 2015

import pandas as pd 		#import the neccessary modules
import numpy as np

#def exel_converter(filename_ex):

def csv_loader(filename):
	df = pd.read_csv(filename)          #read in data and set data thresholds


	labels = ["sequence", "number of mutation" ,"Fraction cleaved", "mutate position", "Total"] #find the labels of data needed
	df = df.loc[:, labels]  #assign data and labels to data frame
	df.rename(columns= {"sequence" : "seq", "number of mutation" : "n" ,"Fraction cleaved" : "fc", "mutate position" : "mut", "Total" : "reads"}, inplace=True)
	print(df.head())   #rename the data labels and check

	return df 
