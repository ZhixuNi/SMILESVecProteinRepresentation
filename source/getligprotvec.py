import os, sys, pickle, json
from chembl_webresource_client.new_client import new_client
from getsmilesvec import *


mapfile = "utils/chembl_uniprot_mapping.txt"
proteins_path = "utils/prots_sample.txt"
emb_path = "utils/" + sys.argv[1]


class PLI:
	def __init__(self, uniprot_, chembl_, ligands_):
		self.uniprotid = uniprot_
		self.chemblid = chembl_
		self.ligands = ligands_

def load_uniprot2chembl(file):
	return {line.split()[0]:line.split()[1].strip() for line in open(file)}

uniprot2ChemblDict = load_uniprot2chembl(mapfile)


def getChEMBLID(prot):
	chmblid = ""

	if prot in uniprot2ChemblDict.keys():
		return uniprot2ChemblDict[prot]
	else:
		return "none"

	return chmblid

def activity_parser(activities):
	compounds = {}

	for activity in activities:
		cid = activity["molecule_chembl_id"]
		canon_smi = activity["canonical_smiles"]
		#activityval = activity["standard_value"]
		#if activityval < 10000:
		if canon_smi is not None:
		  compounds[cid] = canon_smi
	return compounds




def getLigandInteractions(proteins_path):
	proteins = [line.strip() for line in open(proteins_path)]
	print("Constructing protein vectors..")
	protlist = []	
	for prot in proteins:
		chmblid = prot

		if "CHEMBL" not in prot:
			chmblid = getChEMBLID(prot)
			print("Fetching interactions for", prot, chmblid)

		if chmblid is not "none":
			activities = new_client.activity.filter(target_chembl_id=chmblid) #resjson = s.get_target_bioactivities(chemblid)
			compounds = activity_parser(activities)
			#print(compounds)
			protx = PLI(prot, chmblid, compounds)
			protlist.append(protx)
		else:
			protlist.append("none")

	pickle.dump(protlist, open("pl.interactions",'wb'))


	return protlist

smilesEMB, vsize = loadEmbeddings(emb_path)

def getProteinVec(proteins_path):
	PLIlist = getLigandInteractions(proteins_path)
	proteinVectors = []

	for pli in PLIlist:
		if pli is not "none":
			sumVec = [float(0) for i in range(100)]
			protein = pli.uniprotid
			ligands = pli.ligands

			for ligand, smi in ligands.iteritems():
				#print(smi)
				ligVec = getSMIVector(smilesEMB, smi) #q, wordOrChar
				sumVec = [sumVec[i]+ligVec[i] for i in range(len(ligVec))]

			sumVec = [sumVec[i]/len(ligands) for i in range(len(sumVec))]
			proteinVectors.append(sumVec)
		else:
			proteinVectors.append("none")
	pickle.dump(proteinVectors, open("protein.vec",'wb')) 
	print("Done.")


if __name__=="__main__":
    getProteinVec(proteins_path)
    #a = pickle.load(open("output.vec"))
    #print(a)
