#!/bin/bash

declare -A words

#words['the']=$1

while IFS= read -r line; do
    for word in $line; do 
        #echo $word
        if [ ${words[$word]+abc} ]; then
            words[$word]=$((words[$word]+1))
        else
            words[$word]=$((1))
        fi
    done
done < words.txt

for k in "${!words[@]}"; do
  echo $k ${words["$k"]}
done | sort -nr -k 2