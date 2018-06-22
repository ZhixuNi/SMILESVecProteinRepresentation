from wordextract import *
from cmethods import *
import sys

emb_file = sys.argv[1]
smiles = sys.argv[2]



def loadEmbeddings(LRNPATH):
    embeddings_index = {}

    f = open(os.path.join("data/"+LRNPATH)) #'word.11l.100d.txt'
    next(f)
    vsize = 0
    for line in f:
        values = line.split()
        word = values[0]
        vsize = len(values)-1
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()

    return embeddings_index, vsize

EMB, vsize = loadEmbeddings(emb_file)


def getSMIVector(LINGOembds, smiles, q, wordOrChar):


    lingoList = []
    if wordOrChar == "wd":
        lingoList = createLINGOs(smiles, q)
    #elif wordOrChar == "ch":
    #    lingoList = createCHRs(smiles, "l") #ligand, q=1

    smilesVec = vectorAddAvg(LINGOembds, lingoList)
    print(smilesVec)
    return smilesVec


getSMIVector(EMB, smiles, 8, "wd")