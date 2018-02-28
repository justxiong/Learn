#!/usr/bin/env python
# coding=utf-8
import threading
import thread
import time
from redminelib import Redmine
#redminelib 需自己安装
import sys
import os
import json
redmine = Redmine('http://git.nationalchip.com/redmine', key='3ab2deb0cd3668ab064c2325521719cfa9ad9d1f')
project=redmine.project.get('gx6601e')
#gx6601e是linux public,id是202
from multiprocessing import Pool
import threadpool

fid='none'
#finfo='none'
issues_id=[]
all_issues_info=[]
def get_issue_info(r):
    print r
    redmine = Redmine('http://git.nationalchip.com/redmine', key='3ab2deb0cd3668ab064c2325521719cfa9ad9d1f')
    project=redmine.project.get('gx6601e')
    issue_id=r.strip('\n')
    start = time.time()
    issue_info='none'
    try:
        issue=project.issues.get(int(issue_id))
        issue_info=issue_id+':fre:'+issue.custom_fields[0].value+':sev:'+issue.custom_fields[1].value+":"
    #issue close or other
    except AttributeError as e:
        issue_info=issue_id+":NO Find"+"\n"
    finally:
        #finfo.write(json.dumps(issue_info))
        #finfo.close()
        end = time.time()
        print issue_info
        print 'redmine get issue %s runs %0.2f seconds.' % (issue_id, (end - start))

    return issue_info

def get_issue_info_thr(r):
    global all_issues_info
    #print r
    issue_id=r.strip('\n')
    start = time.time()
    issue_info='none'
    try:
        issue=project.issues.get(int(issue_id))
        issue_info=issue_id+':fre:'+issue.custom_fields[0].value+':sev:'+issue.custom_fields[1].value+":"
    #issue close or other
    except AttributeError as e:
        issue_info=issue_id+":NO Find"+"\n"
    finally:
        #finfo.write(json.dumps(issue_info))
        #finfo.close()
        end = time.time()
        print issue_info
        print 'redmine get issue %s runs %0.2f seconds.' % (issue_id, (end - start))
        all_issues_info.append(issue_info)


def get_info_by_mut_thread():
    global fid
    global issues_id
    global all_issues_info
    all_issues_info=[]
    try:
        pool = threadpool.ThreadPool(1)
        requests = threadpool.makeRequests(get_issue_info_thr, issues_id)
        print '>>>>>>>>>>>>>>>>>>request num is %d' %(len(requests))
        print len(all_issues_info)
        for req in requests:
            pool.putRequest(req)
        pool.wait()
    except AttributeError as e:
        pass
    finally:
        print len(all_issues_info)
        for i in all_issues_info:
            print i

def get_info_by_mut_th():
    global fid
    for line in fid:
        r=line
        thread.start_new_thread(get_issue_info, (r,))

    sleep.time(100)

#all_issues_info=[]
#def mut_process_callback(x):
#    print x
#    all_issues_info.append(x)

def get_info_by_mut_process():
    all_issues_info=[]
    p=Pool(10)
    for line in fid:
        r=line
        res=p.apply_async(get_issue_info, (r,))
        all_issues_info.append(res)

    p.close()
    p.join()
    print len(all_issues_info)
    for i in all_issues_info:
        print i.get()
        finfo.write(json.dumps(i.get()))
    finfo.close()



def main():
    global fid,finfo
    print "start"
    main_start = time.time()
    fid=open('/tmp/git_issue_id.log','r')
    if os.path.isfile('/tmp/git_issue_info.log'):
        os.remove('/tmp/git_issue_info.log')
    finfo=open('/tmp/git_issue_info.log','wa+')
    for i in fid:
        issues_id.append(i)

    #mut_thread
    get_info_by_mut_thread()
    #get_info_by_mut_th()
    #mut_process
    #time.sleep(20)
    #get_info_by_mut_process()
    #no_lib

    #finfo.close()
    fid.close()
    main_end = time.time()
    print 'total issues is %d runs %0.2f seconds.' %(len(issues_id),main_end - main_start)

if __name__ == "__main__":
    main()
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
