import numpy as np 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def excel_loader(filename):
	xlsx = pd.ExcelFile(filename)
	df = pd.read_excel(xlsx)
	labels = ["position1", "position2" ,"mut_type1", "mut_type2", "fc"] #find the labels of data needed
	df = df.loc[:, labels]  #assign data and labels to data frame
	
	return df 

excel_loader("grouped_data4heat.xlsx")



