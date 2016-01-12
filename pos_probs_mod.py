'''This is the Module of the program that calculates the positional scores for FCR for the sequence'''


def fcr1(row):
	mut1 = df[5]   																	#define variables that select mutations from filtered df        	
	fc1 = single_mutants[single_mutants["mut"] == mut1]["fc"].iat[0] 	#iat provides integer based lookups, pulls fc from corresponding mutant
	 																					   #at [0] because is the first location in "fc"
	fcd = filtered["fc"].iat[0]
	if fcd > fc1:
		return fcd - fc1
	else:
		return 0.0
																							#these two functions calculate fcr for each specific mutant
def fcr2(df):	
	mut2 = df[6] 
	fc2 = single_mutants[single_mutants["mut"] == mut2]["fc"].iat[0]
	fcd = filtered["fc"].iat[0]
	if fcd > fc2:
		return fcd - fc2
	else:
		return 0.0
