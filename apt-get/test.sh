#! /bin/bash

#List

array=($(cat ./apps.txt))
echo ${array[*]}

echo "Numero de itens no array: "${#array[@]}

#looping through list

echo "loop 1"

for i in $(cat ./apps.txt)
    do
        echo "$i"
    done

echo "loop 2"

for i in $(echo ${array[*]})
    do
        echo "$i"
    done

echo "loop 3"
arrLength=${#array[@]}
arrLength=$[$arrLength+0]
for i in {1..$arrLength}
    do
        echo "$i"
    done
int=1
echo $[$int+$int]

echo "loop 4"
counter=0
for i in $(echo ${array[*]})
    do
       counter=$[$counter+1]
    done
echo $counter