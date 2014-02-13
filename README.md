The files in this repository are scripts I've developed as a frequent user of Pymol. I will periodically add more scripts as I make more. 

thread_onto_backbone.py: 

Given a fixed backbone protein structure, this script allows the user to thread a given protein sequence (supplied as a string of one-letter amino acid codes) onto the target backbone structure. 

USAGE: 
To initialize this script, type the following into the pymol terminal:
"run /path-to/script-directory/thread_onto_backbone.py" 
Where "/path-to/script-directory" is replaced with the path to the directory containing this script. 

To call this script in pymol, you must:

1. Select the region of the backbone you'd like to mutate. NOTE: This region must be continuous, and all amino acids of this region must be on the same protein chain. 

2. Call the script via the pymol terminal with the following command: thread_onto_backbone(backbone_object,selection, amino_acid_string). NOTE: backbone_object is the name of the object being mutated, in double quotes. selection is the name of the selection being mutated, in double quotes. amino_acid_string is the string of amino acid single-character codes (all upper case) in double quotes.
