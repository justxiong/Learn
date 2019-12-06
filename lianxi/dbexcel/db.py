#!/usr/bin/env python
# coding=utf-8

import xlrd
import xlwt
import sqlite3
import sys
import argparse

def excel2db():
    conn=sqlite3.connect('language.db')
    cursor=conn.cursor()
    try:
        cursor.execute('create table lang(id varchar(100) primary key,arabic varchar(100),farsi varchar(100),french varchar(100),spain varchar(100))')
    except sqlite3.OperationalError as e:
        cursor.execute('drop table lang')
        cursor.execute('create table lang(id varchar(100) primary key,arabic varchar(100),farsi varchar(100),french varchar(100),spain varchar(100))')
    wd=xlrd.open_workbook('./i18n.xls')
    sheet=wd.sheets()[0]
    nrow=sheet.nrows
    ncol=sheet.ncols
    for row in range(2,nrow):
        value=[]
        for col in range(0,5):
            value.append(sheet.cell(row,col).value.encode('utf-8'))
        print('insert {v1}'.format(v1=value))
        cursor.execute('insert into lang(id,arabic,farsi,french,spain) values(?,?,?,?,?)',(value[0],value[1],value[2],value[3],value[4]))

    #print('insert {v1} rows'.format(v1=cursor.rowcount))
    cursor.close()
    conn.commit()
    conn.close()

def db2excel():
    conn=sqlite3.connect('language.db')
    cursor=conn.cursor()
    cursor.execute('select * from lang')
    values=cursor.fetchall()

    xls=xlwt.Workbook()
    lang=xls.add_sheet("lang")
    for i in range(len(values)):
        for j in range(len(values[i])):
            #print(values[i][j])
            lang.write(i,j,str(values[i][j],'utf-8'))
    xls.save('./lang.xls')

    cursor.close()
    conn.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test db2excel or excel2db')
    parser.add_argument('mode', help='db2excel or excel2db')
    args = parser.parse_args()
    if args.mode =='db2excel':
        db2excel()
    elif args.mode =='excel2db':
        excel2db()
    else:
        print('eg: python3 db.py db2excel')
        print('eg: python3 db.py excel2db')
        print('for more python3 db.py --help')
