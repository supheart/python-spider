import urllib2
from bs4 import BeautifulSoup
import re

response = urllib2.urlopen("http://www.baidu.com")
# html_doc = response.read()
html_doc = '<div id="u_sp" class="s-isindex-wrap s-sp-menu"> <a href="http://www.nuomi.com/?cid=002540" target="_blank" class="mnav">糯米</a> <a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a> <a href="http://www.hao123.com" target="_blank" class="mnav">hao123</a> <a href="http://map.baidu.com" target="_blank" class="mnav">地图</a> <a href="http://v.baidu.com" target="_blank" class="mnav">视频</a> <a href="http://tieba.baidu.com" target="_blank" class="mnav">贴吧</a><a id="s_username_top" class="s-user-name-top" data-tid="2004" href="http://i.baidu.com/" target="_blank"><span class="user-name">枼心</span></a><a id="s_usersetting_top" href="javascript:;" name="tj_settingicon" class="pf s-user-setting-top"><span class="setting-text">设置</span></a><a href="http://www.baidu.com/more/" name="tj_briicon" class="s_bri" target="_blank"> 更多产品</a><div id="s_user_name_menu" class="s-isindex-wrap s-user-set-menu menu-top" style="right: 128px; display: none;"><div><a href="http://vip.baidu.com/pcui/show/ucenterindex?vip_frm=super_account" target="_blank"> 我的VIP </a> <a href="http://i.baidu.com/center" target="_blank" data-tid="1000"> 个人中心 </a> <a href="http://passport.baidu.com/" data-tid="1001" target="_blank"> 帐号设置 </a> <a class="s-feedback" style="overflow:hidden" href="#" onclick="return false;">意见反馈</a> <a class="quit" style="overflow:hidden" href="#" onclick="return false;"> 退出 </a> </div> <span class="menu-arrow"> <em></em> </span> </div><div id="s_user_setting_menu" class="s-isindex-wrap s-user-set-menu menu-top" style="display:none;"><div> <a href="//www.baidu.com/gaoji/preferences.html" target="_blank"> 搜索设置 </a> <a href="//www.baidu.com/gaoji/advanced.html" target="_blank"> 高级搜索 </a> <a href="http://i.baidu.com/my/history?from=index" target="_blank"> 搜索历史 </a> <a class="s-feedback" style="overflow:hidden" href="#" onclick="return false;"> 意见反馈 </a> </div> <span class="menu-arrow"> <em></em> </span> </div></div>'

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print "获取所有的链接"
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print "获取单一的链接"
link_node = soup.find('a', href="http://passport.baidu.com/")
print link_node.name, link_node["href"], link_node["data-tid"], link_node.get_text()

print "获取正则匹配"
link_node = soup.find('a', href=re.compile(r"history"))
print link_node.name, link_node["href"], link_node.get_text()
# print link_node["data-tid"]

print "获取class节点"
span_node = soup.find('span', class_="menu-arrow")
print span_node.name, span_node.get_text()



