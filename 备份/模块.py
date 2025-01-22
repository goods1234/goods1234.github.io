# coding:utf-8
import os, requests, random, time, parsel, pyautogui, sys, wx, re

# ============1.sys模块（系统模块）不同加括号========
#
# sys模块   system:系统/sistem/
# 1.sys.platform  :获取操作系统信息          [ˈplætfɔːm]平台
# 2.sys.modules   :查看已经加载到内存中的模块  ['mɒdʒʊlz]模块
# 3.sys.path      :Python 搜索模块的路径(是一个列表，能执行列表的所有操作)
#
#
# ============2.os模块（系统控制模块）========
# 1.getcwd                            获取当前文件路径（不包含当前文件），返回一个字符串类型
# 2.mkdir                             创建一个文件夹
# 3.shutil.rmtree()                   强制删,(shutil模块)更好用  [triː]数
# 4.system()                          执行系统命令
# 6.path.getsize                      获取文件or盘符大小
# 7.os.path.exists(path)              判断目标文件是否存在（返回布尔值）[ɪɡˈzɪsts]存在
# 8.os.path.isdir(path)               判断目标是否是文件夹
# 9.os.path.isfile(path)              判断目标是否是文件
# 10.makedirs                         创建多级文件目录  比如r"D:\A\o\u\l"
# 11.os.path.join(patn1,path2)        将两个路径拼接起来，形成一个新的路径
# 12.os.walk(path)                    获取目标文件下的所有文件目录（返回一个对象）使用元组拆包:for a,b,c in os.walk(s):分别打印a,b,c及一个回车符 [wɔːk]步行
# 13.environ                          获取系统环境变量  (无参数)   environment[ɪnˈvaɪrənmənt]环境
# 14.os.listdir(path)                 返回路径下所有文件包括隐藏文件和目录组成的列表 比如"D:/"    d盘下的文件

# ============3.pyautogui模块（键盘事件模块）========
# ========鼠标函数===========:
# pyautogui.PAUSE = 2.5      # 故障保险(常数)跟在导入后
# 获取当前屏幕大小（返回一个元组）:        size()
# 获取当前鼠标位置（返回一个元组）:        position()
# 检查当前屏幕是否存在点（x,y）:          onScreen(x,y)
# 移动鼠标到某一点:                     moveTo(x,y,time=None) time:移动到该点所用的时间
import pyautogui, time


# def 刷新():
#     for u in range(4):
#         pyautogui.moveTo(82, 56)
#         pyautogui.click(82, 56)
#         # 抢
#         pyautogui.moveTo(1183, 676)
#         for i in range(10):
#             pyautogui.click(1183, 676)
#             print("第{}次".format(i))
#
#
# #
# # times = "2023-03-19 22:59:59"
# times = "2023-03-19 22:59:59"
# # print(time.strftime("%Y-%m-%d %H:%M:%S"))
# while 1:
#     t = time.strftime("%Y-%m-%d %H:%M:%S")
#     if t == times:
#         刷新()

# 按住鼠标并拖动到一点:                  dragTo(x, y,time=None, button='c')   c是按住一个键 可以是 左键left 中键middle 右键right
# 当前鼠标位置向左or右移动x,y距离，反向为负:drag(x,y,time=None,button='c') c可以是 左键left 中键middle 右键right
# 点击:                               click(x,y)不填将点击当前位置
# 双击:                               doubleClick(x,y)不填将点击当前位置
# 按住某个键:(先移动在执行)               mouseDown(x,y,button='c')   c可以是 左键left 中键middle 右键right
# 释放某个键:                          mouseUp(x,y,button='c')     c可以是 左键left 中键middle 右键right
# 向上（正数）向下（负数）滚动鼠标:         scroll(次数)
# 向右（正数）向左（负数）滚动鼠标:         hscroll(次数)
# ========键盘函数===========:
# 在当前光标位置输入:                    write(str,time) str是内容 time每个字符输入的间隙
# 按某个键:                            press("c") c:键盘上的某个键
# 按住某个键:                           keyDown（"c"）
# 释放某个键:                           keyUp（"c"）

# 法国发过f'f'f'f'z'f'f'f'f'z'f'f'f'ff'f'f'z'f'f'f'f'z'fz'f'f'f'f'z'f'f'f'f'zz'f'f'f'f'z'f'f'f'fz'f'f'f'f'z'f'f'f'f'z'f'f'f'f'z'f'f'ff'f'z'f'f'f'f'z'f'f'f'f'z'f'f'f'f'z'ff'f'z'f'f'f'f'z'f'f'f'f'z'f'f'f'f'z'f
x = 1000
time.sleep(3)
while 1:
    if x > 0:
        pyautogui.press("z")
        # pyautogui.keyUp(" ")
        pyautogui.press("f")
        # pyautogui.keyUp(" ")
        pyautogui.press("f")
        # pyautogui.keyUp(" ")
        pyautogui.press("f")
        # pyautogui.keyUp(" ")fffffffffff
        pyautogui.press("f")
        # pyautogui.keyUp("f")
        x -= 1
    else:
        print("运行成功")
        break
# 简便方法:hold
#       with pyautogui.hold('shift'):
#               pyautogui.press(['left', 'left', 'left'])  #按住shift键再按3次左键再释放shift键
# 按顺序按住，反序释放:hotkey(键1, 键2,键3，interval=time)  time每个键输入的间隙
# 消息提示窗口
#   1.简单窗口(报警窗口):      alert(text=str1, title=str2, button='OK') str1:窗口内容 str2：窗口标题 button=用户可以点击的键
#   2.确定加取消（确认窗口）：   confirm(text=str1, title=str2, buttons=['OK', 'Cancel'])   Cancel：取消选择
#   3.返回输入文本（输入窗口）:  prompt(text=str1, title=str2 , default='') 当输入时，按确定将返回输入内容，取消则返回无
#   4.密码输入框（密码窗口）:    password(text=str1, title=str2, default='', mask='*') 当输入时用*隐藏输入，但返回时不隐藏的，按确定将返回输入内容，取消则返回none
# ========截图函数===========:
# 1.screenshot("path\文件名") path输出文件路径（图片默认为屏幕大小）
# 2.可定义截图区域（大小）:screenshot("path\文件名",region=(x,y, w, h)) x,y为某个点，w宽度，h高度

# wxpython

# 1.基础：
# 应用= wx.App(False)  # 实例化应用
# 窗口 = wx.Frame(None, wx.ID_ANY, "QQ")  # 框架，顶级窗口  （父对象，Id）wx.ID_ANY让 wxWidgets 为我们选择一个 id   Hello World：窗口标题
# 窗口.Show(True)  # 显示窗口
# 应用.MainLoop() # 启动应用程序
# =========================================================================================
# 2.简单框架：
# class 类(wx.Frame):
#     # 定义一个类继承wx.Frame
#     def __init__(self, parent, title):  # 该函数用于覆盖wx.Frame的__init__方法 parent：表示父类 title：窗口大小
#         wx.Frame.__init__(self, parent, title=title, size=(1280, 720))  # 传值给wx.Frame
#         self.文本 = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # wx.TextCtrl:文本编辑控件  style=wx.TE_MULTILINE表示可以输入多行，没有将只能输入一行
#         self.Show(True)  # 将显示加到wx.Frame的__init__方法中，后续将不需要调用  wx.Frame.Show(True)
#
# 应用 = wx.App(False)  # 实例化应用
# 窗口 = 类(None, 'QQ')
# 应用.MainLoop() # 启动应用程序

# =========================================================================================
# 添加菜单:
# class 主窗口(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(1280, 720))
#         self.文本 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.CreateStatusBar()  # 窗口底部的状态栏（可以忽略）
# # 设置菜单。
#         菜单 = wx.Menu()  # 建立菜单对象
# # wx.ID_ABOUT 和 wx.ID_EXIT 是wxWidget提供的标准ID（见文本AAA.txt）
#         菜单.Append(wx.ID_ABOUT, "关于", " Information about this program")f'f'f'f'z'f'f'f'f'z'f'f
#         菜单.AppendSeparator() # 分隔符（可以忽略）
#         菜单.Append(wx.ID_EXIT, "结束", " Terminate the program")
# # 创建菜单栏
#         菜单栏 = wx.MenuBar()  # 建立菜单栏对象
#         菜单栏.Append(菜单, "file")  # 将文件菜单添加到菜单栏
#         self.SetMenuBar(菜单栏)  # 将菜单栏添加到框架内容
#         self.Show(True) # 将显示加到wx.Frame的__init__方法中，后续将不需要调用  wx.Frame.Show(True)
# app = wx.App(False)  # 实例化应用
# frame = 主窗口(None, "QQ") # 设置顶级窗口
# app.MainLoop()  # 启动应用程序
# =========================================================================================
# 键盘鼠标事件处理:Bind（） 方法
# class 主窗口(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(1280, 720))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.CreateStatusBar()  # 窗口底部的状态栏（可以忽略）
#
#
# # 设置菜单。
#         菜单 = wx.Menu()  # 建立菜单对象
# # wx.ID_ABOUT 和 wx.ID_EXIT 是wxWidget提供的标准ID（见文本AAA.txt）
#         q=菜单.Append(wx.ID_ABOUT, "关于", " Information about this program")
#         菜单.AppendSeparator() # 分隔符（可以忽略）
#         菜单.Append(wx.ID_EXIT, "结束", " Terminate the program")
#         self.Bind(wx.EVT_MENU, self.OnABOUT, q)
#         self.Show(True)
# # 创建菜单栏
#         菜单栏 = wx.MenuBar()  # 建立菜单栏对象
#         菜单栏.Append(菜单, "file")  # 将文件菜单添加到菜单栏
#         self.SetMenuBar(菜单栏)  # 将菜单栏添加到框架内容
#         self.Show(True) # 将显示加到wx.Frame的__init__方法中，后续将不需要调用  wx.Frame.Show(True)
#
#     def OnABOUT(self,e):
#         dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
#         dlg.ShowModal()
#         dlg.Destroy()
# app = wx.App(False)  # 实例化应用
# frame = 主窗口(None, "QQ") # 设置顶级窗口
# app.MainLoop()  # 启动应用程序


# import wx
# class MainWindow(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(1280, 720))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.CreateStatusBar()  # A StatusBar in the bottom of the window
# # Setting up the menu.
#         filemenu = wx.Menu()
# # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
#         menuAbout = filemenu.Append(wx.ID_ABOUT, "关于", " Information about this program")
#         menuExit = filemenu.Append(wx.ID_EXIT, "退出", " Terminate the program")
# # Creating the menubar.
#         menuBar = wx.MenuBar()
#         menuBar.Append(filemenu, "文件")  # Adding the "filemenu" to the MenuBar
#         self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
# # Set events.
#         self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
#         self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
#         self.Show(True)
#     def OnAbout(self, e):# A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
#         dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
#         dlg.ShowModal()  # Show it
#         dlg.Destroy()  # finally destroy it when finished.
#     def OnExit(self, e):
#         self.Close(True)  # Close the frame.
# app = wx.App(False)
# frame = MainWindow(None, "Sample editor")
# app.MainLoop()


# 数学及可视化
import matplotlib.pylab as plt
import numpy as np
import math
# 一，math库(数学函数模块)
# 数论与表示函数
# 1.ceil:           浮点数向上取整,即大于或等于参数最小的整数,如果是整数会直接返回整数
# 2.comb(n,k):      不重复且无顺序地从 n 项中选择 k 项的方式总数.n>k
# 3.copysign(x,y):  返回一个基于 x 的绝对值和 y 的符号的浮点数.
# 4.fabs:           返回绝对值(是一个浮点型)。
# 5.fmod(x,y):用于浮点数的取余(x//y)
# 6.frexp(x):以元组的形式返回x==m*2**e中的m(浮点数)和e(整数)
# 7.gcd:返回给定的多个整数参数的最大公约数,无参数返回0
# 8.floor:浮点数向下取整,即大于或等于参数最小的整数,如果是整数会直接返回整数
# 幂函数与对数函数
# 1.exp(x):返回e**x的结果(e是自然对数=2.718281...)
# 2.log2(x):返回 x 以2为底的对数.
# 3.log(x,y):返回 x 以 y 为底的对数

# matplotlib.pylab库(可视化库)
# 1.imread:读取图片数据
#     1.matplotlib.pylab.imread.shape:返回图片的宽度,高度,色域(维度)的元组
# 2.imshow:将数据转为图片
# 3.show:展示图片,无参数，放在imshow之后
# ps=plt.imread(r"C:\Users\撸瓜\Desktop\训练原素材\5month\不知火\00000.png")
# # print(ps)
# print(ps.shape)
# plt.imshow(ps)
# # plt.show()
# tkinter库
# import tkinter
# root = tkinter.Tk()  # 创建tk对象
# root.geometry("960x768")  # 窗口大小
# root.title("启动器")  # 窗口标题
# 页面1=tkinter.Frame(root)  # 创建页面框架
# 页面1.pack()  # 接手页面布局管理
# 文本=tkinter.Label(页面1,text="这是第一页:",font=24,padx=10,pady=10)  # 标签控件:指定的窗口中显示的文本和图像。(用户无法修改)(页面对象,text=页面文本,font=字体大小,padx=离x轴距离,pady=离y轴距离)
# 文本.pack(side="right",anchor="n") # 接手页面布局管理,side: 决定组件停靠的方向,anchor: 决定组件停靠的位置
# 图片=tkinter.PhotoImage(file=r"C:\Users\撸瓜\Desktop\xxx.png")  # 加载图片
# 显示图片=tkinter.Label(页面1,image=图片,padx=10,pady=10,bd=0)  # bd=标签文字边框宽度，bd=‘边框宽度’。边框宽度显示需要配合边框样式才能凸显。
# 显示图片.pack(side="left",anchor="n")
# root.mainloop()  # 显示窗口

