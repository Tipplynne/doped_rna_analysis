'''This is the heatmap plot Module for the simple GUI for Analyzing Shungo's NGS Data'''

#resources: 

#Maybe attempt to normalise over the whole matrix: http://stackoverflow.com/questions/10715519/conditionally-fill-column-values-based-on-another-columns-value-in-pandas

import numpy as np 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

## first make a seperate data file, with grouped values, just to speed up dev

def mkfile(dfd, dfs):
	#first open file
	writer = pd.ExcelWriter('grouped_data_4heat.xlsx')
	dfd.sort_index()
	print(dfd)

	#using pivot_table method to create the half matrix
	pivotplay1 = pd.pivot_table(dfd, values="fc", index=['position1','mut_type1'], columns=['position2','mut_type2']) 
	
	#create the transposed half matrix
	pivotplay2 = pd.pivot_table(dfd, values="fc", index=['position2','mut_type2'], columns=['position1','mut_type1'])

	#sneakily rename the levels in transposed matrix
	pivotplay2.index.names = pivotplay1.index.names
	pivotplay2.columns.names = pivotplay1.columns.names

	#merge the two matrices
	combined_pivot = pivotplay1.combine_first(pivotplay2)
	combined_pivot.to_excel(writer,'combined_pivot')

   	#need to fill the ID portion of the matrix, using the set_value fxn: 
	#df.set_value('Col', 'Index', value) or using some nifty solns found here: http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/
	print(dfs)

	def fill_id(x):
		if type(x) is NaN:
			if dfs('mut_type', 'position') == combined_pivot(x, 'mut_type1','position1'):
				return dfs('fc')
			else:
				return 0

	combined_pivot.applymap(fill_id)
	#Notes: need to debug the whole fxn
    

	#fix the weird indexing issue created from the cleaning step in positional module
	
	#So, these 2 are not working
	#index_check1 = pivotplay.sortlevel(["position1"], sort_remaining=False)		
	#index_check1.to_excel(writer,'index_check1')

	#pivotplay = pivotplay.sort(['position2'],ascending=[1])


    
		

#heatmapping fxn

#resources: 

#http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor

#http://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set

#http://nekoyukimmm.hatenablog.com/entry/2015/03/25/180528

#http://nbviewer.ipython.org/github/rasbt/matplotlib-gallery/blob/master/ipynb/heatmaps.ipynb
def showmap(df):
	pass	



	
