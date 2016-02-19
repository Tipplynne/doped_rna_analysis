'''This is the heatmap plot Module for the simple GUI for Analyzing Shungo's NGS Data'''

#resources: 

#http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor

#http://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set

#http://nekoyukimmm.hatenablog.com/entry/2015/03/25/180528

#http://nbviewer.ipython.org/github/rasbt/matplotlib-gallery/blob/master/ipynb/heatmaps.ipynb

import numpy as np 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

## first make a seperate data file, with grouped values, just to speed up dev

def mkfile(dfd, dfs):
	#first open file
	writer = pd.ExcelWriter('grouped_data_4heat.xlsx')

	#create the groupby object
	
	gb1 = (dfd['fc'].groupby([dfd['position1'],dfd['position2'],dfd['mut_type1'],dfd['mut_type2']]).max())
	
	gb2 = (dfd['fc'].groupby([dfd['position1'],dfd['mut_type1']]).max())
	gb3 = (dfd['fc'].groupby([dfd['position2'],dfd['mut_type2']]).max())
	#print(gb2)
	
	#writing the results of gb1 on dfd to new df
	dfgb1 = pd.DataFrame(gb1)
	dfgb2 = pd.DataFrame(gb2)
	dfgb3 = pd.DataFrame(gb3)

	dfgb1.to_excel(writer,'FC by pos and mut type')
	dfgb2.to_excel(writer,'FC by pos1 and mut type')
	dfgb3.to_excel(writer,'FC by pos2 and mut type')

	#trying something
	
	pivotplay = pd.pivot_table(dfd, values="fc", index=['position1','mut_type1'], columns=['position2','mut_type2']) #err is for multiple index entries
	pivotplay.to_excel(writer,'TheMatrix')

#heatmapping fxn
def showmap(dfd, dfs):
	pass	



	
