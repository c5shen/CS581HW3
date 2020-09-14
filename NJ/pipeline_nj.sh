#!/bin/bash

# number of repetitions
rep=19

# treebest NJ binary directory
bin=$(pwd)/../../treebest

# run for 1000M1
target=1000M1
if [ ! -d $target ]; then
        mkdir $target
fi
prefix1=$(pwd)/../../$target/$target/R
for i in $(seq 0 $rep); do
        echo -en "\rRunning for $target rep $i"
        if [ ! -d $target/R$i ]; then
                mkdir $target/R$i
        fi
        $bin/treebest nj $prefix1$i/rose.aln.true.phylip > $target/R$i/rose.aln.true.nhx
done
echo -e ""

# run for 1000M4
target=1000M4
if [ ! -d $target ]; then
        mkdir $target
fi
prefix2=$(pwd)/../../$target/$target/R
for i in $(seq 0 $rep); do
        echo -en "\rRunning for $target rep $i"
        if [ ! -d $target/R$i ]; then
                mkdir $target/R$i
        fi
        $bin/treebest nj $prefix2$i/rose.aln.true.phylip > $target/R$i/rose.aln.true.nhx
done
echo -e ""
