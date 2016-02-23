'''This is the heatmap plot Module for the simple GUI for Analyzing Shungo's NGS Data'''

#resources: 

#http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor

#http://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set

#http://nekoyukimmm.hatenablog.com/entry/2015/03/25/180528

#http://nbviewer.ipython.org/github/rasbt/matplotlib-gallery/blob/master/ipynb/heatmaps.ipynb

#Maybe attempt to normalise over the whole matrix: http://stackoverflow.com/questions/10715519/conditionally-fill-column-values-based-on-another-columns-value-in-pandas

import numpy as np 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

## first make a seperate data file, with grouped values, just to speed up dev

def mkfile(dfd, dfs):
	#first open file
	writer = pd.ExcelWriter('grouped_data_4heat.xlsx')

	#using pivot_table method to create matrix
	
	pivotplay = pd.pivot_table(dfd, values="fc", index=['position1','mut_type1'], columns=['position2','mut_type2']) 

	#need to fill the ID portion of the matrix, using the set_value fxn: 
	#df.set_value('Col', 'Index', value) or using some nifty solns found here: http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/
	print(dfs)
	def fillID(x):
		if type(x) is None:
			return 
		
	print(pivotplay)
			
	pivotplay.to_excel(writer,'TheMatrix')

#heatmapping fxn
def showmap(df):
	pass	



	
