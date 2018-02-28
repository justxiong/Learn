#!/usr/bin/env python
# coding=utf-8
import requests
import json
import sys
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36','Cookie': 'GerritAccount=aPGbfjC14GTYBZvC7VT703NnLg4HWt0R'}

#commit='bd1f162f6ca6b7c7d0ed94b4ccd7e1aa53343076'
commit=sys.argv[1]
url1='http://git.nationalchip.com/gerrit/changes/?q='+commit
#data = requests.get('http://git.nationalchip.com/gerrit/changes/37535/revisions/bd1f162f6ca6b7c7d0ed94b4ccd7e1aa53343076/files', headers=headers).text
res1=requests.get(url1, headers=headers)
code_review_id= json.loads(res1.text[5:])[0]['_number']
#print code_review_id
res=requests.get('http://git.nationalchip.com/gerrit/changes/'+str(code_review_id)+'/detail?O=10004', headers=headers)
#res=requests.get('http://git.nationalchip.com/gerrit/#/c/37583/');
#print res.text[5:]
issue_msg=json.loads(res.text[5:])
commit_msg_key=issue_msg['current_revision']
#print commit_msg_key
url='http://git.nationalchip.com/gerrit/changes/'+str(code_review_id)+'/revisions/'+commit_msg_key+'/files'
#print url
res_msg=requests.get(url, headers=headers)
#print res_msg.text[5:]
commit_msg=json.loads(res_msg.text[5:])
commit_msg.pop('/COMMIT_MSG')

gerrit_info=''
if len(commit_msg):
    for fil,info in commit_msg.items():
        gerrit_info+='      '
        gerrit_info+=fil
        if info.has_key('lines_inserted'):
            #print info['lines_inserted']
            gerrit_info+=('    ++'+str(info['lines_inserted']))

        if info.has_key('lines_deleted'):
            #print info['lines_deleted']
            gerrit_info+=('    --'+str(info['lines_deleted']))

        gerrit_info+='\n'

print gerrit_info




