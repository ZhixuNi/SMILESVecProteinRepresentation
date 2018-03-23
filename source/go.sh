#DIRNAME=$(date +%Y%m%d_%H%M%S)
#mkdir "docs" #$DIRNAME
mkdir "outputs" #$DIRNAME



LRNDRUGLINGO8="data/word/drug.l8.chembl23.canon.ws20.txt" 
LRNDRUGCHR1="data/char/drug.l1.chembl23.canon.ws20.txt"
LRNDRUGCHR1Pub="data/char/drug.l1.pubchem.canon.ws20.txt"

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

#Arguments: LRNPATH, pairfile, proteinspath, wordChar, protOrLig, q, MODELCHOICE 
##ProtVec

awk "BEGIN { print \"Computing similarity list..!!\" }"
python lingosim.py $LRNPROTLINGO $PAIRList $SEQFILE "wd" "p" $lprotLen $MODELCHOICE 


#SMILESVec

awk "BEGIN { print \"Computing similarity list..!!\" }"
python lingosmi.py $LRNDRUGLINGO8 $PAIRList $SMILESFILE "wd" "l" $ldrugLen  $INTERACTIONFILE $SMICHOICE #MODEL AVG

$SHELL