from Bio import SeqIO
import subprocess
import os, shutil
import pexpect

targets = ['1000M1']
for target in targets:
    for i in range(20):
        inname = '../../'+target+'/'+target+'/R'+str(i)+'/rose.aln.true.phylip'
        init_tree = '../../'+target+'/'+target+'/R'+str(i)+'/random.tree'

        distance_methods = ['K2P']
        #distance_methods = ['LogDet']

        for method in distance_methods:
            if not os.path.isdir(target+'/'+method):
                os.mkdir(target+'/'+method)
            outname = target+'/'+method+'/R'+str(i)
            if not os.path.isdir(outname):
                os.mkdir(outname)
            print("running FastME NJ on {} dataset on R{}, method {}".format(
                target, str(i), method))
            
            if method == 'p-distance':
                m = 'P'
            elif method == 'K2P':
                m = 'K'
            else:
                m = 'J'

            child = pexpect.spawn('fastme')
            #child.expect('Enter your input data file name > ')
            child.sendline(inname)
            #child.expect('Are these settings correct? (type  Y  or letter for one to change)  ')
            child.sendline('I')
            #child.expect('Choose your input data type: distance (M)atrix, (D)NA alignment, (P)rotein alignment > ')
            child.sendline('D')
            child.sendline('E')
            child.sendline(m)
            child.sendline('M')
            child.sendline('N')
            child.sendline('Y')
            child.interact()  

            shutil.move(inname+'_fastme_tree.txt', outname+'/out_tree.nwk')
            shutil.move(inname+'_fastme_stat.txt', outname+'/out_tree.stat')
            # command = 'fastme -i '+out_phy_name+' -o '+outname+'/out_tree.nwk'+' -d '+method + ' -O '+outname+'/out_matrix.txt  -s -m BalME'
            # os.system(command)
