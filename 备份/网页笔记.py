# 能"一招鲜，吃遍天"就好
# 可以不考虑ie兼容问题，ie2020年已经停止支持了
# 没有的可以去看菜鸟教程
# 大部分问题都是路径问题（谁引用就以谁为起始点）
#         1.比如css文件的引用
#         2.css文件引用字体图标fonts文件

# 补充
# 1.在浏览器标签上设置图像
# <link rel="icon" href="图片路径" type="image/x-icon">
# =====================标签1========================
# 一.html语法
#     一.语法规范
#         1.HTML标签使用尖括号包围关键词，比如<html>
#         2.大多标签为双标签，少部分为单标签
#         3.双标签分为头标签和尾标签，尾标签比头标签多一个/
#     二.标签关系
#         1.包含关系:嵌套
#         2.并列关系
#     三.基本结构标签
#         1.html:根标签
#         2.head：文档头部（其内必须设置title标签）
#         3.title:文档标题，页面的标题
#         4.body:文档的主题，包含所有页面内容
# 示例:
# <html>
#     <head>
#         <title> 这里是标题 </title>
#     </head>
#     <body>
#     这里是页面信息
#     </body>
# </html>
# 、、、、、、、、、、、、、、、、、、、、、、、、、、
# 基本骨架(快捷键:先输入英文的!再点击tab键)
# <!DOCTYPE html>
# <html lang="zh-CN">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width,initial-scale=1.0">
#     <meta http-equiv="x-ua-compatible" content="ie=edge">
#     <title></title>
# </head>
# <body>
#
# </body>
# </html>
# ////////////////////////////////////////////
# 三.骨架信息作用
#     1.<!DOCTYPE>:文档申明标签，用于告诉浏览器使用那中html版本解析网页
#     2.lang:语言种类(告知浏览器该网页为何种语言)，en为英语zh-CN为中文
#     3.charset:存储格式，用何种格式储存代码内容
# /////////////////////////////////////////////////
# 四.常用标签
#     1.标题标签（双标签）:<h1>-----<h6>一级至六级标题  （独占一行，代码也是）
#     2.段落标签（双标签）:<p>                        (用于定义段落,每对标签中的文字为一个段落，且每对标签之间会有一个空行)
#     3.换行标签（单标签）:<br />                     (需要强制换行的地方使用,代码遇到<br />就会强制换行)
# 五.文本格式化标签
#     1.加粗标签（双标签）:<strong>或<b>               (用于加粗文字)
#     2.倾斜标签（双标签）:<en>或<i>
#     3.删除线标签（双标签）:<del>或<s>                 (会给文本添加一条删除线)
#     4.下划线标签（双标签）:<ins>或<u>
# 六.盒子标签（当作一个容器）（双标签）
#     1.<div>:(独占一行)
#     2.<span>:跨距显示，可以一行多个
# 七.图像标签(单标签)
#     1.<img src=""/>:     src="路径"（必须属性）
#         1.其他属性（无顺序要求）:
#             1.alt:     替换文本，图像不能正常显示会用文字替换
#             2.title:   提示文本,鼠标放到图像上，显示的文字
#             3.width:   设置图像的宽度
#             4.height:  设置图像的高度
#             5.border:  设置图像的边框粗细
#     2.图片路径格式:
#         1.相对路径:
#             1.同级路径直接为: 文件名
#             2.下一级路径为:  文件夹/文件名
#             3.上一级路径为:  ../文件名（每上一级加一个../）
#         2.绝对路径（极少使用）
#             1.整个路径(可能协议不允许)
# 八.超链接标签（双标签）<a>（用于链接不同页面）
#     1.语法格式: <a href="跳转目标的链接" target="目标窗口弹出方式">文本或图像</a>
#       1.属性：    target不写或target="_self"为在当前窗口打开页面，="_blank"为在新窗口打开
#     2.链接分类
#         1.外部链接:                         网站域名（必须http开头）
#         2.内部链接(网站中多个页面):            直接页面名称.html就行了
#         3.空连接:#                          (开发使用)
#         4.下载链接:                         如果链接为一个压缩包或文件时，会下载
#         5.描点链接(链接到当前页面的某一位置):1.href="#名字" 2.在目标标签的头标签添加属性 id=名字
#         6.网页元素也能作为链接，将网页元素放与<a>与</a>之间比如   <a><p><strong><i>李白 〔唐代〕</i></strong></p></a>
# 九.注释标签: <!--内容-->
# 十.特殊字符(前三记住)
#     1.空格:         &nbsp;
#     2.<:           &lt;
#     3.>:           &gt;
#     4.&:           &amp;
#     5.人民币:       &yen;
#     6.乘号:        &times;
#     7.除号:        &divide;
#     8.平方:        &sup2;
#     9.立方:        &sup3
#     10.正负号:     &piusmn;
#     11.摄氏度:     &deg;
#     12.版权:      &copy;
#     13.注册商标:   &reg;
# ====================标签2======================
# 十一.表格标签（双标签）
#     1.语法:    <table><tr><td>    </td></tr></table>
#         1.<table>:用于定义表格，<tr>表格中的定义行（可以多个），<td>是数据（可以多个）
#     2.表头单元格（内容会加粗并居中显示）:<th> 放在<tr>中
#     3.表格属性（写在<table>里）
#         1.align=          left左对齐，cebter居中 right右对齐
#         2.border=         1表示有边框，""表示没有边框
#         3.cellpadding=    外边框距离内容的距离
#         4.cellspacing=    单元格之间的距离
#         5.width=          单元格的宽度
#         6.height=         单元格的高度
#     4.结构标签
#         1.<thead>:规定表格头部区域
#         2.<tbody>:规定表格主体区域
#     5.合并单元格(合并后删除多余的单元格)
#         1.行合并:rowspan="数量"  合并相邻行单元格(写在上侧单元格里)
#         2.列合并:colspan="数量"  合并相邻列单元格（写在左侧单元格里）
# 十二.列表标签（双标签）（用于布局里面）
#     1.无序列表:                        <ul><li>内容</li></ul>     <ul> 定义列表 </li>定义列表内部列表  注意:ul里只能放li,li里面可以放任何东西
#     2.有序列表（了解）:                  <ol><li>内容</li></ol>
#     3.自定义列表(一个标题下有多个小标题):   <dl><dt>名词</dt><dd>名词解析1</dd><dd>名词解析2</dd></dl>
# 十三.表单标签(与用户交互，用于收集用户信息)
#     1.结构:表单域（整个表单），表单控件（表单元素，交互区），提示信息（表单文本）
#     2.表单域（规定返回服务器的信息的区域）:<form action="url地址" method="提交方式" name="表单域名称">表单元素控件</form>
#         1.action= 服务器程序的url地址
#         2.method=   get或post
#     3.表单控件（单标签)（以下包含在<form></form>中）
#         1.输入表单元素:<input type="属性值" name（可选）="表单元素名字" value（可选）="提示内容"/>
#             1.属性值type：
#                 1.text:      定义单行的输入字段，用户可以输入，默认宽度为20
#                 2.password:  定义一个密码框，用户看不到输入的密码
#                 3.radio:     定义一个单选框（不可取消）
#                 4.checkbox:  定义一个复选框（可取消）
#                 5.submit:    定义提交按钮，提交按钮会把表单数据提交给服务器（改变文本需添加value="文本"）
#                 6.reset:     定义重置按钮，点击将重置页面输入数据（改变文本需添加value="文本"）
#                 7.button:    定义点击按钮（用于启动脚本，如获取验证码）
#                 8.file:      定义上传文件按钮
#             2.属性name:                （当定义名字相同的两个表单元素，选择时只会被选择一个）注：单选框或复选框要有相同的name值
#             3.属性value:                用户输入框内的提示信息 或 在复选框中定义返回服务器的value值
#             4.属性checked="checked":    页面首次加载input会被默认选中
#             5.属性maxlength（了解）:      规定输入字符的长度
#         2.label标签:（用于快速定位光标）
#             1.语法:<label for="名字">提示信息</label><input.....id="名字"/>   注意:for 要与id的内容相同
#         2.下拉表单元素（下拉菜单）:
#            1.语法:<select><option>文本1</option><option>文本2</option></select>   <option>中可以定义selected="selected" 即该项为默认选中项
#         3.文本域元素(用于定义多行的文本输入):
#             1.语法:<textarea>提示内容</textarea>
#                 1.属性cols="":每行最多能写的字数(了解)
#                 1.属性rows="":最多能显示多少行(了解)
# =============================CSS===========================
# 简介
#     1.结构:选择器+声明(可以多条)
#     位置:一般放在head标签里的<style></style>标签中（多个css之间不用任何东西隔开）[staɪl]款式
#     代码结构:
#     <style>选择器(被修改对象) {修改样式（名称:值;...）}</style>
# 基础选择器(作用:选择标签)
# 1.分类:基础选择器，复合选择器。
#     基础选择器:标签选择器，类选择器，id选择器，通配符选择器。
#     复合选择器:
# 标签选择器:以html标签作为选择器（会全选）
#     语法:标签名{属性1:属性值;属性2:属性值;...}
# 类选择器:可以单独选中一个或几个标签（定义一个类(在<style></style>标签中)，再调用(在开始标签内部调用:class="类名")）
#     语法（定义）:<style>.类名{样式}</style>
#     多类名(将公共的定义为一个类，减少后期修改麻烦性):class中可以调用多个类名，必须要用空格隔开（一个字符串里）。
# id选择器:(与类选择器相似)先定义，再调用(在开始标签内部调用:id="类名")），区别，只能调用一次
#     语法(定义):<style>#类名{样式}</style>
# 通配符选择器（选取所有的元素），定义即生效。
#     语法:<style>* {样式}</style>
# CSS字体属性
#     1.font-family: 字体类型(可以指定多个字体，用;隔开，电脑没有第一字体时，尝试第二字体，以此类推)[fɒnt]字体 [ˈfæməli]家
#     2.font-size:   字体大小(单位用px)，标题标签比较特殊，需要单独指定字体大小
#     3.font-weight: 字体粗细，属性值;bold:粗体,bolder:特粗体，lighter:细体 直接数字（100-900 700以后加粗，400正常字体）[weɪt]重量
#     4.font-style:  字体样式。属性值;normal:默认值，浏览器会显示标准的字体:，italic:浏览器会显示斜体
#     5.复合属性:      略
# CSS文本属性
#     1.color:字体颜色，值可使用英文，16进制(开发常用)，rbg,比如rgb(255,0,0)
#     2.text-align:对齐文本，只能设置水平对齐方式，center:居中，left:左对齐（默认），right:右对齐，
#     3.text-decoration:给文本添加下划线,删除线等。none:没有装饰线（默认,可取消a的下划线），underline:下划线（链接a自带下划线，常用），line-through:删除线
#     4.text-indent:首行缩进，使用px或em(相对单位，匹配当前文本的一个字符大小)表示
#     5.line-height:行间距（行高，行与行之间的距离），使用px，行高测量（选中目标文本，颜色区域显示即可看懂）
# CSS引入方式
#     1.行内样式表（行内式）:将样式全部放在<style>标签中，方便控制整个页面。（针对少量代码使用）
#     2.内部样式表（嵌入式）:在标签内部使用<style>，比如<p style="...">，使用简单的样式，只能控制当前标签。（极少使用）
#     3.外部样式表（连接式）:开发常用，适用于样式多的情况，样式单独写在CSS文件中，将CSS文件引入HTML中即可，需要建立一个后缀名为.css的文件（文件内部直接写样式即可）。
#     内部注释格式:/*注释*/
#     4.引入CSS:使用<link>单标签标签，格式:<link rel="stylesheet" href="css文件路径"> 放在body标签上面
# Chrome调试工具:浏览器提供的调试工具，用于调试HTML结构和CSS样式
#     1.打开Chrome调试工具:F12健或右键-检查，点击元素一栏，左边是HTML右边是CSS
#     2.使用Chrome调试工具
#         1.Ctrl+滚轮，放大代码大小
#         2.左边是HTML右边是CSS
#         3.右边CSS可以改动数值,属性,查看颜色，点击击左边目标标签，即可在右边修改，双击即可编辑
#         4.Ctrl+0，还原工具大小
#         5.点击左边元素，发现右边没有CSS引入，极有可能类名或样式引入错误
#         6.如果有样式，但样式前面有黄色感叹号提示，则样式属性书写错误
# Emmet语法，它使用缩写，提高html和css的编写速度，Vscode/pycharm内部都已经集成该语法
#     1.使用Emmet语法快速生成HTML标签
#         1.生成标签:输入标签名后按tab健即可，比如p然后按tab健生成<p></p>
#         2.生成多个标签:输入标签名*数量然后按tab即可
#         3.生成有父子（包含）关系的标签:用>，比如ul>li
#         4.生成有兄弟（并列）关系的标签:用+，比如div+p
#         5.生成带类名的:写x.类名按tab健即可（x表示标签名，不写默认为div标签）
#         6.生成带id的:写x#类名按tab健即可（x表示标签名，不写默认为div标签）
#         7.生成的类名/id名是有顺序的:使用$*x（x表示数量）
#         8.生成标签即有内容:使用{}，比如，p{内容}，生成多个自增内容:p{$}*x
#     2.使用Emmet语法快速生成css标签:基本采用简写的形式再按tab即可(略)
# 复合选择器
#     1.什么是复合选择器:复合选择器是建立在基础选择器之上，对基本选择器进行组合形成的。
#     2.复合选择器可以更准确，高效的选择目标元素（标签）
#     3.复合选择器由两个或多个基础选择器，通过不同方式组合而成。
#     4.常用的复合选择器有:后代选择器，子选择器，并集选择器，伪类选择器等
#     后代选择器:用于选择目标标签中的标签，比如选择ul中的li(ol中也有li)
#         1.格式:目标标签 目标标签的内部标签(可多层){...} 比如ul li{...}或.类名 li{...}
#     子选择器:只能选择下一级字元素，不能选择下下一级子元素(少用)
#         1.格式:元素1>元素2{}
#     并集选择器:可以选择多组标签，同时为它们定义相同的样式，常用于集体声明
#         1.格式:元素1,元素2,...{}
#     伪类选择器:用于向某些选择器添加特殊效果，比如给链接添加特俗效果，或选择第一，第n个元素。
#         1.格式:冒号标签名
#         2.链接伪类标签
#             1.a:link 选择未被访问的链接
#             2.a:visited 选择所有已经被访问的链接
#             3.a:hover 选择鼠标指针位于其上的链接
#             4.a:active 选择活动链接（鼠标按下未弹起的链接）
#             5.注意：书写时按link-visited-hover-active的顺序写，不然可能不起作用
#             6.因为a链接具有默认样式，所以我们实际工作中需单独给链接指定样式
#         3.focus伪类选择器:用于选择获得焦点（光标）的表单元素。(少用)
#             1.格式:input:focus{...}
# CSS元素显示模式
#     1.作用:网页标签非常多，在不同的地方会用到不同类型的标签，了解他们的特点可以更好的布局网页
#     2.什么是元素显示模式:元素（标签）以什么方式进行显示，HTML元素一般分为块元素和行内元素两种。
# 块元素：<h1>-<h6>,<p>,<div>,<ul>,<ol>,<li>...
#     特点：
#         1.独占一行
#         2.高度，宽度，外边距，内边距都可以控制
#         3.宽度默认是容器（父级宽度，也就是上一级）的100%
#         4.是一个容器及盒子，里面可以方行内或块元素
#         5.注意:文字类元素内不能使用块元素，比如<p>中不能放块元素。
# 行内元素：<a>,<strong>,<b>,<em>,<i>,<del>,<s>,<ins>,<u>,<span>...
#     特点:
#         1.相邻行内元素在一行上，一行可以显示多个
#         2.高，宽直接设置无效
#         3.默认宽度就是它本身内容的宽度
#         4.行内元素只能容纳文本或其他行内元素
#         5.注意:链接内不能再放链接，特殊情况<a>可以放块级元素，但是给<a>转换以下块级模式最安全
# 行内块元素:同时具有块和行内元素的特点,<img/>,<input/>,<td>
#     特点：
#         1.和相邻行内元素（行内块）在一行上，他们之间会有空白空隙。一行可以显示多个
#         2.默认宽度就是它本身内容的宽度
#         3.高度，宽度，外边距，内边距都可以控制
# 元素显示模式转换:一个模式的元素需要另一个元素模式的特性，比如增强<a>的触发范围
#     转换为块元素格式：display:block，放在样式中
#     转换为行内元素格式：display:inline，放在样式中
#     转换为行内块元素格式：display:inline-block，放在样式中
# 小技巧：单行文字垂直居中，让文字的行高等于盒子的高度即可，即height与line-height相等
# 小工具snipaste推荐（一个软件，微软商店免费下载）
#     常用快捷方式：
#         1.F1可以截图，同时测量大小，设置箭头，书写文字等。
#         2.F3在桌面置顶显示
#         3.点击图片，alt可以取色，（按下shift可以切换取色模式）
#         4.按下esc取消图片显示
# CSS背景
#     1.background-color:背景颜色,默认透明
#     2.background-image:背景图片，多使用与logo或一些装饰性的小图片或超大的背景图片，参数url(地址)，默认为none，优点，非常便于控制位置
#     3.background-repeat:背景平铺(当图片大小小0于容器大小时会出现多张图片)，参数：repeat平铺，no-repeat不平铺，repeat-x延x轴平铺，repeat-y延y轴平铺
#     4.background-position:背景图片位置,格式，background-position:x,y;（可使用方位名词或精准单位）
#         1.参数是方位名词(top,center,left,bottom,right)
#             1.如果指定的两个参数都是方位名词，则不用考虑前后顺序，效果一致
#             2.如果中指定一个方位名词，第二个不写，则第二个值默认为居中对齐
#         2.精准单位:百分数,px,em...
#             1.顺序为x,y
#         3.混合单位:方位名词与精准单位组合使用，顺序为x,y
#     5.background-attachment:背景图像固定:图片是否随页面滚动（视差滚动），参数scroll滚动(默认)，fixed固定
# 背景符合写法
#     1.直接使用background:背景颜色 背景图片地址 背景平铺 背景图像滚动 背景图片位置（没有顺序要求，但惯例是这样）
# 背景色半透明(盒子的背景色半透明，内容不受影响)
#     1.background:rgba(x,y,z,透明度) 透明度取值范围0-1
# CSS三大特性
#     1.层叠性:解决样式冲突问题
#         1.样式冲突:遵循就近原则，那个样式离结构近，就执行那个样式（css文件会加载到style中，即越下面的越近）
#         2.样式不冲突:不层叠
#     2.继承性:子标签会继承父标签的某些样式
#         1.恰当的使用可以简化代码，降低CSS的复杂性
#         2.子元素继承父元素的部分样式(text-开头，font-开头，line-开头，color)
#         3.行高的继承性:当行高不指定单位时，即表示子元元素的行高大小是子元素内容大小*父元素无单位数值（当上一级父元素没有行高，行高会逐级往上找）
#     3.优先级:当一个元素指定多个选择器，就会产生优先级
#         1.选择器相同，则执行层叠性
#         2.选择器不同，根据选择器权重执行
#         3.选择器权重（上到下变高，继承的权重为0）
#             1.继承或通配符选择器:0,0,0,0
#             2.标签选择器:0,0,0,1
#             3.类，伪类选择器:0,0,1,0
#             4.ID选择器:0,1,0,0
#             5.行内样式（style=""）:1,0,0,0
#             6.!important:无穷大（在样式值后加，不用空格）
#         4.权重叠加:复合选择器会有权重叠加（累加即可）
# 盒子模型
#     1.盒子模型的组成
#         1.边框（border）:边框
#         2.内容(content):内容
#         3.内边距(padding):盒子内容与边框之间的距离
#         4.外边距(margin):盒子与盒子之间的距离
#     2.边框
#         1.border-width:定义边框粗细（所有边框），一般用px
#             1.border-top上边框
#             2.border-bottom:下边框
#             3.border-left:左边框
#             4.border-right:右边框
#         2.border-style:边框样式，参数:solid实线边框，dashed虚线边框，dotted点线边框
#         3.border-color:边框颜色
#         4.边框复合写法:格式:border 某px  样式 颜色（没有顺序）
#         5.border-collapse:collapse:合并相邻边框，不会使相邻边框线变大。
#         6.边框会影响盒子大小，加边框会变大
#     3.内边框（可由于内容字数不一样多时，给定相同的内边框，就看起来比较好看）
#         1.padding-top上边框
#         2.padding-bottom:下边框
#         3.padding-left:左边框
#         4.padding-right:右边框
#         5.复合写法
#             1.格式:padding:a b c d;(当只有一个值时表示上下左右，两个时，a表示上下，b表示左右，三个时，a表示上，b表示左右，c表示下，四个时，表示上右下左)
#         6.padding会影响盒子大小,盒子会变大（当不指定宽度时不会影响）
#     4.外边距
#         1.margin-top上边距
#         2.margin-bottom:下边距
#         3.margin-left:左边距
#         4.margin-right:右边距
#         5.典型运用:外边距可以让盒子水平居中，需满足一下条件
#             1.盒子必须指定宽度
#             2.盒子左右外边距都设置为auto,即加上margin:0 auto;
#         6.行内元素，行内块元素水平居中,直接给其父元素添加text-align:center;即可
#         7.嵌套块元素垂直外边距坍陷问题:对于两个嵌套关系（父子关系）的块元素，都有外边距时，父元素会有较大的（外边距）塌陷
#             1.解决方法:给父元素添加overflow:hidden;即可
#         8.清除内外边距:许多网页元素会带有默认的内外边距，浏览器不同值也不同，所以在布局前，需要删除默认内外编剧。
#             1.解决方法:定义一个通配符选择器，加上padding:0（清除内边距）;和margin:0（清除外边距）;即可*{padding:0;margin:0;}
#         9.注意:行内元素为了照顾兼容性，最好不要设置上下内边距，但是转换为块，行内块元素可以。
#     5.圆角边框：让盒子变成圆角
#         1.border-radius:设置外边框圆角,参数为px或百分比\
# 盒子阴影（不占用空间）
#     1.box-shadow:h-shadow（实际为一个px） v-shadow（实际为一个px） blur（实际为一个px） spread（实际为一个px） color inset（不变）;
#         1.h-shadow:必须值，水平阴影的距离（沿x轴移动，允许负数）
#         2.v-shadow:必须值，垂直阴影的距离（沿y轴移动，允许负数）
#         3.blur:可选，模糊距离
#         4.spread:可选，阴影尺寸
#         5.color:可选，阴影颜色
#         6.inset:可选，将外部阴影改为内部阴影
#         7.鼠标经过时出现阴影:使用,选择器名:hover{...}即可
# 文字阴影(少用)
#     1.text-shadow:h-shadow（实际为一个px） v-shadow（实际为一个px） blur（实际为一个px）color;
#         1.h-shadow:必须值，水平阴影的距离（沿x轴移动，允许负数）
#         2.v-shadow:必须值，垂直阴影的距离（沿y轴移动，允许负数）
#         3.blur:可选，模糊距离
#         4.color:可选，阴影颜色
# 网页布局的三种方式（一个网页应该包括三种方式）
#     1.标准流
#     2.浮动
#     3.定位
# 浮动
#     1.作用:许多布局，标准流无法实现，浮动可以解决，最典型的是用于，让多个块级元素在一行内排列显示
#     2.网页布局第一准则:多个块级元素纵向排列使用标准流，多个块级元素横向排列使用浮动
#     3.什么是浮动:float属性用于创建浮动框，将其移动到一边，指导左边或右边触及到另一个浮动框的边缘。
#     4.float:创建浮动框，参数有none不浮动(默认)，left左浮动，right右浮动
# 浮动特性
#     1.脱离标准流的控制（浮），移动到指定位置（动），俗称脱标
#     2.浮动的盒子不在保留原先的位置
#     3.如果多个盒子都设置了浮动，则他们会按照属性值一行内显示并且顶端对齐排列。
#     4.浮动元素具有行内块元素特点(即不用再转换，可直接设置宽高)
#         1.如果块级盒子没有设置宽度，默认同父级，但添加浮动过后，大小根据内容决定。
#         2.浮动的盒子中间没有缝隙。
#         3.行内元素同理。
# 浮动元素一般搭配标准流父元素使用，即父元素是标准流，子元素是浮动
# 注意:
#     1.浮动一般搭配标准流使用（使用标准流排列上下位置，之后内部元素使用浮动排列左右位置）
#     2.盒子中的一个元素浮动，一般其他元素也要浮动（浮动的盒子只会影响浮动盒子后面的标准流，不会影响前面的标准流）
# 清除浮动
#     1.问题，当子元素过多（或是一个模板）时，父盒子不适合写死大小
#     2.为什么要清除浮动:父盒子不方便给高度时，但子盒子浮动右不占位置，此时父盒子高度为0，就会影响下面的标准流（父级没有高度，子盒子浮动，影响到下面的布局）
#     3.清除浮动的本质
#         1.清除浮动的本质是清除浮动元素造成的影响
#         2.如果父盒子本身有高度，则不需要清除浮动
#         3.清除浮动之后，父级就会根据浮动的子盒子自动检测高度。父级有了高度，就不会影响下面的标准流了
#     4.清除浮动的方法
#         1.给父元素添加overflow:hidden;
#         2.使用伪元素(类似于两个类选择器，只需要在父元素中调用该类选择器（用clearfix名即可）即可，可以调用多个（用空格隔开）如class="选择器1 clearfix")
#                 .clearfix:after{content:"";display:block;height:0;clear:both;visibility:hidden;}
#                 .clearfix{/*解决IE6,IE7兼容问题*/*zoom:1;}
#         3.使用双伪元素(调用同2，比2更好用)
#                 .clearfix:before,.clearfix:after{content:"";display:table;}
#                 .clearfix:after{clear:both;}
#                 .clearfix{/*解决IE6,IE7兼容问题*/*zoom:1;}
# CSS属性书写顺序（只是建议，专业人士必备）
#     1.布局定位属性：display/position/float/clear/visibility/overflow(建议display第一个写，毕竟关系到模式)
#     2.自身属性：width/height/margin/padding/border/background
#     3.文本属性：color/font/text-decoration/text-align/vertical-align/white-space/break-word
#     4.其他属性(CSS3):content/cursor/border-radius/box-shadow/text-shadow/background:linear-gradient...
# 定位
#     1.为什么要有定位:可以让元素更自由的改变位置，或者固定在屏幕的某个地方
#     2.定位的组成:定位模式（指定元素在文档中的定位方式）+边偏移（决定元素的最终位置）
#     3.position:定位模式，参数：static静态定位，relative相对定位，absolute绝对定位，fixed固定定位
#     4.边偏移
#         1.top:顶端偏移量，定义元素相对于其父元素上边线的距离，用px，如top:25px;
#         2.bottom:底部偏移量，同同理1
#         3.left:左侧偏移量，同同理1
#         4.right:右侧偏移量，同理1
# 静态定位(等于标准流):默认定位方式，无定位意义（了解）
#     1.语法:position:static;
# 相对定位，元素在移动位置的时候，是相对于它原来的位置(以元素左上角为原点)来说的
#     1.语法:position:relative;
#     2.原位置依然占有空间，不会被其他元素占用，后面的元素依然以标准流来对待他
#     3.他典型的应用是用来限制绝对定位
# 绝对定位,元素在移动位置时，是相对于他的祖先元素来说的
#     1.语法:position:absolute;
#     2.如果没有祖先元素或者祖先元素没有定位，则以浏览器为准定位。
#     3.如果祖先元素有定位（静态定位不算），则以最近一级的有定位祖先元素为参考点移动位置。
#     4.绝对定位不再占有原来的位置（脱标）
# 子绝父相（大多是这样的情况）
#     1.子级绝对定位，不会占有位置，可以放到父盒子里面的任何位置，不会影响其他的兄弟盒子。
#     2.父盒子需要加定位限制子盒子在父盒子内显示。
#     3.父盒子布局时，需要占有位置，因此父盒子只能是相对的。
# 固定定位，元素固定于浏览器可视区的位置，主要用于可以在浏览器页面滚动时元素位置不会改变。
#     1.语法:position:fixed;
#     2.以浏览器的可视窗口为参照物移动元素。
#     3.跟父元素没有任何关系
#     4.不随滚动条滚动移动
#     5.固定定位不再占有原来的位置（可以看作一种特殊的绝对定位）
#     技巧:固定在版心左侧
#         算法:
#             1.让固定定位的盒子left:50%
#             2.让固定定位的盒子margin-left:版心宽度的一半（版心多大你自己懂）
# 粘性定位（不常用，兼容性差），固定定位与相对定位的混合。
#     1.语法：position:sticky;
#     2.以浏览器的可视窗口为参照物移动元素。
#     3.原位置依然占有空间，不会被其他元素占用，后面的元素依然以标准流来对待他
#     4.必须添加top、left、right、bottom其中的一个才有效
# 定位的叠放次序，在使用定位时，可能出现定位重叠的情况，需要控制盒子的叠放次序。
#     1.语法：z-index:数值;
#     2.数值可以是正数、负数、0，数值越大优先级越大
#     3.如果属性值相同，按照书写顺序，后来居上（后面的压住前面的）
#     4.数值不加单位
#     5.只有定位的盒子才有该属性，普通的标准流没有
# 定位拓展:
# 绝对定位的盒子水平居中的方法
#     1.让盒子left:50%;
#     2.让盒子margin-left:-值（盒子宽度的一半）
# 绝对定位的盒子垂直居中的方法
#     1.让盒子top: 50 %;
#     2.让盒子margin-left: -值（盒子高度的一半）
# 定位的特殊特性：
# 绝对定位和固定位和也和浮动类似。
#     1.行内元素添加绝对或者固定定位，可以直接设置高度和宽度。
#     2.块级元素添加绝对或者固定定位，如果不给宽度或者高度，默认大小是最内容的大小。
# 脱标的盒子不会触发外边距塌陷
#     1..浮动元素、绝对定位（国定定位）元素的都不会触发外边距合并的问题。
# 绝对定位（固定定位）会完全压住盒子
#     1.浮动元素不同，只会压住它下面标准流的盒子，但不会压住下面标准流盒子里面的文字（图片）。（因为浮动最初的目的是为了做文字环绕效果）
#     2.绝对定位会压住下面标准流所有的内容。
# 元素的显示和隐藏：
# 类似广告，当我们点击关闭就不见了，但重新刷新页面，会重新出现。
# 本质：让一个元素在网页中隐藏或显示出来。
# 1.display属性—隐藏元素后不占有原来的位置
#     1.display:none;：隐藏对象
#     2.display:block;：除了转化为块级元素外，同时还有显示元素的意思
# 2.visibility属性—隐藏元素后占有原来的位置
#     1.visibility:visible;：元素可视
#     2.visibility:hidden;：元素隐藏
# 3.overfole属性—溢出隐藏
#     属性值
#         1.visible：不切除内容也不显示滚动条（默认属性）
#         2.hidden：超出部分删除掉不显示
#         3.scroll：不管内容是否超出都显示滚动条
#         4.auto：超出自动显示滚动条，不超出不显示滚动条
#         5.注意：有定位的盒子请慎用hidden
# CSS高级技巧
# 精灵图（sprites）
# 作用为了有效减少服务器接收和发送请求的次数，提高页面的加载速度。
# 原理：将网页中的一些小背景图像整合到一张大图中，这样服务器只需要请求一次即可
#     1.精灵图主要针对背景图片使用，就是把多个小背景图片整合到一张大图片当中。
#     2.大图称为精灵图
#     3.移动背景图片位置，使用background-position
#     4.移动的距离是图片的x,y轴，以左上角为原点，右边为x正半轴，左下边为y轴正半轴————原点为图片对齐盒子的左上角。
#     5.使用精灵图的时候需要精准测量，每个背景图片的大小和位置。
#     6.background-position:xpx ypx;，px为单位，负值为负半轴方向走
#     7.步骤：创建盒子（大小等于要使用的精灵图部分的大小）——给盒子加上背景图片（background:url(图片路径)）——移动图片位置（background-position:xpx ypx;）
# 精灵图缺点
# 1.图片文件比较大
# 2.图片本身放大或缩小会失真
# 3.一档图片制作完毕，需要更换非常复杂
# 字体图标
# 字体图标的使用场景
#     1.主要用于显示网页中通用、常用的一些小图标
#     2.解决精灵图的缺点
#     3.字体图标可以为前端工程师提供一种方便的图标使用方式，展示的是图标，本质属于字体
# 优点
# 1.轻量级：一个图标字体比一系列图像要小，提单字体加载了，图标就会马上渲染出来，减少了服务其请求
# 2.灵活性：本质四字体，可以改变颜色、产生阴影、透明效果、旋转等
# 3.兼容性：几乎兼容所有浏览器
# 总结：简单的图标使用字体图标，复杂的图标1使用精灵图
# 字体图标的下载
# 网站
# 1.icomoon字库——外网
# http://icomoon.io
# 2.阿里iconfont字库
# http://www.iconfont.cn
# 字体图标的引用
# 1.把下载的包里的fonts文件夹放入页面根目录下，同.html在一个目录
# 2.在CSS样式中全局声明字体：通过CSS引入页面
# 3.引用部分在字体文件夹同目录的style.css文件中，从@font-face开始到font-display:block;}部分即可
# 示例：(embedded-opentype、truetype、woff、svg四种不同的字体格式是为了解决浏览器兼容问题)
# @font-face{
# font-family:'icomoon';
# src:url('路径');
# src:url('路径') format('embedded-opentype'),
# url('路径') format('truetype'),
# url('路径') format('woff'),
# url('路径') format('svg'),
# font-weight:normal;
# font-style:normal;
# font-display:bllock;
# }
# 4.在字体文件夹有一个demo.html文件，打开文件复制图标对应的小方框到需要该图标的盒子或标签中（把它看作字体即可）
# 5.再给盒子或标签声明一个字体，使用选择器给盒子或标签声明一个字体，在选择器中添加font-family:'icomoon';即可icomoon可以自定义，一般直接使用即可
# 字体图标的追加
# 在下载字体图标的网页中，加载以前下载的字体图标的selection.json文件，原来的字体图标就加载好的，在选择要追加的字体图标，然后再下载字体图标文件，然后替换原来的文件夹即可
# CSS三角
# 1.将盒子的高度和宽度指定为0
# 2.指定一定长度的透明边框
# 3.将左边框、右边框、上边框、下边框其中的一个指定某一颜色即可
# 示例：
# .名字{
#     width:0; # 宽度
#     height:0; # 高度
#     border: xpx solid transparent; # x像素长的透明边框
#     border-top-color:pink; # 上边框为粉色
# }
# ===========用户界面样式=================
# 鼠标样式（cursor）
# 作用：设置或检索在对象上移动的鼠标指针采用何种系统预定义的光标样式
# 语法
# cursor:属性值;
# 属性值：
#     1.defaul：默认
#     2.pointer：小手
#     3.move：移动
#     4.text：文本
#     5.not-allowed：禁止
# 轮廓线（对目标进行添加而不是对包住他的盒子添加）
# 1.给表单添加outline:0;或outline:none;样式后，就可以去掉默认的蓝色边框。————推荐像清空默认内外边距一样多使用
# 防止拖拽文本域
# 1.设置文本域不可拖拽：添加resize:none;即可
# vertical-align属性的使用场景；用于设置图片或者表单（行内元素）和文字垂直对齐
# 1.解释：用于设置一个元素的垂直对齐方式，（只对行内元素，行内块元素有效）
# 2.属性值：baseline(基线对齐/默认属性)，top(顶端对齐),middle(中部对齐)，bottom(底部对齐)
# 3.解决图片底部默认空白间隙问题
#     1.原因图片底部有空白间隙，是行内块元素和文字的基线对齐导致
#     2.解决方法
#         1.给图片添加vertical-align:top|middle|bottom等（提倡使用）
#         2.将图片转换为块级元素 display:block;
# 溢出的文字省略号显示
# 1.单行文本溢出显示省略号-必须满足三个条件
#     1.强制一行内显示文本: white-space:noworap;  (默认为normal自动换行)
#     2.超出部分隐藏: overflow:hidden;
#     3.文字用省略号代替超出部分: text-overflow:ellipsis;
# 2.多行文本溢出显示省略号，需严格控制盒子大小-有较大兼容性问题，适用于webkit浏览器或移动端（移动端大部分为webkit内核）
#     1.超出部分隐藏: overflow:hidden;
#     2.文字用省略号代替超出部分: text-overflow:ellipsis;
#     3.弹性伸缩模型显示: display:-wekit-bok;
#     4.限制在一个块元素显示的文本行数: -webkit-line-clamp:n(一个数字，代表行数)
#     5.设置或检索伸缩对象的子元素的排序方式: -weblit-box-orient:vertical;
# 常见布局技巧
# 1.margin负值的运用
#     1.当多个盒子排序时，盒子与盒子的边框会出现1+1=2的情况，这时只要给其中一个盒子的一条边框添加 margin-left:负值(向左移动x像素)即可
#     2.在1的基础上需要添加鼠标经过某一盒子时，盒子边框改变颜色，解决思路:如果盒子没有定位，鼠标经过时添加相对定位，若果有则加 z-index:1;
# 2.文字围绕浮动元素
#     1.思路:一个大盒子包含两个小盒子，其中一个盒子为文字盒子，另一个图片盒子或其他，文字盒子不用指定宽高采用标准流，另一个盒子采用浮动，那么文字将绕浮动元素
# 3.行内块的巧妙运用-更快速的制作翻页盒子（网页常见的翻页布局）
# 示例：
# 1.目标:
# <div class="翻页盒子">
#     <a href="#">1</a>
#     <a href="#">2</a>
#     <a href="#">3</a>
#     <a href="#">4</a>
# </div>
# 2.css：
# /*复合选择器-后代选择器-选择目标标签中的标签*/
# .翻页盒子 a{
# /*转换为行内块元素格式*/
# display:inline-block;
# /*设置宽高*/
# width:35px;
# height:35px;
# /*设置背景颜色*/
# background-color:red;
# /*设置边框及边框颜色*/
# border:1px solid blue;
# /*文字水平居中*/
# text-align:center;
# /*文字垂直居中-让文字的行高等于盒子的高度即可，即height与line-height相等*/
# line-height:35px;
# /*移除a的下划线*/
# text-decoration:none;
# }
#
# .翻页盒子{
# /*文字水平居中-使其内的所有标签居中*/
# text-align:center;
# }
# 4.css三角强化（要得到想要的三角形）
# 示例：
# /*设置宽高*/
# width:0;
# height:0;
# /*设置边框颜色-透明（上） 红色（右） 透明（下） 透明（左）*/
# border-color:transparent red transparent transparent;
# /*设置边框样式*/
# border-style:solid;
# /*定义边框粗细（所有边框）-上-右-左-下*/
# border-width:22（自定义）px 8（自定义）px 0 0;

# CSS初始化
# 不同浏览器对不同标签的默认值是不同的，为了消除差异性，兼顾不不同浏览器，需要对CSS初始化
# 代码(复制粘贴直接用)：
# /*以下为CSS初始化代码*/
# /*清空默认内外边距，加上就对了*/
# *{padding:0;
# margin:0;
# }
# /*取消em,i标签的文字倾斜*/
# em,i{
# font-style:normal
# }
# li{
# /*去掉li的小圆点*/
# list-style:none
# }
# img{
# /*为了兼顾低版本浏览器-如果图片外面有链接会有边框的问题*/
# border:0
# /*取消图片底侧右空白的问题*/
# vertical-align:middle
# }
# button{
# /*鼠标经过button时会变成小手，告诉用户可以点击*/
# cursor:pointer
# }
# .a{
# /*设置颜色*/
# color:#666
# /*取消下划线*/
# text-decoration:none
# }
# a:hover{
# /*鼠标经过变红色*/
# color:red;
# }
# .button,input{
# /*给所有的按钮指定字体-\5B8B\4F53表示宋体，如果使用中文会出现乱码情况所以不用中文*/
# font-family:Microsoft YaHei,Heiti SC,tahoma,arial,Hiragino Sans GB,"\5B8B\4F53",sans-serif;
# }
# .body{
# /*抗锯齿让文字显示更加清晰-拼写没错*/
# -webkit-font-smoothing:antialiased;
# /*设置背景色*/
# background-color:white;
# /*指定字体大小/1.5倍行高，及字体*/
# font:12px/1.5 Microsoft YaHei,Heiti SC,tahoma,arial,Hiragino Sans GB,"\5B8B\4F53",sans-serif;
# /*字体颜色*/
# color:#666;
# }
# /*清除浮动-使用伪元素(类似于两个类选择器，只需要在父元素中调用该类选择器（用clearfix名即可）即可，可以调用多个（用空格隔开）如class="选择器1 clearfix")*/
# .clearfix:after{content:"";display:block;height:0;clear:both;visibility:hidden;}
# .clearfix{/*解决IE6,IE7兼容问题*/*zoom:1;}
# /*以上为CSS初始化代码*/

# Unicode编码字体:
# 把中文字体的名称用Unicode编码代替，可以避免浏览器解释css代码的时候乱码。
# 示例:
# 1.黑体:     \9ED1\4F53
# 2.宋体:     \5B8B\4F53
# 3.微软雅黑:  \5FAE\8F6F\96C5\9ED1

# ==========================CSS进阶部分-HTML5与CSS3===========================
# HTML5的新特性
# HTML5的新增特性主要是针对于以前的不足，增加了一些新的标签、新的表单和新的表单属性等。这些新特性都有兼容性问题，基本是IE9+以上版本的浏览器才支持，
# 如果不考虑兼容性问题，可以大量使用这些栽特性。
# 1.html5新增的语义标签
#     1.<header>:   头部标签
#     2.<nav>:      导航标签
#     3.<article>:  内容标签
#     4.<section>:  定义文档某个区域
#     5.<aside>:    侧边栏标签
#     6.<footer>:   尾部标签
# 2.html5新增的多媒体标签
#     注:谷歌默认禁用自动播放
#     1.<audio>:  音频标签-当前只支持三种格式MP3(所有浏览器都支持此格式),Wav,Ogg
#         语法:<audio src="文件地址" controls="controls"></audio>
#         常见属性:
#             1.src属性:视频地址（路径）
#             2.autoplay属性:属性值autoplay（自动播放）
#             3.controls属性：属性值controls（向用户显示播放控件）
#             4.loop属性:属性值loop(循环播放)
#             5.muted属性:属性值muted(静音播放)
#     2.<video>:  视频标签-当前只支持三种格式MP4(所有浏览器都支持此格式),WebM,Ogg
#        语法:<video src="文件地址" controls="controls"></video>
#         常见属性:
#             1.src属性:视频地址（路径）
#             2.autoplay属性:属性值autoplay（自动播放）(如果是谷歌浏览器需要加上muted="muted"才会自动播放)
#             3.controls属性：属性值controls（向用户显示播放控件）
#             4.width属性:播放器宽度（px）  在标签设置，当=100%时等于浏览器宽度
#             5.height属性:播放器高度(px)  在标签设置，当=100%时等于浏览器高度
#             6.loop属性:属性值loop(循环播放)
#             7.preload属性:属性值auto(预先加载视频),none(不加载视频)
#             8.poster属性:属性值 图片(路径)地址(加载等待的画面图片)
#             9.muted属性:属性值muted(静音播放)
# 3.html5新增的input标签
#     属性值               说明
#     1.type="email"      限制用户输入必须为Email类型
#     2.type="url"        限制用户输入必须为URL类型
#     3.type="date"       限制用户输入必须为日期类型
#     4.type="time”       限制用户输入必须为时间类型
#     5.type="month"      限制用户输入必须为月类型
#     6.type="'week"      限制用户输入必须为周类型
#     7.type="number"     限制用户输入必须为数字类型（重点）
#     8.type="tel"        手机号码（重点）
#     9.type="search"     搜索框（重点）
#     10.type="color"     生成一个颜色选择表单
# 4.html5的表单属性
# 属性                值            说明
# 1.required         required         表单拥有该属性表示其内容不能为空，必填
# 2.placeholder      提示文本          表单的提示信息，存在默认值将不显示
# 3.autofocus        autofocus       自动聚焦属性，页面加载完成自动聚焦到指定表单
# 4.autocomplete     off/on          当用户在字段开始键入时，浏览器基于之前键入过的值，应该显示出在字段中填写的选项。
#                                    默认已经打开，如autocomplete="on”，关闭autocomplete ="off"需要放在表单内，
#                                    同时加上name属性，同时成功提交（了解）
# 5.multiple         multiple        可以多选文件提交

# CSS三的新特性
# 1.css新增选择器
#     1.属性选择器（权重为11）-可以根据元素的特定属性来选择元素，这样就不用借助类或id选择器。
#         语法1:某标签[某标签中的属性]{...}
#         示例:
#             html:
#                 <input type="text" value="请输入用户名">
#                 <input type="text">
#             css:
#                 input[value]{...}会选择的一个
#         语法2:某标签[某标签中的属性="值"]{...}     （重点）
#         示例:
#             html:
#                 <input type="text" value="请输入用户名">
#                 <input type="text" value="请输入内容">
#             css:
#                 input[value="请输入内容"]{...}     会选择的第二个
#         语法3:某标签[某标签中的属性^="以什么开头"]{...}
#         语法4:某标签[某标签中的属性$="以什么结尾"]{...}
#         语法5:某标签[某标签中的属性*="含有什么(不判断开头或结尾，只要含有就选择)"]{...}
#         示例:
#             htlml:
#                 <div class="ico1"></div>
#                 <div class="ico2x"></div>
#                 <div class="px"></div>
#             css1:
#                 div[class^=ico]{...}       会选择的第一第二个
#             css2:
#                 div[class$=x]{...}         会选择的第二第三个
#     2.结构伪类选择器
#         语法1:某标签:first-child   选择父元素中的第一个          （针对多个相同且同级的标签有效，执行方式，从后往前执行，当存在不同的标签时可能无效）
#         语法2:某标签:last-child    选择父元素中的最后一个        （针对多个相同且同级的标签有效，执行方式，从后往前执行，当存在不同的标签时可能无效）
#         语法3:某标签:nth-child(n)  选择父元素中一个或多个（重点）  （针对多个相同且同级的标签有效，执行方式，从后往前执行，当存在不同的标签时可能无效）
#                 1.n可以是:     数字，关键字，公式
#                 2.n是数字时:   代表选择第n个子元素。数字从1开始
#                 3.n是关键字时: even偶数，odd奇数
#                 4.n是公式时，常见公式（）:
#                     1.当是n时，则从0开始一直累加选择元素，但是第0个和超出的元素会被忽略
#                     2.当是2n时，等价于even
#                     3.当是2n+1时，等价于odd
#                     4.当是5n时，表示5、10、15...，公式里可以不是5
#                     5.n+5时，表示从第五(包含第五个)个开始到最后，公式里可以不是5
#                     5.-n+5时，前五个(包含第五个)，公式里可以不是5
#         语法4:某标签:first-of-type   选择父元素中的第一个     （存在不同的标签时也有效，执行方式，从前往后执行)
#         语法5:某标签:last-of-type    选择父元素中的最后一个    (同理语法4)
#         语法6:某标签:ntf-of-type(n)    选择父元素中的最后一个(使用语法同理语法3)    (同理语法4)
#         示例1:
#             html:
#                 <ul>
#                     <li>第一个</li>
#                     <li>第二个</li>
#                     <li>第三个</li>
#                     <li>第四个</li>
#                 </ul>
#             css1:
#                 ul :first-child{...}      选择第一个li
#                 ul :last-child{...}       选择最后一个li
#                 ul :nth-child(2){...}     选择第二个li
#                 ul :nth-child(even){...}  选择第二第四个li
#                 ul :nth-child(odd){...}   选择第一第三个li
#                 ul :nth-child(n){...}     选择所有li
#         示例2:
#             html2:
#                 <ul>
#                     <p>第一个</p>
#                     <li>第二个</li>
#                     <li>第三个</li>
#                     <li>第四个</li>
#                     <p>第五个</p>
#                 </ul>
#             css2:
#                 li:first-of-type{...} 会选择第二个，也就是第一个li,如果是li:first-child{...}将无法选中
#                 li:last-of-type{...}  会选择第第四个个，也就是第三个li,如果是li:last-child{...}将无法选中
#     3.伪元素选择器（权重为1加上标签也就是2）-可以帮助我们利用CSS创建新标签元素，而不需要HTML标签，从而简化HTML结构（创建的元素在文档树（右键检查）中找不到，所以称为伪元素）
#         选择符        说明
#         ::before     在元素内部的前面插入元素（创建的元素属于行内元素）
#         ::after      在元素内部的后面插入元素（创建的元素属于行内元素）
#         1.语法:标签::before{}
#         before和after必须有content属性，比如标签::before{content:"内容（可以不写内容但引号要有）";}
#     4.伪元素的使用场景
#         1.伪元素字体图标
#             示例:
#             html:
#                 <div></div>
#             css:
#                 /*以下为引用字体图标，详见字体图标，所有路径为当前文件调用的字体fonts文件所在路径*/
#                 @font-face {
#                   font-family: 'icomoon';
#                   src:  url('../字体图标/fonts/icomoon.eot?5pdkhh');
#                   src:  url('../字体图标/fonts/icomoon.eot?5pdkhh#iefix') format('embedded-opentype'),
#                     url('../字体图标/fonts/icomoon.ttf?5pdkhh') format('truetype'),
#                     url('../字体图标/fonts/icomoon.woff?5pdkhh') format('woff'),
#                     url('../字体图标/fonts/icomoon.svg?5pdkhh#icomoon') format('svg');
#                   font-weight: normal;
#                   font-style: normal;
#                   font-display: block;
#                   }
#                 /*以上引用字体图标*/
#                 /*设置盒子宽高-方便显示*/
#                 div{
#                 width:auto;
#                 height:40px;
#                 }
#                 /*伪元素选择器*/
#                 div::before{
#                 /*声明字体*/
#                 font-family:'icomoon';
#                 /*调用字体-字体的demo.html文件可以查看字体编码*/
#                 content:'\e936';
#                 }
#         2.图片加阴影
#             示例:
#                 html:
#                     <div class="遮罩层"><img src="../image/新建文件夹/sex.jpg" width="1000px" height=auto></div>
#                 css:
#                     .遮罩层{position: relative;width:1000px;height:auto;}
#                     .遮罩层::before{content:"";display:none;position:absolute;top:0;left:0;width:100%;height:100%;background-size:1000px;
#                     }
#                     .遮罩层:hover::before{
#                     /*当鼠标经过时，让before遮罩层显示出来*/
#                     display:block;
#                     background:rgba(0,0,0,0.5);
#                     }
#         3.伪元素清除浮动
#             示例1:
#                 .clearfix:after{
#                 /*伪元素必须写的属性*/
#                 content:"";
#                 /*插入的伪元素必须是块级*/
#                 display:block;
#                 /*不要看见这个元素*/
#                 height:0;
#                 /*清除浮动*/
#                 clear:both;
#                 /*不要看见这个元素*/
#                 visibility:hidden;
#                 }
#             示例2:
#             双伪元素清除浮动
#                 .clearfix:before,.clearfix:after{content:"";display:table;}
#                 .clearfix:after{clear:both;}
#                 .clearfix{/*解决IE6,IE7兼容问题*/*zoom:1;}
# 2.css三盒子模型
#     css3通过box-sizing来指定盒子模型有两个值
#         1.box-sizing:content-box;  盒子大小为width+padding+border，相当于外扩(默认)
#         2.box-sizing:border-box;   盒子大小为width，相当于内缩
# 3.css其他特性（了解）
#     1.filter:滤镜-filter属性可以将模糊或颜色偏移等图形效果应用于元素
#         语法:filter:函数();
#         比如:filter:blur(5px); blur模糊处理，数值越大越模糊（js模块会详细的将函数）
#         calc()函数-计算函数-,+,_,*,/都可以
#             比如当子盒子永远比父盒子小x像素:(运算符用空格隔开)
#                 width:calc(100% - 30px);   100%表示父盒子的宽度
# 4.css3过度（重点）-通常和hover搭配使用(谁变化就加在谁上)当需要改变多个属性时在第一个的后加逗号再写一遍即可（transition:width 5s ease 1s,height 5s ease 1s...;）
#     语法:transition:要过度的属性 花费的时间 运动曲线 何时开始;
#         要过度的属性:  想要变化的css属性，宽高，背景颜色，内外边距都可以，写all代表所有属性
#         花费的时间:    单位是秒。比如1s
#         运动曲线:      默认是easa(可以省略)
#         何时开始:      单位是秒（必须写单位），可以设置延迟出发时间，默认是0s(可以省略)
#     示例:
#         html:
#             <div></div>
#         css:
#             div{
#             width:100px;
#             height:100px;
#             background-color:pink;
#             transition:width 5s;
#             }
#             div:hover{
#             width:500px;
#             }
# 5.广义的HTML5:html5+css3+javascript

# ================================================================================
# ============================JavaScript==========================================
# ============================JavaScript==========================================
# ================================================================================
# 一 JavaScript介绍
#     1.什么是js:
#         是一种运行在客户端（浏览器）的编程语言，实现人机交互效果。
# 二 javascript的书写位置
#     1.行内js——直接写在html文件里，用script标签包住,script标签写在</body>上面。
#     将script写在html文件底部的原因:浏览器会按照代码在文件中的顺序加载html。如果先加载js，那么可能由于html尚未加载而失效。
#     示例:
#         <body>
#         ...
#         <script>...</script>
#         </body>
#     2.内部js--代码写在html标签内部（了解，vue框架才会用到）
#         示例:
#             <button onclick="alert("你好")">确认</button>
#     3.外部js
#         语法:<script src="js文件路径"></script> 同样写在</body>上面（标签中间不用写内容，写也不会执行）。
# 三 js注释及结束符
#     1.注释
#         1.单行注释://内容
#         2.多行注释:/*内容*/
#     2.结束符
#         语法:结尾使用;
#         实际开发中，可写可不写，浏览器(js引擎)会制动判断语句的结束位置，（实际开发中，人们主张省略结束符，所以js文件要么都写要么都不写）
# 四 输入输出语法
#     1.输入语法:
#         1.prompt("提示文本:")
#             显示一个对话框，对话框中包含一条文本信息，用来提示用户输入文字（类似python中的input）
#     2.输出语法:
#         1.document.write("内容")
#             向body内输出内容，可以输出标签（会被解析为网页元素）
#         示例:
#             document.write("你好")
#             document.write("<h1>一级标题</h1>")
#         2.alert("内容")
#            页面弹出警告对话框
#         3.console.log("内容")
#             控制台输出语法，调试用（输出在浏览器右键-控制台）
# 五 变量
#     1.变量的声明
#         语法:let 变量
#     2.变量的赋值（同python）
#     3.可以同时声明+赋值
#         示例:let age = 10
#     4.变量的命名规则
#         1.不能使用关键字
#         2.只能用下划线、字母、数字、$、组成，且不能以数字开头
#         3.区分大小写
#         4.小驼峰体写法--第一个单词首字母小写，后续的单词首字母大写，比如:userName
#         5.常量--使用const声明得变量叫常量
#             语法:const 变量名=值
#             注意:
#                 1.常量不允许重新赋值，声明的时候必须赋值（初始化）
#         6.数组（类似列表）
#             语法:let 数组名=[数据1,数据2...]
#             索引从0开始（类似列表）
# 六 基本数据类型
#     1.数字类型:只要是数字统称为数字类型，整数
#         1.算术运算符--乘（*）除（/）加（+）减（-）取余（%）
#         2.NaN:表示一个计算错误，任何对NaN的操作都会返回NaN(是粘性的)
#     2.字符串类型:使用单引号('')、双引号("")、反引号(``)包裹的数据都是字符串--推荐使用单引号，双引号CSS在用，做一个区分
#         1.字符串可以拼接（使用+号拼接）
#         2.格式化字符串
#             1.语法:`...${变量名}`
#             示例:
#                 let age=1
#                 document.write(`我现在${age}岁了`)
#     3.布尔类型(true和false)
#     4.未定义类型(undefined)
#         1.未定义是比较特殊的类型，只有一个值--undefined
#         2.只声明变量，不赋值的情况下，变量的默认值为undefined
#     5.空类型（null）
#         1.代表空、无、未知
#         2.赋值为null即为空类型
#     6.类型检测
#         1.使用函数typeof()
#         2.使用函数typeof  # 不加括号也行
# 七 类型转换
    1.隐式转换
        1.+只要有一边是字符串，就会把另一边转换为字符串
        2.除了+以外的算术运算符会把数据转换为数字类型
    2.显式转换