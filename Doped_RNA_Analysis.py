'''This file is the primary run file for the Doped RNA Analysis package'''

import Twister_Importer
#First use of the menu

opt = Twister_Importer.options(input("\n\n Doped RNA Analyser \n\n===========================================================\n\n 1: Load NGS Data (D)\n 2: Filter the data (F)\n 3: Calculate the products of each DP mutant's correspending SPmutants (P)\n 4: View distribution of data (plot) (V)\n 5: View normalised distribution plot of data (N)\n 6: View a heatmap of the fraction cleaved value for each position (H)\n 7: Calculate list of DPMutants with high FC for several SPMutants (L)\n\n===========================================================\nTo terminate the Doped RNA Analyser, enter 'Q'\n"))

#All subsequent returns to the menu
while opt == "":

	opt = Twister_Importer.options(input("\n\n Doped RNA Analyser \n\n\n===========================================================\n 1: Load NGS Data (D)\n 2: Filter the data (F)\n 3: Calculate products of each DP mutant's correspending SPmutants (P)\n 4: View distribution of data (plot) (V)\n 5: View normalised distribution plot of data (N)\n 6: View a heatmap of the fraction cleaved value for each position (H)\n 7: Calculate list of DPMutants with high FC for several SPMutants (L)\n\n===========================================================\nTo terminate the Doped RNA Analyser, enter 'Q'\n"))

	
