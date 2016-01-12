import matplotlib.pyplot as plt
import pylab


filtered.plot(kind='scatter', x='fcp', y='fc');
pylab.show()
																							

def rem_rows(row):
	val1 = row[8]
	val2 = row[9]
	
	return val1 + val2																			#to remove empty rows
			
filtered["row_checker"] = [rem_rows(row) for row in filtered.itertuples(False)] 
filtered = filtered[filtered.row_checker > 0.0]
