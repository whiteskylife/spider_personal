#!/usr/bin/env python
# -*-coding:utf-8 -*-
#
# a = [1, 2]
# b = 'Immutable'
# def test():
#     # global b
#     print(a)
#     a.append('asd')
#     b = b + 'asd'
#     def test2():
#         print(a)
#         print(b)
#     test2()
#
# test()
# # 在python3中，若在局部中有改变不可变类型的全局变量的值的操作，无论先后顺序，
# # 系统会默认为将该变量作为局部变量，不会再去全局寻找该变量的值，因此如上的代码，会报错：
# # 解决办法是使用global将该变量变为全局变量。  在局部中增，删，改可变类型的全局变量的元素，不存在这个问题
#
# a = '''
# <div class="header">
#     <div class="logo"><a href="/"><img width="180" height="60" src="//www.sogou.com/images/logo2014/error180x60.png"></a></div>
#     <div class="other"><span class="s1">您的访问出错了</span><span class="s2"><a href="/">返回首页&gt;&gt;</a></span></div>
# </div>
#
# '''
# from pyquery import PyQuery as pq
#
# doc = pq(a)
# b = doc('.header .other .s1').text()
# if b == '您的访问出错了':
#     print('asdasdasd')

# a = '''
#         } else {
#             var u = navigator.userAgent;
#             var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1;
#             var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
#             if (isAndroid) {
#                 window.alert(getString(0));
#                 window.location.href = "http://m.sohu.com/" + Math.random().toString().substring(2, 10) + ".apk"
#             }
#
#             function isPC() {
#                 var userAgentInfo = navigator.userAgent;
#                 var Agents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
#                 var flag = true;
#                 for (var v = 0; v < Agents.length; v++) {
#             '''
# import re
# pattern = re.compile('window.location.href\s=\s"(.*?)".*?apk"', re.S)
# ret = re.search(pattern, a).group()
# print(ret)
# if ret == 'http://m.sohu.com/':
#     print('asdasdasdasdaaaaaaaaa')


# import pytesseract
# from PIL.Image import Image
#
#
# img = Image.convert(mode="L")
# threshold = 80
# table = []
#
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# img = img.point(table, '1')
# img.show()

# img = Image.open('seccode.jpg')
# # img = Image.open('getAuthCode.jpg')
# code = pytesseract.image_to_string(img)
# print(code)
#



# import tesserocr
# from PIL import Image
#
# image = Image.open('getAuthCode.jpg')
#
# image = image.convert('L')
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# image = image.point(table, '1')
# # image.show()
#
# result = tesserocr.image_to_text(image)
# print(result)

# from PIL import Image
# import tesserocr
# p1 = Image.open('getAuthCode.jpg')
#
# threshold = 127
#
# def binarizing(img,threshold):
#     """传入image对象进行灰度、二值处理"""
#     img = p1.convert("L")  # 转灰度
#     pixdata = img.load()
#     w, h = img.size
#     threshold = 127
#
#     for y in range(h):
#         for x in range(w):
#             if pixdata[x, y] < threshold:
#                 pixdata[x, y] = 0
#             else:
#                 pixdata[x, y] = 255
#     return img
#
#
#
# def depoint(img):
#     '''传入二值化后的图片进行降噪'''
#     pixdata = img.load()
#     w,h = img.size
#     for y in range(1,h-1):
#         for x in range(1,w-1):
#             count = 0
#             if pixdata[x,y-1] > 245:#上
#                 count = count + 1
#             if pixdata[x,y+1] > 245:#下
#                 count = count + 1
#             if pixdata[x-1,y] > 245:#左
#                 count = count + 1
#             if pixdata[x+1,y] > 245:#右
#                 count = count + 1
#             if pixdata[x-1,y-1] > 245:#左上
#                 count = count + 1
#             if pixdata[x-1,y+1] > 245:#左下
#                 count = count + 1
#             if pixdata[x+1,y-1] > 245:#右上
#                 count = count + 1
#             if pixdata[x+1,y+1] > 245:#右下
#                 count = count + 1
#             if count > 4:
#                 pixdata[x,y] = 255
#     return img
#
#
# img = binarizing(p1, threshold)
#
# img = depoint(img) # 可以多次降噪
# # img = depoint(img)
# # img = depoint(img)
# img = depoint(img)
#
# img.show()
# ret = tesserocr.image_to_text(img)
# print(ret)
#
# # https://m.aliyun.com/jiaocheng/516832.html

# a = '''
#     var first_js_time = +new Date();
#     console&&console.log("first js excute:"+(first_js_time-write_sceen_time));
#     var showDate="";
#     var svrDate=new Date("1528004135"*1000);
#     var createDate=new Date("1527998431"*1000);
#     var ct="1527998431"*1;
#     var publish_time = "2018-06-03" || "";
#     var cD={
#       year:createDate.getYear(),
#       month:createDate.getMonth()+1,
#       date:createDate.getDate()
#     };
# '''
# import re
# pattern = re.compile('var.publish_time.=."(.*?)".\|\|', re.S)
# ret = re.search(pattern, a).group(1)
# # ret = re.findall(pattern, a)[0]
# print(ret)



import tesserocr
from PIL import Image
# image = Image.open('getAuthCode.jpg')
image = Image.open('222.jpg')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)






# from PIL import Image
# import tesserocr
# p1 = Image.open('222.jpg')
#
# threshold = 127
#
# def binarizing(img,threshold):
#     """传入image对象进行灰度、二值处理"""
#     img = p1.convert("L")  # 转灰度
#     pixdata = img.load()
#     w, h = img.size
#     threshold = 127
#
#     for y in range(h):
#         for x in range(w):
#             if pixdata[x, y] < threshold:
#                 pixdata[x, y] = 0
#             else:
#                 pixdata[x, y] = 255
#     return img
#
#
#
# def depoint(img):
#     '''传入二值化后的图片进行降噪'''
#     pixdata = img.load()
#     w,h = img.size
#     for y in range(1,h-1):
#         for x in range(1,w-1):
#             count = 0
#             if pixdata[x,y-1] > 245:#上
#                 count = count + 1
#             if pixdata[x,y+1] > 245:#下
#                 count = count + 1
#             if pixdata[x-1,y] > 245:#左
#                 count = count + 1
#             if pixdata[x+1,y] > 245:#右
#                 count = count + 1
#             if pixdata[x-1,y-1] > 245:#左上
#                 count = count + 1
#             if pixdata[x-1,y+1] > 245:#左下
#                 count = count + 1
#             if pixdata[x+1,y-1] > 245:#右上
#                 count = count + 1
#             if pixdata[x+1,y+1] > 245:#右下
#                 count = count + 1
#             if count > 4:
#                 pixdata[x,y] = 255
#     return img
#
#
# img = binarizing(p1, threshold)
#
# img = depoint(img) # 可以多次降噪
# # img = depoint(img)
# # img = depoint(img)
# img = depoint(img)
#
# # img.show()
# ret = tesserocr.image_to_text(img)
# print(ret)










