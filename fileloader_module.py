'''This module reads in files for the Doped Twister project, in either .csv or .xls format (which it subsequently transforms to .csv format)'''

import pandas as pd 		#import the neccessary modules
import numpy as np


def excel_loader(filename):
	xlsx = pd.ExcelFile(filename)
	df = pd.read_excel(xlsx)
	labels = ["sequence", "number of mutation" ,"Fraction cleaved", "mutate position", "Total"] #find the labels of data needed
	df = df.loc[:, labels]  #assign data and labels to data frame
	df.rename(columns= {"sequence" : "seq", "number of mutation" : "n" ,"Fraction cleaved" : "fc", "mutate position" : "mut", "Total" : "reads"}, inplace=True)
	
	return df 

def csv_loader(filename):
	df = pd.read_csv(filename)          #read in data and set data thresholds
	labels = ["sequence", "number of mutation" ,"Fraction cleaved", "mutate position", "Total"] #find the labels of data needed
	df = df.loc[:, labels]  #assign data and labels to data frame
	df.rename(columns= {"sequence" : "seq", "number of mutation" : "n" ,"Fraction cleaved" : "fc", "mutate position" : "mut", "Total" : "reads"}, inplace=True)

	return df 
