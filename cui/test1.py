#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os
import time
from threading import Thread
from multiprocessing import Process

# def func():
#     while True:
#         time.sleep(1)
#         print('我还活着')
#
#
# def func2():
#     print('in func2 start')
#     time.sleep(8)
#     print('in func2 finished')
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True
#     p.start()
#     time.sleep(2)
#     p2 = Process(target=func2)
#     p2.start()

# import time
# from threading import Thread
#
#
# def func1():
#     while True:
#         print('*' * 10)
#         time.sleep(1)
#
#
# def func2():
#     print('in func2')
#     time.sleep(5)
#
#
# t = Thread(target=func1, )
# t.daemon = True
# t.start()
# t2 = Thread(target=func2, )
# t2.start()
# # t2.join()
# print('主线程')


# def func(lock):
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.2)
#     n = temp - 1
#     lock.release()
#
# n = 10
# t_lst = []
# lock = Lock()
# for i in range(10):
#     t = Thread(target=func,args=(lock,))
#     t.start()
#     t_lst.append(t)

# for t in  t_lst: t.join()
# print(n)
import json, re
# s = '''
# {\"count\":4,\"sub_images\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/1524670089467caf2fff4c4\",\"width\":1280,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/1524670089467caf2fff4c4\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/1524670089467caf2fff4c4\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1524670089467caf2fff4c4\"}],\"uri\":\"origin\\/pgc-image\\/1524670089467caf2fff4c4\",\"height\":1007},{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/1524670089355a07d28f775\",\"width\":1280,\"url_list\":[{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/1524670089355a07d28f775\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1524670089355a07d28f775\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/1524670089355a07d28f775\"}],\"uri\":\"origin\\/pgc-image\\/1524670089355a07d28f775\",\"height\":900},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1524670089412445c95fe1e\",\"width\":1280,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1524670089412445c95fe1e\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1524670089412445c95fe1e\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1524670089412445c95fe1e\"}],\"uri\":\"origin\\/pgc-image\\/1524670089412445c95fe1e\",\"height\":1022},{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/152467008944401ff089475\",\"width\":1280,\"url_list\":[{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/152467008944401ff089475\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/152467008944401ff089475\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/152467008944401ff089475\"}],\"uri\":\"origin\\/pgc-image\\/152467008944401ff089475\",\"height\":1151}],\"max_img_width\":1280,\"labels\":[\"\\u51b7\\u996e\",\"\\u7f8e\\u5973\",\"\\u5386\\u53f2\"],\"sub_abstracts\":[\"\\u5357\\u4eac\\u8def\\u5df2\\u6709100\\u591a\\u5e74\\u7684\\u5386\\u53f2\\uff0c\\u5b83\\u7684\\u524d\\u8eab\\u662f\\\"\\u6d3e\\u514b\\u5f04\\\"\\uff0c1865\\u5e74\\u6b63\\u5f0f\\u547d\\u540d\\u4e3a\\u5357\\u4eac\\u8def\\u3002\\u56fe\\u4e3a\\u4e24\\u5916\\u56fd\\u7f8e\\u5973\\u559d\\u51b7\\u996e\\u3002\\uff08\\u56fe\\u7247\\u6765\\u81ea\\u4e1c\\u65b9IC\\uff09\",\"\\u56fe\\u4e3a\\u5357\\u4eac\\u8def\\u6b65\\u884c\\u8857\\u4e0a\\u7684\\u5916\\u56fd\\u53cb\\u4eba\\u4e00\\u8def\\u4e0e\\u51b7\\u996e\\u76f8\\u4f34\\u3002\\uff08\\u56fe\\u7247\\u6765\\u81ea\\u4e1c\\u65b9IC\\uff09\",\"\\u4e0e\\u51b7\\u996e\\u4e3a\\u4f34\\u3002\\uff08\\u56fe\\u7247\\u6765\\u81ea\\u4e1c\\u65b9IC\\uff09\",\"\\u5929\\u6c14\\u786e\\u5b9e\\u6709\\u70b9\\u70ed\\u3002\\uff08\\u56fe\\u7247\\u6765\\u81ea\\u4e1c\\u65b9IC\\uff09\"],\"sub_titles\":[\"\\u5357\\u4eac\\u8def\\u6b65\\u884c\\u8857\\u8857\\u62cd\",\"\\u5357\\u4eac\\u8def\\u6b65\\u884c\\u8857\\u8857\\u62cd\",\"\\u5357\\u4eac\\u8def\\u6b65\\u884c\\u8857\\u8857\\u62cd\",\"\\u5357\\u4eac\\u8def\\u6b65\\u884c\\u8857\\u8857\\u62cd\"]}
# '''
# s1 ='{\"count\":9,\"sub_images\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"}],\"uri\":\"origin\\/pgc-image\\/15271742772357721d812e1\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"}],\"uri\":\"origin\\/pgc-image\\/1527174277647b550504541\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"}],\"uri\":\"origin\\/pgc-image\\/1527174278005c5432ac90d\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"}],\"uri\":\"origin\\/pgc-image\\/15271742783364a45600a3f\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"}],\"uri\":\"origin\\/pgc-image\\/152717427853791ec6e8e69\",\"height\":1096},{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"}],\"uri\":\"origin\\/pgc-image\\/152717427888877a89ab8b0\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"}],\"uri\":\"origin\\/pgc-image\\/15271742791887f7c85f8b1\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"}],\"uri\":\"origin\\/pgc-image\\/1527174279512815df3ef61\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"}],\"uri\":\"origin\\/pgc-image\\/1527174279792a645755c89\",\"height\":1104}],\"max_img_width\":690,\"labels\":[\"\\u65f6\\u88c5\\u642d\\u914d\"],\"sub_abstracts\":[\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\" \",\" \",\" \",\" \",\" \",\" \",\" \",\" \"],\"sub_titles\":[\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\"]}'


# tes = '''
# <!DOCTYPE html><html><head><meta charset=utf-8><title>重庆街拍，衬衫与牛仔裤的夏季搭配，时髦又有女人味！</title><meta http-equiv=x-dns-prefetch-control content=on><link rel=dns-prefetch href=//s3.pstatp.com/ ><link rel=dns-prefetch href=//s3a.pstatp.com/ ><link rel=dns-prefetch href=//s3b.pstatp.com><link rel=dns-prefetch href=//p1.pstatp.com/ ><link rel=dns-prefetch href=//p3.pstatp.com/ ><meta http-equiv=Content-Type content="text/html; charset=utf-8"><meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no,minimal-ui"><meta name=360-site-verification content=b96e1758dfc9156a410a4fb9520c5956><meta name=360_ssp_verify content=2ae4ad39552c45425bddb738efda3dbb><meta name=google-site-verification content=3PYTTW0s7IAfkReV8wAECfjIdKY-bQeSkVTyJNZpBKE><meta name=shenma-site-verification content=34c05607e2a9430ad4249ed48faaf7cb_1432711730><meta name=baidu_union_verify content=b88dd3920f970845bad8ad9f90d687f7><meta name=domain_verify content=pmrgi33nmfuw4ir2ej2g65lunfqw6ltdn5wselbcm52wszbchirdqyztge3tenrsgq3dknjume2tayrvmqytemlfmiydimddgu4gcnzcfqrhi2lnmvjwc5tfei5dcnbwhazdcobuhe2dqobrpu><link rel="shortcut icon" href=//s3a.pstatp.com/toutiao/resource/ntoutiao_web/static/image/favicon_8e9c9c7.ico type=image/x-icon><!--[if lt IE 9]>
#   <p>您的浏览器版本过低，请<a href="http://browsehappy.com/">升级浏览器</a></p>
# <![endif]--><script src="//s3.pstatp.com/toutiao/monitor/sdk/slardar.js?ver=20171221_1" crossorigin=anonymous></script><script>window.Slardar && window.Slardar.install({
#     sampleRate: 1,
#     bid: 'toutiao_pc',
#     pid: 'image_detail_new',
#     ignoreAjax: [/\/action_log\//],
#     ignoreStatic: [/\.tanx\.com\//, /\.alicdn\.com\//, /\.mediav\.com/]
#   });</script><meta name=pathname content=toutiao_pc_image_detail_new><meta name=keywords content=今日头条，头条，头条网，头条新闻，今日头条官网><meta name=description content=《今日头条》(www.toutiao.com)是一款基于数据挖掘的推荐引擎产品，它为用户推荐有价值的、个性化的信息，提供连接人与信息的新型服务，是国内移动互联网领域成长最快的产品服务之一。><link rel=stylesheet href=//s3b.pstatp.com/toutiao/static/css/page/index_node/index.54216f12b9c43dfe74dac14cfdc2068e.css><script>!function(e){function t(a){if(c[a])return c[a].exports;var o=c[a]={exports:{},id:a,loaded:!1};return e[a].call(o.exports,o,o.exports,t),o.loaded=!0,o.exports}var a=window.webpackJsonp;window.webpackJsonp=function(r,n){for(var p,s,l=0,i=[];l<r.length;l++)s=r[l],o[s]&&i.push.apply(i,o[s]),o[s]=0;for(p in n)Object.prototype.hasOwnProperty.call(n,p)&&(e[p]=n[p]);for(a&&a(r,n);i.length;)i.shift().call(null,t);if(n[0])return c[0]=0,t(0)};var c={},o={0:0};t.e=function(e,a){if(0===o[e])return a.call(null,t);if(void 0!==o[e])o[e].push(a);else{o[e]=[a];var c=document.getElementsByTagName("head")[0],r=document.createElement("script");r.type="text/javascript",r.charset="utf-8",r.async=!0,r.src=t.p+"static/js/"+e+"."+{1:"561720e91f5a0e0a3043",2:"be6fe966c0fc186b263c",3:"2a2c7b371c2c757802c3",4:"6a0a43d169ee2b10172e"}[e]+".js",c.appendChild(r)}},t.m=e,t.c=c,t.p="/toutiao/",t.p="//s3.pstatp.com/toutiao/"}([]);</script></head><body><div id=app></div><script src=//s3.pstatp.com/inapp/lib/raven.js crossorigin=anonymous></script><script>;(function(window) {
#     // sentry
#     window.Raven && Raven.config('//key@m.toutiao.com/log/sentry/v2/96', {
#       whitelistUrls: [/pstatp\.com/],
#       sampleRate: 1,
#       shouldSendCallback: function(data) {
#         var ua = navigator && navigator.userAgent;
#         var isDeviceOK = !/Mobile|Linux/i.test(navigator.userAgent);
#         if (data.message && data.message.indexOf('p.tanx.com') !== -1) {
#           return false;
#         }
#         return isDeviceOK;
#       },
#       tags: {
#         bid: 'toutiao_pc',
#         pid: 'image_detail_new'
#       },
#       autoBreadcrumbs: {
#         'xhr': false,
#         'console': true,
#         'dom': true,
#         'location': true
#       }
#     }).install();
#   })(window);</script><script>var PAGE_SWITCH = {"adScriptQihu":false,"adScriptTB":true,"anti_spam":false,"migScriptUrl":"//s3a.pstatp.com/toutiao/picc_mig/dist/img.min.js","nineteen":"","picVersion":"20180412_01","qihuAdShow":false,"taVersion":"20171221_1","ttAdShow":true};</script><script>var BASE_DATA = {
#     headerInfo: {
#       id: 0,
#       isPgc: false,
#       userName: '',
#       avatarUrl: '',
#       isHomePage: false,
#       chineseTag: '图片',
#       crumbTag: 'ch/news_image/',
#       hasBar: true
#     },
#     mediaInfo: {
#       name: '海玲时尚',
#       avatarUrl: '//p6.pstatp.com/large/382f0005b0e7dbc47d8d',
#       openUrl: '/c/user/58444595361/',
#       user_id: '58444595361',
#       like: false
#     },
#     userInfo: {
#       id: 0,
#       name: '',
#       avatarUrl: '',
#       isPgc: false,
#       isOwner: false
#     },
#     commentInfo: {
#       group_id: '6559163651570270723',
#       item_id: '6559163651570270723',
#       comments_count: 4,
#       ban_comment: 0
#     }
#   }
#
#   BASE_DATA.galleryInfo = {
#     title: '重庆街拍，衬衫与牛仔裤的夏季搭配，时髦又有女人味！',
#     isOriginal: false,
#     mediaInfo: BASE_DATA.mediaInfo,
#     gallery: JSON.parse("{\"count\":9,\"sub_images\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742772357721d812e1\"}],\"uri\":\"origin\\/pgc-image\\/15271742772357721d812e1\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174277647b550504541\"}],\"uri\":\"origin\\/pgc-image\\/1527174277647b550504541\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174278005c5432ac90d\"}],\"uri\":\"origin\\/pgc-image\\/1527174278005c5432ac90d\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742783364a45600a3f\"}],\"uri\":\"origin\\/pgc-image\\/15271742783364a45600a3f\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/152717427853791ec6e8e69\"}],\"uri\":\"origin\\/pgc-image\\/152717427853791ec6e8e69\",\"height\":1096},{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/152717427888877a89ab8b0\"}],\"uri\":\"origin\\/pgc-image\\/152717427888877a89ab8b0\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/15271742791887f7c85f8b1\"}],\"uri\":\"origin\\/pgc-image\\/15271742791887f7c85f8b1\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174279512815df3ef61\"}],\"uri\":\"origin\\/pgc-image\\/1527174279512815df3ef61\",\"height\":1104},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\",\"width\":690,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/1527174279792a645755c89\"}],\"uri\":\"origin\\/pgc-image\\/1527174279792a645755c89\",\"height\":1104}],\"max_img_width\":690,\"labels\":[\"\\u65f6\\u88c5\\u642d\\u914d\"],\"sub_abstracts\":[\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\" \",\" \",\" \",\" \",\" \",\" \",\" \",\" \"],\"sub_titles\":[\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\",\"\\u91cd\\u5e86\\u8857\\u62cd\\uff0c\\u886c\\u886b\\u4e0e\\u725b\\u4ed4\\u88e4\\u7684\\u590f\\u5b63\\u642d\\u914d\\uff0c\\u65f6\\u9ae6\\u53c8\\u6709\\u5973\\u4eba\\u5473\\uff01\"]}"),
#     siblingList: [],
#     publish_time: '2018-05-24 23:04:54',
#     group_id: '6559163651570270723',
#     item_id: '6559163651570270723',
#     share_url: 'https://m.toutiao.com/group/6559163651570270723/',
#     abstract: ''.replace(/<br \/>/ig, ''),
#     repin: 0
#   }</script><script>var imgUrl = '/c/2q4eiw4w5e2ycsyk9qg5naoiofnundefinedbrl4mzp4z6htctomujmsqqa3q/'</script><script>tac='i)69yvmdd0ls!i#zw5s"0,<8~z|\x7f@QGNCJF[\\^D\\KFYSk~^WSZhg,(lfi~ah`{md"inb|1d<,%Dscafgd"in,8[xtm}nLzNEGQMKAdGG^NTY\x1ckgd"inb<b|1d<g,&TboLr{m,(\x02)!jx-2n&vr$testxg,%@tug{mn ,%vrfkbm[!cb|'</script><script type=text/javascript crossorigin=anonymous src=//s3.pstatp.com/toutiao/static/js/vendor.561720e91f5a0e0a3043.js></script><script type=text/javascript crossorigin=anonymous src=//s3.pstatp.com/toutiao/static/js/page/index_node/index.be6fe966c0fc186b263c.js></script><script type=text/javascript crossorigin=anonymous src=//s3b.pstatp.com/toutiao/static/js/ttstatistics.6a0a43d169ee2b10172e.js></script><style>a[href^='http://www.cnzz.com/stat'] {
#       display: none!important;
#   }</style><script src="//s95.cnzz.com/z_stat.php?id=1259612802&web_id=1259612802" language=JavaScript></script><script>if (window.ttAnalysis) {
#     ttAnalysis.setup({
#       c: 'detail_gallery'
#     });
#     ttAnalysis.send('pageview', {});
#   }</script><script>document.getElementsByTagName('body')[0].addEventListener('click', function(e) {
#     var target = e.target,
#         ga_event,
#         ga_category,
#         ga_label,
#         ga_value;
#     while(target && target.nodeName.toUpperCase() !== 'BODY') {
#       ga_event = target.getAttribute('ga_event');
#       ga_category = target.getAttribute('ga_category') || 'detail_gallery';
#       ga_label = target.getAttribute('ga_label') || '';
#       ga_value = target.getAttribute('ga_value') || 1;
#       ga_event && window._czc && _czc.push(﻿["_trackEvent", ga_category, ga_event, ga_label, ga_value]);
#       ga_event && window.ttAnalysis && ttAnalysis.send('event', { ev: ga_event });
#       target = target.parentNode;
#     }
# });</script></body></html>
# '''
#
# img_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),', re.S)  # 注意，需要转义
# out = re.search(img_pattern, tes)
# result = out.group(1)
# print(result)
# a = json.loads(result)
# print(a)
#

from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import requests
import json
import os
from hashlib import md5
import re
import pymongo
from json.decoder import JSONDecodeError


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

def get_page_index(offset):
    """获取指定offset的response.json"""
    data = {
        'offset': offset,
        "format": "json",
        'keyword': '街拍',
        "autoload": "true",
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery',
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
            # return response.json()      # 将结果转换为json格式返回
    except RequestException:
        return 'get_page - RequestException....'

def parse_page_detail(html, url):
    img_pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)   # 注意，需要转义
    out = re.search(img_pattern, html)

    print('out------', out, html)
    # result = re.sub('\\\\', '', out.group(1))
    result = out.group(1)
    print('--', type(result), result)
    a = json.loads(result)
    print(a)

def parse_page_index(response):
    """返回article_url"""
    data = json.loads(response)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    '''请求article_url， 返回html'''
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)     #  allow_redirects允许跳转参数
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None


html = get_page_index(0)
for url in parse_page_index(html):
    html = get_page_detail(url)
    if html:
        result = parse_page_detail(html, url)
