from dendropy.datamodel.treemodel import Tree
import dendropy
import sys, os
from dendropy.calculate import treecompare
tns = dendropy.TaxonNamespace()
distance_methods = ['p-distance','K2P','JC69']
dataset = ['1000M1', '1000M4'] 

for data in dataset:
    result_file = open('result_{}_nj.txt'.format(data), 'w')
    for method in distance_methods:
            result_file.write(method + '\n')
            for i in range(20):
                    truth = '../../{}/{}/R{}/rose.tt'.format(data, data, i)
                    predicted_tree_file = (data + '/' + method + '/R'+ str(i)
                            + '/out_tree.nwk')
                    if (not os.path.isfile(predicted_tree_file) or 
                            os.stat(predicted_tree_file).st_size == 0):
                        result_file.write('R'+str(i)+'(-,-)')
                        continue
                    true_tree_file = (truth)

                    tree1 = Tree.get_from_path(
                            predicted_tree_file,
                            "newick",
                            taxon_namespace=tns)
                    tree2 = Tree.get_from_path(
                            true_tree_file,
                            "newick",
                            taxon_namespace=tns)

                    tree1.encode_bipartitions()
                    tree2.encode_bipartitions()

                    print('R'+str(i),treecompare.false_positives_and_negatives(tree1, tree2))
                    result_file.write('R'+str(i)+str(treecompare.false_positives_and_negatives(tree1, tree2)))
            result_file.write('\n')

    result_file.close()
