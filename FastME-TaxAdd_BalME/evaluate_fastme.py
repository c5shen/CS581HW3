# evaluate the result, get false positive rate and false negative rate


from dendropy.datamodel.treemodel import Tree
import dendropy
from dendropy.calculate import treecompare
tns = dendropy.TaxonNamespace()
result_file = open('result_fastme.txt','w')
distance_methods = ['p-distance','LogDet','JC69']
for method in distance_methods:
        result_file.write(method+'\n')
        for i in range(20):
                predicted_tree_file = 'results/FastME/SaTe-1000M1/'+method+'/R'+str(i)+'/out_tree.nwk'
                true_tree_file = 'SaTe-1000M1/1000M1/data/R'+str(i)+'/rose.tt'

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