#!/usr/bin/env python
# coding=utf-8
import time
from redminelib import Redmine
#redminelib 需自己安装
import sys
import os
import json
redmine = Redmine('http://git.nationalchip.com/redmine', key='3ab2deb0cd3668ab064c2325521719cfa9ad9d1f')
project=redmine.project.get('gx6601e')
#gx6601e是linux public,id是202

fid='none'
finfo='none'

def get_issue_info(r):
    global finfo
    issue_info='none'
    issue_id=r.strip('\n')
    #start = time.time()
    try:
        issue=project.issues.get(int(issue_id))
        issue_info='fre:'+issue.custom_fields[0].value+':sev:'+issue.custom_fields[1].value+":"
    #issue close or other
    except AttributeError as e:
        issue_info="NOFind"
    except ValueError as e:
        issue_info="NOFind"
    finally:
        finfo.write(json.dumps(issue_info)+"\n")
        end = time.time()
        #print issue_info
        #print 'redmine get issue %s runs %0.2f seconds.' % (issue_id, (end - start))

def main():
    global fid,finfo
    issue_total=0
    main_start = time.time()
    fid=open('/tmp/git_issue_id.log','r')
    if os.path.isfile('/tmp/git_issue_info.log'):
        os.remove('/tmp/git_issue_info.log')
    finfo=open('/tmp/git_issue_info.log','wa+')
    for issue_id in fid:
        get_issue_info(issue_id)
        issue_total=issue_total+1

    fid.close()
    finfo.close()
    main_end = time.time()
    #print 'total issues is %d runs %0.2f seconds.' %(issue_total, main_end - main_start)

if __name__ == "__main__":
    main()
