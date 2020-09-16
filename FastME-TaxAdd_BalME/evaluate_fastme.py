from dendropy.datamodel.treemodel import Tree
import dendropy
import sys
from dendropy.calculate import treecompare
tns = dendropy.TaxonNamespace()
distance_methods = ['p-distance','JC69','K2P']
dataset = ['1000M1', '1000M4'] 

for data in dataset:
    result_file = open('result_{}_fastme_taxadd.txt'.format(data), 'w')
    for method in distance_methods:
            result_file.write(method + '\n')
            effective_samples = 0
            agg_false_positives = 0
            agg_false_negatives = 0
            for i in range(20):
                    truth = '{}/{}/data/R{}/rose.tt'.format(data, data, i)
                #     print(truth)
                    predicted_tree_file = (data + '/' + method + '/R'+ str(i)
                            + '/out_tree.nwk')
                    true_tree_file = (truth)
                    try:
                     
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
                        print("try")
                        print('R'+str(i),treecompare.false_positives_and_negatives(tree1, tree2))
                        effective_samples = effective_samples+1
                        agg_false_positives = agg_false_negatives+treecompare.false_positives_and_negatives(tree1, tree2)[0]
                        agg_false_negatives = agg_false_negatives+treecompare.false_positives_and_negatives(tree1, tree2)[1]
                        result_file.write('R'+str(i)+str(treecompare.false_positives_and_negatives(tree1, tree2)))
                    except Exception as e:
                        print("exception")
                        print(e)
                        result_file.write('R'+str(i)+"(err,err)\n")
            ave_false_positive = agg_false_positives/effective_samples
            ave_false_negative = agg_false_positives/effective_samples
            result_file.write("total effective{}, averge false positive{},average false negative{}".format(effective_samples,ave_false_positive,ave_false_negative))   
            result_file.write('\n')

    result_file.close()