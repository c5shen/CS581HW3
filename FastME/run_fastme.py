
# run FastME
# convert all input to phylip format


from Bio import SeqIO
import os

for i in range(20):
    inname = 'SaTe-1000M1/1000M1/data/'+'R'+str(i)+'/rose.aln.true.fasta'
    if not os.path.isdir('SaTe-1000M1-phylip/'+'R'+str(i)):
        os.mkdir('SaTe-1000M1-phylip/'+'R'+str(i))
    out_phy_name = 'SaTe-1000M1-phylip/'+'R'+str(i)+'/rose.aln.true.phy'
    # if not os.path.isfile(out_phy_name):
    SeqIO.write(SeqIO.parse(inname, "fasta"), out_phy_name, "phylip")
    
    distance_methods = ['p-distance','LogDet','JC69']

    for method in distance_methods:
        outname = 'results/FastME/SaTe-1000M1/'+method+'/R'+str(i)
        if not os.path.isdir(outname):
            os.mkdir(outname)
        print("running FastME on 1000M1 dataset on R"+str(i))
        command = 'fastme -i '+out_phy_name+' -o '+outname+'/out_tree.nwk'+' -d '+method + ' -O '+outname+'/out_matrix.txt'
        print("execute command ", command)
        os.system(command)


