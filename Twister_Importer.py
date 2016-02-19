'''This is the Primary Module for the simple GUI for Analyzing Shungo's NGS Data'''

## This Function takes user input from the interface and calls all other modules and functions ##
def options(menu):

## ---- Option 1, step 1: Load the NGS data, distinguish filetype ------------------------------------ ##
	if menu == "1" or menu == "D":
		import fileloader_module
		filename = input("\n\nPlease enter the name of the file you would like to analyse, character for character: ")	
		filetype = int(input("\nIs this an .xls/.xlsx file (type 1) or a csv file (type 2)? Enter the appropriate value, i.e 1 or 2: "))
		if filetype == 1: 
			rawDF = fileloader_module.excel_loader(filename)
		elif filetype == 2:
			rawDF = fileloader_module.csv_loader(filename)
		else:
			print("\nError. Go back to Menu and try again")	
		print(rawDF)

## ---- Option 2: Filter the data based on user preferences ---------------------------------- ##
	elif menu == "2" or menu == "F": 
		import filtering_module
		global rawDF
		out = filtering_module.filter(rawDF)
		filtered_doubles = out[0]
		single_mutants = out[1]
		#print(filtered_doubles)
		#print(single_mutants)
		

## ---- Option 3: Calculate the Product each dpM's corresponding single mutants -------------- ##
	elif menu == "3" or menu == "P": 
		import spm_product_module
		global filtered_doubles 
		global single_mutants
		dbls_wprods = spm_product_module.pullproduct(filtered_doubles, single_mutants)
		


## ---- Option 4: View the distribution of the Product Data ---------------------------------- ##
	elif menu == "4" or menu == "V":
		import prod_dist_module
		global dbls_wprods
		prod_dist_module.distri(dbls_wprods)
	

## ---- Option 5: View the distribution of the normalised Product Data ----------------------- ##
	elif menu == "5" or menu == "N":
		import prod_dist_module
		global dbls_wprods
		prod_dist_module.norm_distri(dbls_wprods)
	


## ---- Option 7: Mine the positions and mutant types from mutation data --------------------- ##
	elif menu == "7":

		import positional_module
		import fcr_module
		 
		mined_doubles = positional_module.find_posD(filtered_doubles)
		mined_singles = positional_module.find_posS(single_mutants)
		df_new = fcr_module.remove_dups(mined_doubles)
		a_df = fcr_module.calc_fcr(df_new, mined_singles)
		#print(a_df)


## ---- Option 6: View the heatmap of the dataset in terms of FC ----------------------------- ##

	elif menu == "6":
		import Heat_mod
		global mined_doubles 
		global mined_singles
		Heat_mod.mkfile(mined_doubles, mined_singles)
		#Heat_mod.showmap(mined_doubles, mined_singles)

## ---- Option 8: Menu escape and return ----------------------------------------------------- ##
	elif menu == "" or menu == "Q":
		last = input("\nDo you want to exit [Enter] or do you want go back to the menu? (M)")
		if last == "":
			return "\nexit"
		if last == "M":
			return ""
	return ""

## ---- Running the Main Menu ---- ##
#First instance of the menu
opt = options(input("\n\n Doped RNA Analyser \n\n===========================================================\n\n 1: Load NGS Data (D)\n 2: Re/Filter the data (F)\n 3: Calculate the products of each DP mutant's correspending SPmutants (P)\n 4: View distribution of data (plot) (V)\n 5: View normalised distribution plot of data (N)\n 6: View a heatmap of the fraction cleaved value for each position (H)\n 7: Calculate list of DPMutants with high FC for several SPMutants (L)\n\n===========================================================\nTo terminate the Doped RNA Analyser, enter 'Q'\n"))

#All subsequent returns to the menu
while opt == "":
	opt = options(input("\n\n Doped RNA Analyser \n\n\n===========================================================\n 1: Load NGS Data (D)\n 2: Re/Filter the data (F)\n 3: Calculate products of each DP mutant's correspending SPmutants (P)\n 4: View distribution of data (plot) (V)\n 5: View normalised distribution plot of data (N)\n 6: View a heatmap of the fraction cleaved value for each position (H)\n 7: Calculate list of DPMutants with high FC for several SPMutants (L)\n\n===========================================================\nTo terminate the Doped RNA Analyser, enter 'Q'\n"))
