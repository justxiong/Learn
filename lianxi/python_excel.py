import xlrd
import xlwt
from xlutils.copy import copy


def sort_i18n_xls(theme):
    global xls_id_sorted_list

#excel文件读
    wd=xlrd.open_workbook(theme + '/language/i18n.xls')
    #sheet_count = wd.sheets()
    sheet=wd.sheets()[0]
    #sheet_name = sheet.name
    nrow=sheet.nrows
    ncol=sheet.ncols
    org_xls_id_list=[]
    for row in range(2,nrow):
        xls_id = sheet.cell(row,0).value.encode('utf-8')
        if xls_id != "":
            org_xls_id_list.append(xls_id)
    xls_id_sorted_list=sorted(org_xls_id_list)

#excel文件写
    temp_xls=xlwt.Workbook()
    sort_sheet=temp_xls.add_sheet("Sort_list")
    for r in range(0,2):
        for c in range(0,ncol):
            word=sheet.cell(r,c).value
            sort_sheet.write(r,c,word)
    temp_xls.save('./xls_id_sorted.xls')

#向已存在sheet中写数据
def write_into_xls(path):
    rb=xlrd.open_workbook(path,formatting_info=True)
    wb=copy(rb)
    sheet=wb.get_sheet(n)
    nrows=len(sheet.rows)
    ncols=len(sheet.ncols)
    for c in range(0,len(results)):
        sheet.write(nrows, c, results[c])
    wb.save(path)

#
