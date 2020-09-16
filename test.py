from htmlManager import html
from cssManager import css, CssRand
blog = html()

blog.create('testHtml', 'title')
li = [['Home'],['about'],['more','f','c','d'],['more2','f','c','d']]
lis = [['a','b', 'ff'],['c','d'],['e','g'],['e','g'],['e','g']]
blog.addComponent('bp-navbar',li, "NavBar")
blog.addComponent('table',lis )
lisimg = ['51-TsSmY0lL._AC_SX466_.jpg', '51-TsSmY0lL._AC_SX466_.jpg', 'iphone.png']
blog.addComponent('slider', lisimg, '25')

blog.addComponent('video', 'MTWKL - Tayer Foog.mp4')
blog.info()
print(blog.getLinks())
blog.end()

cssm = css('style.css')
c = CssRand().color()
cssm.write('nav', {'bg-c': c})