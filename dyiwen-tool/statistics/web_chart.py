# -*- coding: utf-8 -*-
from gpcharts import figure
from pyecharts import Bar, Page, Style
# my_plot = figure(title='Demo')
# my_plot.plot([1,2,10,15,12,23])
#-------------------------------------------------------------------------------
# fig3 = figure()
# xVals = ['Temps','2016-03-20','2016-03-21']
# yVals = [['十堰太和医院','山西心研所','南昌大学第一附属医院'],[10,30,40],[12,28,41]]
# fig3.title = '前置机数据统计'
# fig3.ylabel = '日期'
# fig3.bar(xVals, yVals)
#--------------------------------------------------------------------------------
'''
attr = ['十堰太和医院','山西心研所','南昌大学第一附属医院']
v1 = [35,10]
v2 = [10,1]
v3 = [29,1]
bar = Bar('柱状图数据堆叠示例')
bar.add("十堰太和医院", attr, v1, is_stack=False, is_label_show=True)
bar.add("山西心研所", attr, v2, is_stack=True, is_label_show=True)
bar.add("南昌大学第一附属医院", attr, v3, is_stack=True, is_label_show=True)
bar.show_config()
# bar.render(path="C:\\Users\\dyiwen\\Desktop\\dyiwen-tool\\statistics\\1.png")
bar.render()
'''
#---------------------------------------------------------------------------------
page = Page()
style = Style(width = 900, height =400)
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [5, 20, 36, 10, 75, 90]
# v2 = [10, 25, 8, 60, 20, 80]
# chart = Bar("柱状图-数据堆叠", **style.init_style)
# chart.add("商家A", attr, v1, is_stack=True)
# chart.add("商家B", attr, v2, is_stack=True, is_more_utils=True)
# page.add(chart)

# chart = Bar("柱状图-数据标记", **style.init_style)
# chart.add("商家A", attr, v1, mark_point=["average"])
# chart.add("商家B", attr, v2, mark_line=["min", "max"], is_more_utils=True)
# page.add(chart)

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
      135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
      175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
	  175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
chart = Bar("柱状图-数据缩放(slider)", **style.init_style)
chart.add("十堰太和医院", attr, v1, mark_line=["average"],
          mark_point=["max", "min"])
chart.add("山西心研所", attr, v2, mark_line=["average"],
          mark_point=["max", "min"],
          is_datazoom_show=True, datazoom_range=[50, 80])
chart.add("南昌大学第一附属医院", attr, v3, mark_line=["average"],
          mark_point=["max", "min"],
          is_datazoom_show=True, datazoom_range=[60, 80])
page.add(chart)




page.render()