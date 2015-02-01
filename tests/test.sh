#!/bin/bash

compiler=../ukelele
ilasm=ilasm
mono=mono

for j in *.uk
    do
        $compiler $j
        n=$(basename $j .uk)
        $ilasm $n.ukil 1>/dev/null
        $mono $n.exe > $n.tmp
        diff -b -B --brief $n.out $n.tmp
        if [ $? -eq 0 ]
            then
                echo "$n: PASSED";
        else
            echo "$n: FAILED"
        fi
    done
