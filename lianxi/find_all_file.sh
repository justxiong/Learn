#!/bin/bash


src=$1
src_dir=$(cd `dirname $1`; pwd)
src_file=${src##*/}

echo $src_file

function get_dir_file(){
    for i in $(ls $1)
    do
        if [ -f $1/$i ];then
            echo $i
            #sed -i 's/app/APP/g' $1/$i
        else
            get_dir_file $1/$i
        fi
    done
}

if [[ -f $src_dir/$src_file ]];then
    echo $1
else
    get_dir_file $src_dir/$src_file
fi
