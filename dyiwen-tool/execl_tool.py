# -*- coding: utf-8 -*-
import xlsxwriter
import time
import collections
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def generate_excel(rec_data):
	workbook = xlsxwriter.Workbook(u'./前置机数据统计.xlsx')

	def create_sheet(dict):
		worksheet = workbook.add_worksheet(dict['hospital_name'].strip())

		bold_format = workbook.add_format({'bold':True})
		# money_format = workbook.add_format({'num_format':'$#,##0'})
		# date_format = workbook.add_format({'num_format':'mmmm dd yyyy'})

		worksheet.write('A1','医院名称', bold_format)
		worksheet.write('B1','生成时间', bold_format)
		worksheet.write('C1','随访信息',bold_format)
		worksheet.write('D1','病案首页',bold_format)
		worksheet.write('E1','住院检查',bold_format)
		worksheet.write('F1','住院病程志',bold_format)
		worksheet.write('G1','住院检查',bold_format)
		worksheet.write('H1','住院志',bold_format)
		worksheet.write('I1','住院医嘱',bold_format)
		worksheet.write('J1','护理记录',bold_format)
		worksheet.write('K1','手术数据',bold_format)
		worksheet.write('L1','门诊检验',bold_format)
		worksheet.write('M1','病程志数据',bold_format)
		worksheet.write('N1','门诊检查',bold_format)
		worksheet.write('O1','医嘱数据',bold_format)
		worksheet.write('P1','筛查信息数据',bold_format)

		row = 1
		col = 0
		for item in dict:
			# print item
			worksheet.write_string(row, col, dict[item])
			worksheet.set_column(col,col,len(dict[item])+2)
			col += 1


	for key in rec_data.keys():
		create_sheet(rec_data[key])

	workbook.close()

if __name__ == '__main__':
	t = time.strftime("%Y-%m-%d %H:%M",time.localtime())
	rec_dict = collections.OrderedDict()
	rec_dict['hospital_name'] = u'南昌大学第一附属医院       '
	rec_dict['create_time'] = t
	rec_dict['follow_up'] = u"0条(NULL)"
	rec_dict['nursing_record'] = u"3403条(2018-12-14 23:05:08)"
	rec_dict['inpatient_check'] = u"75453条(2018-12-14 23:00:08)"
	rec_dict['home_page'] = u"75453条(2018-12-14 23:00:08)"
	rec_dict['operation_record'] = u"0条(NULL)"
	rec_dict['inpatient_disease_course_journal'] = u"6978条(2018-12-05 11:39:32)"
	rec_dict['screening'] = u"0条(NULL)"
	rec_dict['outpatient_treatment'] = u"11条(2018-12-14 23:00:11)"
	rec_dict['inpatient_examination'] = u"23980条(2018-12-14 23:00:12)"
	rec_dict['inpatient_journal'] = u"6902条(2018-12-13 23:02:30)"
	rec_dict['inpatient_treatment'] = u"507202条(2018-12-13 23:02:31)"
	rec_dict['outpatient_disease_course_journal'] = u"10条(2018-12-14 23:04:06)"
	rec_dict['outpatient_check'] = u"0条(NULL)"
	rec_dict['outpatient_examination'] = u"0条(NULL)"

	rec_data = [rec_dict]
	
	generate_excel(rec_data)
