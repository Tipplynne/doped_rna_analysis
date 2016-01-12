'''This module calculates the product of the FC values for the SPmutants that correspond to each given DPmutants'''

def pullproduct(dpm, spm):   

	def fcproduct(row):     														#create a fxn for calculating mutant products
	  
		mut1 = row[5]
		mut2 = row[6]  
														#define variables that select mutations from filtered df
	
		fc1 = spm[spm["mut"] == mut1]["fc"].iat[0]	#iat [0] provides integer based lookups, pulls fc from corresponding mutant
		print(fc1)
		fc2 = spm[spm["mut"] == mut2]["fc"].iat[0] 	#iat [0] because is the first location in "fc" 
		print(fc2)
		return fc1 * fc2

#call the fcproduct fxn in spm_product_module, using .itertuples(), which iterates over the rows of filtered df as tuples, with index value as first element of the tuple 

#using itertuples(False) seems to call all but index to tuple	

	dpm["fcp"] = [fcproduct(row) for row in dpm.itertuples(False)]

	return dpm


