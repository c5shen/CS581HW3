

from Bio import SeqIO

input = '/Users/workplace/Desktop/workplace/cs581/hw3/new_1000_m1_dataset/1000M1/data/R0/rose.aln.true.internal.fasta'
output = 'output_internal'
records = SeqIO.parse(input, "fasta")
count = SeqIO.write(records, output, "phylip")
print("Converted %i records" % count)

