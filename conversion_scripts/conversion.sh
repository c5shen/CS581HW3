#!/bin/bash

# 1000M1 conversion
prefix1=$(pwd)/1000M1/1000M1/R
rep=19
for i in $(seq 0 $rep); do
        python3 convert_fasta_to_phy.py $prefix1$i/rose.aln.true.fasta
done


# 1000M4 conversion
prefix2=$(pwd)/1000M4/1000M4/R
for i in $(seq 0 $rep); do
        python3 convert_fasta_to_phy.py $prefix2$i/rose.aln.true.fasta
done

