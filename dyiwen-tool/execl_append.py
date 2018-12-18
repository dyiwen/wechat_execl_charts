# -*- coding: utf-8 -*-
import os 
import xlrd
import xlwt
from xlutils.copy import copy

def excelwrite(L=None):
	if L is None:
		L = []
	print L
	filename = u"./前置机数据统计.xls"
	workbook = xlrd.open_workbook(filename,formatting_info = True)
	# print workbook.sheet_names()
	# for i in workbook.sheet_names():
	# 	if i == u"十堰太和医院":
	# 		print True
	sheet = workbook.sheet_by_name(u'十堰太和医院')
	print sheet
	rowNum = sheet.nrows
	print rowNum
	colNum = sheet.ncols
	print colNum
	newbook = copy(workbook)
	newsheet = newbook.get_sheet(u'十堰太和医院')
	print newsheet
	# str = 'hehe'
	# newsheet.write(rowNum, 0 ,str)
	newbook.save(filename)

def append_excel(dict):
	filename = u"./前置机数据统计.xls"
	workbook = xlrd.open_workbook(filename,formatting_info = True)
	#------------------------------------------------
	sheet = workbook.sheet_by_name(u'十堰太和医院')
	rowNum = sheet.nrows
	#------------------------------------------------
	newbook = copy(workbook)
	for key in dict.keys():
		# print dict[key]['hospital_name']
		colNum = 0
		newsheet = newbook.get_sheet(dict[key]['hospital_name'].strip())
		for item in dict[key]:
			# print item
			newsheet.write(rowNum, colNum, dict[key][item])
			colNum += 1
		newbook.save(filename)


	


if __name__ == '__main__':
	excelwrite()