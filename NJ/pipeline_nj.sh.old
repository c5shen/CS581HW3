#!/bin/bash

# number of repetitions
rep=19

# treebest NJ binary directory
#bin=$(pwd)/../../treebest

# run for 1000M1
declare -a targets=(1000M1 1000M4)
declare -a methods=(p-distance LogDet JC69)

for t in ${targets[@]}; do
        prefix=$(pwd)/../../$t/$t/R
        if [ ! -d $t ]; then
                mkdir $t
        fi

        for m in ${methods[@]}; do
                outdir=$t/$m        
                if [ ! -d $t/$m ]; then
                        mkdir $t/$m
                fi
                for i in $(seq 0 $rep); do
                        out=$outdir/R$i
                        if [ ! -d $out ]; then
                                mkdir $out
                        fi
                        if [ $m == p-distance ]; then
                                method=P
                        elif [ $m == LogDet ]; then
                                method=L
                        else
                                method=J
                        fi

                        echo -en "\rRunning for $t rep $i, method $m($method)"
                        fastme -i $prefix$i/rose.aln.true.phylip \
                                -o $out/out_tree.nwk -d $method -m N \
                                -s -n B -O $out/out_matrix.txt

                done
                echo -e ""
        done
done

# evaluate NJ method
python3 evaluate_nj.py 1000M1 $(pwd)/../../1000M1/1000M1
python3 evaluate_nj.py 1000M4 $(pwd)/../../1000M4/1000M4
