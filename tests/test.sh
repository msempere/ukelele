#!/bin/bash

compiler=../ukelele
ilasm=ilasm
mono=mono

for j in *.uk
    do
        n=$(basename $j .uk)
        rm -rf $n.ukil $n.exe $n.tmp $n.err.tmp
        touch $n.tmp $err.tmp
        $compiler $j 2> $n.err.tmp
        if [ $? -eq 0 ]
            then
                $ilasm $n.ukil 1>/dev/null
                $mono $n.exe > $n.tmp
        fi
        diff -b -B --brief $n.out $n.tmp
        if [ $? -eq 0 ]
            then
                diff -b -B --brief $n.err $n.err.tmp
                if [ $? -eq 0 ]
                    then
                        echo "$n: PASSED";
                    else
                        echo "$n: FAILED"
                fi
        fi
    done
