#!/bin/bash

grep -r "define" app/include/app_config.h | sed 's/[ ]\+/ /g' >1
#cfg_list=$(awk '{if(NF>=3){print $2,$3}else{print $2,"0"}}' 1)

declare -A def_cfg
while read line
do
    k=`echo $line |cut -f2 -d" "`
    v=`echo $line |cut -f3 -d" "`
    if [ ! $v ];then
        def_cfg[$k]="0"
    else
        def_cfg[$k]=$v
    fi
done<1

#for v in ${def_cfg[@]}
#do
#    echo $v
#done

begin=false
count=0
del_word=()
while read line
do
    if [[ $line =~ "#if" ]];then
        key=`echo $line | cut -f2 -d "("| cut -f1 -d">"|cut -f1 -d" "`
        if [[ ${def_cfg[$key]} == "0" ]];then
            begin=true
        fi
    elif [[ $line =~ "#define" && $begin == true ]];then
        #echo $line
        if [[ $line =~ "/" ]];then
            echo $line
        else
           del_word[count]=`echo $line |cut -f2 -d"\""`
           #echo $line | cut -f2 -d "\""
           echo ${del_word[$count]}
           let count++
       fi
    elif [[ $line =~ "#endif" ]];then
        begin=false
    fi
done<app/include/app_str_id.h
echo $count
for i in ${del_word[@]}
do
    echo $i
    sed "/$i/d" -i output/theme/language/English.xml
done
