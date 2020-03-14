import sys
sys.path.extend(['D:\\Misaki\\venv\\Lib\\site-packages'])
import re
import xlwt

f = open("new.xml", "r", encoding='utf-8')
content = f.read()
f.close()

book = xlwt.Workbook()
sheet1 = book.add_sheet("hi", cell_overwrite_ok=True)
tall_style = xlwt.easyxf("font:height 400")
title = ["姓名", "年龄"]
for i in title:
    sheet1.write(0, title.index(i), i)

channelList = re.findall("<PathDetail.*?</PathDetail>", content, re.S)

for j in channelList:
    pname = re.findall("<name>(.*?)</name>", j, re.S)[0]
    channel = re.findall("<age>(.*?)</age>", j, re.S)[0]
    sheet1.write(channelList.index(j)+1, 0, pname)
    sheet1.write(channelList.index(j)+1, 1, channel)

col0 = sheet1.col(0)
col1 = sheet1.col(1)
row0 = sheet1.row(0)
col0.width = 256*30
col1.width = 256*20
row0.set_style(tall_style)

book.save("channel_id.xls")


