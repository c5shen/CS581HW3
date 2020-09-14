from Bio import SeqIO
import sys

input = sys.argv[1]
output = '.'.join(input.split('.')[:-1]) + ".phylip"
records = SeqIO.parse(input, "fasta")
count = SeqIO.write(records, output, "phylip")
print("Converted %i records" % count)
