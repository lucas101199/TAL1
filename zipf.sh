#!/bin/bash

file=$1

sed 's/[ \t]/\n/g' $file | sort | uniq -c | sort -t " " -n -r >> zipf.data
