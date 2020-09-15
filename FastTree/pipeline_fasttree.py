from Bio import SeqIO
import subprocess
import os, shutil
import pexpect

targets = ['1000M1', '1000M4']
binary = '../../FastTree/FastTreeMP'
for target in targets:
    for i in range(20):
        inname = '../../'+target+'/'+target+'/R'+str(i)+'/rose.aln.true.phylip'
        init_tree = '../../'+target+'/'+target+'/R'+str(i)+'/random.tree'

        models = ['GTR', 'JC']

        for method in models:
            if not os.path.isdir(target):
                os.mkdir(target)
            if not os.path.isdir(target+'/'+method):
                os.mkdir(target+'/'+method)

            outname = target+'/'+method+'/R'+str(i)
            if not os.path.isdir(outname):
                os.mkdir(outname)
            print("running FastTree on {} dataset on R{}, method {}".format(
                target, str(i), method))

            if method == 'GTR':
                m = '-gtr'
            else:
                m = ''

            command = binary + ' -nt -gamma {} '.format(m) + inname + ' > ' + outname + '/out_tree.nwk'
            os.system(command)
