#!/bin/bash

if [[ $# -ne 2 && $# -ne 3 ]]; then
    echo -e "\033[1;31mExample: ./gitDifferentBranches.sh branch1 branch2\033[0m"
    echo
    git branch -r
    echo
    echo -e "\033[1;33m'./gitDifferentBranches.sh test dev' That will show you commits that dev has but test doesn't.\033[0m"
    exit 1
fi
remote=`git remote -v | awk '{print $1}' | sed -n '1p'`
echo -e "\033[1;33m remoter is $remote \033[0m"
old_branch=$1
new_branch=$2
issue_id=0
diff=0
get_issue_info=false
commits=`git log --no-merges --oneline --pretty=tformat:"%H" $remote/$old_branch..$remote/$new_branch`

if [[ $# -eq 3 && "$3" == "getinfo" ]];then
    issue_id_num=0
    get_issue_info=false
    if [ -f "/tmp/git_issue_id.log" ];then
        rm -rf /tmp/git_issue_id.log
    fi
    for commit in $commits
    do
        issue_id=`git show --pretty=format:'%<(80,trunc)%s' $commit --no-patch |cut -f 2 -d ' '|cut -f 1 -d ':'`
        case "$issue_id" in
            [0-9]*)
                echo "$issue_id">>/tmp/git_issue_id.log
                let "issue_id_num++"
            ;;
            *)
                echo "xxxxx">>/tmp/git_issue_id.log
                #echo "      issue id is error"
            ;;
        esac
    done
    if [ $issue_id_num -gt 0 ];then
        python ./get_redmine_info.py
        if [ $? -eq 0 ];then
            get_issue_info=true
        fi
    fi
fi

for commit in $commits
do
    changeid=`git log $commit | grep "Change-Id" | awk -F ":" '{print $2}' | sed -n '1p'`
    find=`git log $remote/$old_branch --no-merges --grep="$changeid"`
    if [[ -z $find ]];then
        #issue_id=`git show --pretty=format:'%<(80,trunc)%s' $commit --no-patch |cut -f 2 -d ' '|cut -f 1 -d ':'`
        #git show --pretty=format:'%C(bold red)%h%Creset %C(bold green)%<(10,trunc)%aN%Creset %<(80,trunc)%s %C(bold yellow)(%cr)%Creset' --stat $commit --no-patch #> /tmp/git.log
        let "diff++"
        if [ $get_issue_info == true ];then
            echo "      "
            git show --pretty=format:'%C(bold red)%h%Creset %C(bold green)%<(10,trunc)%aN%Creset %<(80,trunc)%s %C(bold yellow)(%cr)%Creset' --stat $commit
            if [ -r "/tmp/git_issue_info.log" ];then
                issue_info=`sed -n "$diff"p /tmp/git_issue_info.log`
                invalid=`echo $issue_info|cut -c2-7`
                if [ "$invalid" != "NOFind" ];then
                    fre=`echo $issue_info |cut -f 2 -d ":"`
                    sev=`echo $issue_info |cut -f 4 -d ":"`
                    echo -e "   严重性 $sev 频率 $fre"
                fi
            fi
            #git show --pretty=format: --stat bd1f162f6ca6b7c7d0ed94b4ccd7e1aa53343076
            #cat /tmp/git.log
            #echo
        else
            git show --pretty=format:'%C(bold red)%h%Creset %C(bold green)%<(10,trunc)%aN%Creset %<(80,trunc)%s %C(bold yellow)(%cr)%Creset' $commit --no-patch #> /tmp/git.log
        fi
    fi
done

if [ $diff -eq 0 ];then
    hash1=`git log $remote/$old_branch -1 --pretty="%H"`
    hash2=`git log $remote/$new_branch -1 --pretty="%H"`
    if [ $hash1 = $hash2 ];then
        echo -e "\033[1;33m$old_branch and $new_branch are the same!\033[0m"
    else
        echo -e "\033[1;33m$old_branch has all commits that $new_branch has!\033[0m"
    fi
    exit 0
fi

exit 0
