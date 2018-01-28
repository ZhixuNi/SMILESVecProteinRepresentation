#DIRNAME=$(date +%Y%m%d_%H%M%S)
#mkdir "docs" #$DIRNAME
mkdir "outputs" #$DIRNAME
#mkdir "data" #$DIRNAME

LRNDRUGLINGO="data/word/drug.l8.chembl23.canon.ws20.txt" 
LRNDRUGLINGOPub="data/word/drug.pubchem.canon.l8.ws20.txt" 


LRNDRUGCHR="data/char/drug.chembl.canon.l1.ws20.txt"
LRNDRUGCHRPub="data/char/drug.pubchem.canon.l1.ws20.txt"

LRNPROTLINGO="data/word/prot.l3.w20.100d.txt"
LRNPROTCHR="data/char/prot.w25.d100.txt"

SEQFILE="a50/a50fam.se.filtered" 
PAIRList="a50/a50fam.se.filtered.pairs"
SMILESFILE="a50/a50fam.se.filtered.smiles"

INTERACTIONFILE="a50/a50fam.se.filtered.interactions"

MODELCHOICE=2
ldrugLen=8
lprotLen=3
SMICHOICE=2

#(LRNPATH, pairfile, proteinspath, wordChar, protOrLig, q, MODELCHOICE) 
##Prot2vec

#awk "BEGIN { print \"Computing similarity list..!!\" }"
#python lingosim.py $LRNPROTLINGO $PAIRList $SEQFILE "wd" "p" $lprotLen $MODELCHOICE 


#Smiles2vec

awk "BEGIN { print \"Computing similarity list..!!\" }"
python lingosmi.py $LRNDRUGLINGOPub $PAIRList $SMILESFILE "wd" "l" $ldrugLen  $INTERACTIONFILE $SMICHOICE #MODEL AVG

$SHELL
