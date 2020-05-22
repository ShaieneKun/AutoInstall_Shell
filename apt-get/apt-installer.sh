#! /bin/bash

appList=($(cat ./apps.txt)) #Obtaining apps/packages list from txt file

#Listing info about apps
apt-get update
echo -e "\nNumber of apps to install: ${#appList[@]} \n"
echo -e "Apps to install: ${appList[*]}\n"
echo -e "Apt info:\n"
apt list ${appList[*]}

#Counting number of Apps
counter=0
for i in $(echo ${appList[*]})
    do
       counter=$[$counter+1]
    done

#Installing

echo -e "\nNow installing $counter apps\n" 
apt-get install -y $(echo ${appList[*]})
 
apt-get update 


