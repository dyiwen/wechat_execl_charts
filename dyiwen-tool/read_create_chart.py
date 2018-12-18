# -*- coding: utf-8 -*-
from pyecharts import Bar, Page, Style
import xlrd
import xlwt
import re


def re_job(xx,source):
	rex = re.compile(xx)
	result = rex.findall(source)
	return result
def read_execl():
	index_list = [u'十堰太和医院',u'山西心研所',u'南京大学第一附属医院']
	readbook = xlrd.open_workbook(u'C:\\Users\\dyiwen\\Desktop\\dyiwen-tool\\前置机数据统计.xls')

	sheet = readbook.sheet_by_name(index_list[0])
	nrows = sheet.nrows #行
	# ncols = sheet.ncols #列
	# print ncols
	# col = 4
	# lng = sheet.cell(1,3).value
	# print lng
	total_list = []
	for index_ in index_list:
		sheet = readbook.sheet_by_name(index_)
		value_list = []
		date_list = []
		for i in range(sheet.nrows):
			if i <> 0:
				cell_value = sheet.cell(i,3).value
				date_value = sheet.cell(i,1).value
				result = re_job(r'(\d+)',cell_value)[:-3]
				value_list.append(int(result[0]))
				date_result = re_job(r'(\d+-\d+-\d+)',date_value)[0]
				date_list.append(date_result)
				# print '-'*50
		value_list.append(index_)
		value_list.append(date_list)
		# print value_list
		# print value_list[:-1]
		total_list.append(value_list)
	print total_list
	return total_list



def create_chart_1(list_):
	'''chart.add("十堰太和医院", attr, v1, mark_line=["average"],
          mark_point=["max", "min"])'''
	page = Page()
	style = Style(width = 534, height =227)
	attr = ["{}".format(i) for i in list_[0][3]]
	chart = Bar("病首数据", **style.init_style)
	# print len(list_[0])-1
	for i in list_:
		chart.add(i[-2], attr, i[:-2], mark_line=["average"],
          mark_point=["max", "min"],is_datazoom_show=True, datazoom_range=[50, 80])
	chart.render(path="C:\\Users\\dyiwen\\Desktop\\dyiwen-tool\\statistics\\2.png")
	page.add(chart)
	page.render()

def create_chart_2(list_):
	page = Page()
	style = Style(width = 1068, height =445)
	attr = ["{}".format(i) for i in list_[0][3]]
	attr = ['2018-12-17', '2018-12-18']
	chart = Bar("病首数据", **style.init_style)
	# print len(list_[0])-1

	for i in list_:
		chart.add(i[-2], attr, i[:-2], mark_line=["average"],
          mark_point=["max", "min"],is_datazoom_show=True, datazoom_range=[10, 60])
	chart.render(path="C:\\Users\\dyiwen\\Desktop\\dyiwen-tool\\statistics\\2.png")
	page.add(chart)
	page.render()

if __name__ == '__main__':
	list_ = read_execl()
	# print list_
	create_chart_2(list_)