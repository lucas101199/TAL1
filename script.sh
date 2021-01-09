#!/bin/bash

file=$1

for i in 100 500 1000 1500 2000 4000 5000 10000 20000 30000 40000 50000 80000 100000 200000 500000 1000000 2000000 5000000
do 
	echo -n $i' ' >> plot.txt
	sed 's/[ \t]/\n/g' $file | head -n $i | sort -u | uniq -c | wc -l >> orfeo.data
done
