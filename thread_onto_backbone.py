#!/usr/bin/python -tt
#
# -- basicCodeBlock.py
#

import sys
from pymol import cmd, stored

# A dictionary to convert between 
# single-char and three-char amino
# acid names.
def aaLetter(aaChar): 
	return {
		'ARG': 'R',
		'HIS': 'H',
		'LYS': 'K',
		'ASP': 'D', 
		'GLU': 'E',
		'SER': 'S',
		'THR': 'T',
		'ASN': 'N',
		'GLN': 'Q',
		'CYS': 'C',
		'SEC': 'U',
		'GLY': 'G',
		'PRO': 'P',
		'ALA': 'A',
		'ILE': 'I',
		'LEU': 'L',
		'MET': 'M',
		'PHE': 'F',
		'TRP': 'W',
		'TYR': 'Y',
		'VAL': 'V',
		}[aaChar]
		
# A dictionary to convert between 
# single-char and three-char amino
# acid names.		
def aaName(aaChar): 
	return {
		'R': 'ARG',
		'H': 'HIS',
		'K': 'LYS',
		'D': 'ASP', 
		'E': 'GLU',
		'S': 'SER',
		'T': 'THR',
		'N': 'ASN',
		'Q': 'GLN',
		'C': 'CYS',
		'U': 'SEC',
		'G': 'GLY',
		'P': 'PRO',
		'A': 'ALA',
		'I': 'ILE',
		'L': 'LEU',
		'M': 'MET',
		'F': 'PHE',
		'W': 'TRP',
		'Y': 'TYR',
		'V': 'VAL',
		}[aaChar]
		
def intInList(string):
  return int(string)
 
def thread_onto_backbone(backbone_object, backbone_selection, aaString):
#
# 
#  
# create a new temporary dictionary
  stored.tmp_res_dict = {}
  
# store residue indices(=key) and chain(=value)
  cmd.iterate(backbone_selection, "stored.tmp_res_dict[resi] = chain")
  
# create a sorted list of all indices as integers  
  sorted_keys_list = []
  for index_string in stored.tmp_res_dict.keys(): 
    sorted_keys_list.append(int(index_string))
  sorted_keys_list.sort()
  
# set up the mutagenesis wizard
  cmd.wizard("mutagenesis")
  cmd.refresh_wizard()
  
  count = 0
 
  for residue_index in range(sorted_keys_list[0], sorted_keys_list[0] + len(sorted_keys_list) ):
    # get a selection string representation of our current residue
    # e.g. /HPG-3//A/12
    index_string = "%d" %(residue_index)
    selection_str = "/" + backbone_object + "//"+ stored.tmp_res_dict[index_string] + "/%d/" %(residue_index)
    
    # perform the desired mutagenesis
    cmd.get_wizard().do_select(selection_str)
    cmd.get_wizard().set_mode(aaName(aaString[count]))
    cmd.get_wizard().apply()
    
    count = count + 1
    
# close up the mutagenesis wizard    
  cmd.set_wizard()
  
cmd.extend( "thread_onto_backbone", thread_onto_backbone );