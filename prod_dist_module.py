'''This module produces a plot of DPmutant FC values vs Product of the FC values of the respective corresponding SPmutants'''

#import the libraries, pylab mostly to run the viewer
import matplotlib.pyplot as plt
import numpy as np
import pylab

def distri(DF):
	DF.plot(kind='scatter', x='fcp', y='fc');
	plt.ylim((-0.01,1.01))
	plt.xlim((-0.01,1.01))
	plt.ylabel('Double Mutant FC Value')
	plt.xlabel('Product of corresponding Single Mutant FC Values')
	#plot the linear correlation (default = red)
	#assign x, y because x and y above are in plot()'s namespace 
	x=DF['fcp']
	y=DF['fc']
	z = np.polyfit(x, y, 1) 
	p = np.poly1d(z)
	pylab.plot(x,p(x),"r-")
	# the line equation:
	#print "y=%.6fx+(%.6f)"%(z[0],z[1])

	from scipy.stats import pearsonr
	pearsonr(x, y)
	#print pearsonr(x, y)
	plt.suptitle(pearsonr(x, y))
	pylab.show()

def norm_distri(DF):

## Creating a Normalised data set of filtered products: based on code from http://chrisalbon.com/python/pandas_normalize_column.html
	#calculating the normalised values of the SP mutant products

	DF["norm_fcp"] = (DF['fcp'] - DF['fcp'].min()) / (DF['fcp'].max() - DF['fcp'].min())
	
	DF.plot(kind='scatter', x='norm_fcp', y='fc');
	plt.ylim((-0.01,1.01))
	plt.xlim((-0.01,1.01))
	plt.ylabel('Double Mutant FC Values')
	plt.xlabel('Normalised Product of corresponding Single Mutant FC Values')
	#plot the linear correlation (default = red)
	#assign x, y because x and y above are in plot()'s namespace 
	x=DF['norm_fcp']
	y=DF['fc']
	z = np.polyfit(x, y, 1)
	p = np.poly1d(z)
	pylab.plot(x,p(x),"r-")
	# the line equation:
	#print "y=%.6fx+(%.6f)"%(z[0],z[1])

	from scipy.stats import pearsonr
	pearsonr(x, y)
	#print pearsonr(x, y)
	plt.suptitle(pearsonr(x, y))
	pylab.show()


