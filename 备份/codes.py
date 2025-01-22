# 第三方库快速安装代码（镜像）:使用终端安装or cmd
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 库名
# 手动安装第三方库(前提安装有pip)：
#     1.下载第三方库:https://pypi.org/    版本选择：pandas-2.1.1(库版本)-cp310(python版本)-cp310-win_amd64（操作系统版本）.whl
#     2.将第三方库文件放到C:\Users\用户文件夹内
#     3.cmd终端输入pip install 第三方库文件全名
#     4.等待安装完成:出现Successfully installed 库名即为成功。
# 注意:编辑器如果无法找到第三方库，极有可能第三方库只安装在解释器根目录而没有安装在编辑器根目录中，此时需要将第三方库复制一份到编辑器第三方库目录中
# 补充
# 1.内置函数
# 1.1 abs() 绝对值函数
# print(abs(-1))
# 1.2 all()函数 可迭代中的布尔值都为True才会返回True 如果为None也返回True
# 1.3any()函数 可迭代中的布尔值有一个为True就会返回True 如果为None也返回False
# a=[1,2,3,4,0]
# b=[]
# print(all(a),all(b))
# print(any(a),any(b))
# 1.4bin()将十进制转化二进制 ,oct()将十进制转化8进制 ,hex() 将十进制转化16进制
# 1.5bool() 布尔类型
# print(bool(15))
# 1.6callable() 判断一对象是否可以被调用
# class foo():
#     pass
# print(callable(foo))
# 1.7.chr(x) 返回 Unicode编码x对应的单字符.ord(x) 返回单字符×表示的Unicode编码
# 1.8 complex() 复数类型
# 1.9dir() 查看对像有哪些属性
# 1.10 divmod(x,y) xy表示两个数，回返回x/y的（商，余数）
# 1.11 enumerate() 与for联用可以得到可迭代对象的（索引，值）
# 1.12isinstance() 类型判断 比type好用，判断一个对象是不是一个类的实例
# 1.13pow() (x,y,z) x**y%z
# 1.14round()四舍五入
# #变量的定义
# # 1.先定义，再引用。
# name = "ps"
# print(name)
# L = "W"
# print(L)
# # 、、、、、、、、、、、、、、、
# # 垃圾回收机制
# x = 10
# y = x
# z = x
# print(x)
# print(y)
# print(z)
# del x  # （解除变量x与10的绑定关系）
# # print(x) x会无效
# # 、、、、、、、、、、、、、、、、、、、、、、、、
# # 变量名的命名风格
# # 1.纯小写加下划线(多用这个）
# name_of_my='wei ye fu'
# print(name_of_my)
# #2.驼峰体————首字母大写
# NameOfMy="wei ye fu"
# print(NameOfMy)
# #、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 变量值的两个特性
# # 1.id (反映变量值的内存地址）内存地址不等于不同id不同
# x=10
# print(id(x))#(id查找方式)
# #2.type（类型)
# y =2
# print(type(y))
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # is与==
# x="w"
# y="w"
# # is 比较的是id是否相等
# #== 比较的是值是否相等
# print(x,y)
# print(id(x),id(y))
# # 、、、、、、、、、、、、、、、、、
# #常量，不变的量
# #全大写表示
# #NAME=10让别人知道它不能改
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 数字类型
# # 1.整型1.2.3.。。。。。
# # 2.浮点型——小数
# # 、、、、、、、、、、、、、、、、、、、、、
# #字符串类型
# #定义:用引号"","","外层用多引号内层用小一级引号
# y="1'2'"
# print(y)
# x = "1""2""3"
# print(x)
# #、、、、、、、、、、、、、、、、、、、、、、、、、
# #列表
# #作用:记录多个值，并且可以按照索引取指定位置的值
# #定义:在[]内用逗号分隔开多个任意类型的值，一个值称为一个元素
# x=[1,2,3,4,5,6,7,8,9]or [1,"2","3"]
# y=[1,"tt",'u',3]
# print(y[0])
# print(y[1])
# print(y[2])
# print(y[3])
# print(y[-1]) #负的没有0
# print(y[-2])
# #、、、、、、、、、、、、、、、、、、、、、、、、、
# #列表与列表
# x=["dog",1,["water"]],["cat",2,["milk"]]
# print(x[1][2])
# #、、、、、、、、、、、、、、、、、、、、、、、、、
# #字典类型:key对应值，其中通常为字符串类型，所以key对值可以有描述性
# #作用:用来存多个值，每个值有唯一对应key，key对值有描述性
# #定义:在{}内用逗号分开多个key:value
# w={"dog":1,"cat":2}
# print(w["dog"])
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 布尔类型（真假）就两个
# #True
# #False
# #、、、、、、、、、、、、、、、、、、、、、、、、、
# #与用户交互
# #输入
# #input()#内容存为字符串
# #int()#只能将纯数字转为整型
# age=input("请输入数字：")
# print(age)
# age=int(age)
# age+=1
# print(age)
# #、、、、、、、、、、、、、、、、、、、、、


# 字符串格式化输出
# %s的用法(位置一一对应，数量也要相等)（可接收任意类型数据）%d只能接收整型
# name="my name is %s" %("cat")
# print(name)
# my="my name is %s,my age is %s" %("cat","20")
# print(my)
# 添加
# 当要输出%时
# a="成功的概率:%s%%"%("99")
# print(a)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 不按位置，以字典形式(有key对应值)
# x = "my name is %(name)s my age is %(age)s" % {"name": "cat", "age": "20"}
# print(x)
# .format()
# 用法(位置一一对应）
# a="my name is {0}{0}{0},my age is {1}" .format("cat","20")#可多次
# print(a)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 不按位置，(有key对应值)
# name = input("名字:")
# age = input("年龄:")
# a = "my name is {name},my age is {age}".format(name=name, age=age)
# print(a)
# 增加
# 当要加括号时
# name = input("名字:")
# age = input("年龄:")
# a = "my name is {{{name}}},my age is {age}".format(name=name, age=age)
# print(a)

# =要添加的是=，<（右对其）当的占位小于20字符时添加=，>左对其，^居中对其
# print("{x:=<20}".format(x="开始执行:"))   #=要添加的是=，<当的占位小于20字符时添加=
# print("{x:=>20}".format(x="开始执行"))
# print("{x:=^20}".format(x="开始执行"))
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 四舍五入
# print("{x:.3f}".format(x=3.1415926535))#(3取三位小数)
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# f的用法
# x=input("请输入你的名字:")
# y=input("请输入你的年龄:")
# z=f"你的名字是:{x}?  你的年龄是:{y}?"
# print(z)
# 增加
# 当要运行f里的东西时
# f"{print(10+3)}"
# 基本运算符
# 1: +,_ *,/
# /(正常除)
# print(10/3)
# //(直接取整数部分)
# print(10//3)
# %(取余数）
# print(10%3)
# **（次方）
# print(10**3)
# 、、、、、、、、、、、、、、、、、、、、、、、
# 比较运算
# 1:>,>=,<,<=,==,!=(不等于)
# ==(等于)，=（赋值）
# !=(判断是否不相等)
# x=2
# y=2
# print(x!=y)
# 、、、、、、、、、、、、、、、、、、、、、、、、
# 赋值运算符
# =（赋值）
# 1:增量赋值（年龄的变化）
# +=（加），/=,%=,**=(简写的意思)
# 1.+=    s=s+x+y等于s+=x+y
# 2./=          同理
# 2.%=           同理
# 2.**=          同理
# 、、、、、、、、、、、、、、、、、、、、、、、、
# 链式赋值
# x=y=z=10
# print(x,y,z)

# x,y,z=1,2,3#(!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
# print(x,y,z)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 交叉赋值（调换值）
# x=1
# y=2
# x,y=y,x
# print(x,y)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 解压赋值(数量要对应)
# a=[1,2,3,4,5]
# x,b,c,d,e,=a
# print(x,b,c,d,e,)
# # 只取前几个
# *_ 不能取中间
# g=[1,2,3,4,5,6,7]
# a,b,c,*_=g #*_去掉后面所有的
# print(a,b,c)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# g=[1,2,3,4,5,6,7]
# *_,a,b,c,=g #*_去掉前面面所有的
# print(a,b,c)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# g=[1,2,3,4,5,6,7]
# a,b,*_,c,=g #*_取两头
# print(a,b,c)
# 、、、、、、、、、、、、、、、、、、、、、


# # 可变类型与不可变类型
# # 可变类型:值改变，id不变，证明改的是原值，证明原值是可以被改变的
# #有:列表，字典（key不可变，value可变）
# # 不可变类型:值改变，id变，证明是产生新的值，没改变原值，证明原值是不可修改的。
# #有：整型，浮点型，字符串，布尔类型
# #赋值操作:与可变不可变没关系
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、


# # #逻辑运算符
# # 显性布尔值
#
# # 隐式布尔值
# # 其中0，None，空（空字符串""，空列表[]，控字典{} ，有空格的不算）代表false，其余都为true
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # not（把紧跟其后的条件结果取反）
# # print(not True)
# # 、、、、、、、、、、、、、、、、、、、、、、、、、
# # and （连结两个条件，都真即为真，都假即为假。）
# # print(1>1 and 2>1)
# # print(2>1 and 3>1)
# # print(4>1and 3>1and 6>1)
# # and 偷懒机制（逐个条件判断，当发现一个条件与前面的不同就不用算了）
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # or （一个为真即为真，全为假才为假）(也有偷懒机制)
# # print(2>1or 3>1or 1>1)
# # 优先级:not>and>or
# # 、、、、、、、、、、、、、、、、、、、、、、、、、
# # 成员运算符
# # in用法
# # 对于字符串，列表 字典，即判断字符串、元素 key是否存在其中
# print("x"in"x y")
# print("t"in "tape player")
# print(111 in[111,222,333])
# print("a"in {"a":111,"b":222})
# # 、、、、、、、、、、、、、、、、、、、、、、、、、
# # not in(不在其中)
# print("t"not in "tape")
# # 、、、、、、、、、、、、、、、、、、、
# # 身份运算符
# # is（判断id是否相等）
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、
# #  流程控制======================================流程控制
# # 1，if判断
# # 语法1:
# # if 条件:
# #     代码1
# #     代码2
# #     代码3
#
# age=20
# is_girl=10
# if age>12and is_girl:
#     print("合格")
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 语法2:
# # if 条件:
# #     代码1
# #     代码2
# #     代码3
# # else:
# #     代码1
# #     代码2
# age=12
# is_girl=True
# if age>15and is_girl :
#     print("合格")
# else:
#     print("不合格")
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 语法3:
# # if 条件1:
# #     代码1
# #     代码2
# #     代码3
# # elif 条件2:
# #     代码1
# #     代码2
# #     代码3
# #     。。。。。。。。。。。
# x=82
# if x>=90:
#     print("优秀")
# elif x>=80:
#     print("良好")
# elif x>=50:
#     print("不及格")
# # 、、、、、、、、、、、、、、、、、、、、、、、、
# # 语法4（最完整）
# # if 条件1:
# #     代码1
# #     代码2
# #     代码3
# # elif 条件2:
# #     代码1
# #     代码2
# #     代码3
# # elif 条件3:
# #     代码1
# #     代码2
# #     代码3
# #     .。。。。。
# # else:
# #     代码1
# #     代码2
# #     代码3
# # # 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # if 嵌套if
# # if 条件1:
# #     代码1
# #     if 条件:
# #        代码1
# #        代码2
# #     代码3
# # elif 条件2:
# #     代码1
# #     代码2
# #     代码3
# # elif 条件3:
# #     代码1
# #     代码2
# #     代码3
# #     .。。。。。
# # else:
# #     代码1
# #     代码2
# #     代码3
# x=94
# if x>=100:
#     print("马上毕业")
# elif x>=90:
#     print("没问题")
#     x+=5
#     if x>=100:
#         print("推迟半年毕业")
#     else:
#         print("推迟一年毕业")
# elif x>=70:
#     print("补考")
# else:
#     print("重修")
# # 、、、、、、、、、、、、、、、、、、、、、、、、
# # 短路运算=偷懒机制 (可能输出隐式布尔值)
# x=10>3and 5and None and 5>2
# print(x)
# # 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # 深浅拷贝
# x=["d",[2,2],"asw"]
# y=x
# x[0]="c"
# print(y)
# # (两个列表不可分开，x变y也跟着变)
# #如何拷贝
# 1 浅拷贝（.copy()）把第一层拷贝
# x=["d",[2,2],"asw"]
# y=x.copy()
# x[0]="c"
# print(y,x)

# x=["d",[2,2],"asw"]# (无法改变容器中的容器的东西，x变y也变)
# y=x.copy()
# x[1][1]=3
# print(y,x)
# # 2 深拷贝，区分可变类型与不可变类型的拷贝要用到（import copy）import导入的意思，中的copy.deepcopy()供能使两个列表完全独立开
# x=["d",[2,2],"asw"]
# import copy
# y=copy.deepcopy(x)
# x[0]="c"
# print(y,x)
#
# x=["d",[2,2],"asw"]
# import copy
# y=copy.deepcopy(x)
# x[1][1]=3
# print(y,x)
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# # while循环============================================================while循环
# # 语法
# # while 条件:
# #     代码1
# #     代码2
# #     代码3
# # 基本使用
# x=1
# while x<5:
#     print(x)
#     x+=1
# print("完成")
# #、、、、、、、、、、、、、、、、、、、、、、、、
# #死循环
# # # # # # # while True:
# # # # # # #    print(186)
# #while循环的应用（账号密码）
# username="999"
# x="123"
# while 1:
#     inp_name=input("请输入账号:")
#     inp_x=input("请输入密码:")
#     if inp_name ==username and inp_x==x:
#         print("{d:=<40}".format(d="登陆成功:"))
#     else:
#         print("登陆失败")
# #退出循环的方法
# #方法1条件为假
# username="999"
# x="123"
# s=10
# while s:
#     inp_name=input("请输入账号:")
#     inp_x=input("请输入密码:")
#     if inp_name ==username and inp_x==x:
#         print("{d:=^40}".format(d="登陆成功:"))
#         s=[]
#     else:
#         print("登陆失败")
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# #方法2加break (运行到break就停止运行)
# username="999"
# x="123"
# s=10
# while s:
#     inp_name=input("请输入账号:")
#     inp_x=input("请输入密码:")
#     if inp_name ==username and inp_x==x:
#         print("{d:=^40}".format(d="登陆成功:"))
#         break
#     else:
#         print("登陆失败")
#     print("{g:=^40}".format(g="结束"))#(不会运行了)
# #、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# #while嵌套
# #1.break 不适用，方法1适用(加了个限制次数)
# username="999"
# x="123"
# s=10
# u=1
# while s and u<=3:
#     inp_name=input("请输入账号:")
#     inp_x=input("请输入密码:")
#     if inp_name ==username and inp_x==x:
#         print("{d:=^40}".format(d="登陆成功:"))
#         while s:
#             q=input("请输入命令:")
#             if q=="w":
#                 s =[]
#             else:
#                 print("运行中")
#     else:
#         print("登陆失败")
#         print("{g:=^40}".format(g="结束"))
#         if u==1:
#             print("你还有两次机会")
#         elif u ==2:
#             print("你还有一次机会")
#         else:
#             print("请24小时后再试")
#         u+=1
# #方法3
# #加continue(结束本次循环，直接进入第二次循环)
# #比如打印1至6但不打印5
# #死循环加与continue同级的代码毫无意义
# a =1
# while a<7:
#     if a==5:
#         continue
#     print(a)
#     a+=1
# #改进
# a =1
# while a<7:
#     if a==5:
#         a+=1
#         continue
#     print(a)
#     a+=1
#  #、、、、、、、、、、、、、、、、、、、、、、、
# while+else(else运行条件 在while循环正常运行的情况下
# 即不被break打断时 才可运行)
# 针对break  案例 输错三次退出程序
# user = "w"
# e = "1"
# a = 0
# q = 10
# while q:
#     if a == 3:
#         print("输入次数过多")
#         break
#     uu = input("账号")
#     ee = input("密码")
#     if uu == user and ee == e:
#         print("{r:=^40}".format(r="登陆成功"))
#     else:
#         print("账号或密码错误")
#         a += 1
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 优化
# user = "w"
# e = "1"
# a = 0
# while a<3:
#     uu = input("账号")
#     ee = input("密码")
#     if uu == user and ee == e:
#         print("{r:=^40}".format(r="登陆成功"))
#         while True:
#             p=input("输入命令")
#             if p=="e":
#                 break
#             else:
#                 print("正在运行")
#         break
#     else:
#         print("账号或密码错误")
#         a += 1
# else:
#     print("输错三次停止")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# for循环
# 语法
# for 变量名 in 可迭代对象(列表 字典 字符串 元组 集合):
#     代码1
#     代码2
#     代码3
#     ...
# 1.循环取值
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for s in a:
#     print(s)
# # while
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # i=0
# while i<3:
#     print(a[i])
#     i+=1
# 、、、、、、、、、、、、、、、、、、、、、、、、
# 字典
# a ={"k":1,"k1":2,"k3":3}
# for x in a:
#     print(x)
#     print(a[x])
# 字符串、
# a="question want"
# for g in a:
#     print(g)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# range（循环次数）
# for+range
# for a in range(10):
#     print("{s:=^80}".format(s="刷新中"))
# 加入、、、、、、、在for中break continue else 和while中的一样、、、、、、、、、、、、、、、、、、、、、、、、、
# user = "w"
# e = "1"
# for i in range(3):
#     uu = input("账号")
#     ee = input("密码")
#     if uu == user and ee == e:
#         print("{r:=^40}".format(r="登陆成功"))
#         while True:
#             p=input("输入命令")
#             if p=="e":
#                 break
#             else:
#                 print("正在运行")
#         break
#     else:
#         print("账号或密码错误")
# else:
#     print("输错三次停止")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# for+continue
# for i in range(9):
#     if i==5:
#         continue
#     print(i)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# for 嵌套
# for i in range(3):
#     print("外层")
#     for i in range(3):
#         print("内层")
# 终止for循环只能用break 想终止那一层加在那一层
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# print 换行符end
# print("e",end="")
# print("p")
#
# print("e",end="")
# print("p")
# ////////////////////////////////////////////
# 基本数据类型
# 1.int类型（整型）
# int 可以将纯数字的字符串转为整型
# 进制转化   2进制（0.1）8进制(0-7) 10进制(0-9) 16进制(0-9)(a-f)
# 1 10进制转2进制（bin）前缀0b代表2进制
# print(bin(10))
# 10进制转8进制(oct)前缀0o代表8进制
# print(oct(10))
# 10进制转16进制((hex))前缀0x代表16进制
# print(hex(10))
# 、、、、、、、、、、、、、、、、、、、、、、、
# 2进制转10 8 16 进制用int
# print(int("0b011", 2))  # 2代表进制(下同)
# print(int("0o10",8))
# print(int("0x10",16))
# 、、、、、、、、、、、、、、、、、、、、、
# float类型（浮点型）
# 类型转换（float）
# a="3.14125"
# a=float(a)
# print(a)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 字符串str（）可以把任何类型转为字符串
# 1.可按索引取值 正取 反取（没有—1）只能取不能改
# a="question"
# print(a[0])
# 2.切片——从一个大的字符串中拷贝出一个子字符串__取值顾头不顾尾
# a="question"
# b=a[0:5]
# print(a)
# print(b)
# 有步长:
# a="question"
# b=a[0:4:2]#0 2 (4取不到)
# print(a)
# print(b)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 长度len
# a="trousers"
# print(len(a))
# 移除空白strip   只能去两边不能去中间
# a="     trousers     shorts      "
# b=a.strip()#括号不加东西默认去除两头空白 要去除啥加上“啥”可以多个
# print(b)
# c="****trousers*******"
# d=c.strip("*")
# print(d)
# 应用 多输入空格
# username="w"
# a="1"
# user=input("账号:").strip()
# b=input("密码:").strip()
# if user==username and a==b:
#     print("登陆成功")
# else:
#     print("账号或密码错误")
# 、、、、、、、、、、、、、、、、、、、、、、、、、
# 切分 split 把一个字符串按某种分隔符进行切分得到一个列表
# a="question shorts trousers"
# b=a.split()# 默认分隔符为空格
# print(b)
# 指定分隔 在括号里加"啥"
# a="question:shorts:trousers"
# b=a.split(":")
# print(b)
# 指定分割次数(无用)
# a="question:shorts:trousers"
# b=a.split(":",1)
# print(b)
# /////////////////字符串需要掌握////////////////////
# 1.strip 去两头空格  l strip 去左边的 r strip 去右边的
# lower 改为小写 upper 改为大写
# a="QUESTION  trousers"
# print(a.lower() )
# print(a.upper())
# 2.startswith 以什么为开头 endswith 以什么为结尾
# print("trousers have question".startswith("trousers"))
# print("trousers have question".endswith("question"))
# 3.split 从左往右切 rsplit 从右往左切  区别在于有次数的时候
# a="trousers:have:question"
# print(a.split(":",1))
# print(a.rsplit(":",1))
# ///////////////////////////////////
# join 把列表拼接为字符串 按某个分割符 将元素全为字符串的列表拼接成一个字符串
# a=["question","shorts","trousers"]
# b=":".join(a)
# print(b)
# 替换 replace （"要替换的"，"替换为"，替换次数）
# a="question shorts trousers shorts"
# b=a.replace("shorts","healthy",2)
# print(b)
# 判断 isdigit 判断字符串是否由纯数字组成
# a="131654986554654"
# print(a.isdigit())
# 应用
# age=input("请输入你的年龄:").strip()
# if age.isdigit():
#     age=int(age)
#     if age>18:
#         print("年龄太大")
#     elif age<18:
#         print("年龄太小")
#     else:
#         print("符合标准")
# else:
#     print("请输入年龄")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 列表
# 类型转化 但凡能够被for循环遍历的类型都可以当作参数传给list()转成列表()
# a="relaxing"
# b=list(a)
# print(b)
# c={"k1":1,"k2":2,"k3":3}
# d=list(c)
# print(d)
# 内置方法
# 1.可以取值 该值
# 2.追加append 加在最后
# a=[1,2,3]
# a.append(4)
# print(a)
# 插入值 insert（）
# a=[1,2,3]
# a.insert(1,1.1) #在索引1前加1.1
# print(a)
# 列表组合 多个值组合 extend
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)
# a=[1,2,3]
# a.extend("abc")
# print(a)0
# 删除
# 1.del 通用
# a=[1,2,3]
# del a[0]#不支持赋值
# print(a)
# 2.pop 根据索引删 不指定默认删除最后一个 会返回删除的值
# a=[1,2,3]
# x=a.pop()
# print(a)
# print(x)
# 3.remove 根据元素删 无返回值
# a=[1,2,3]
# a.remove(1)
# print(a)
# 切片 顾头不顾尾 有不长
# a=[1,2,3,4,5,6,7,8,9]
# print(a[0:8:2])
# 把列表倒过来
# a=[1,2,3]
# print(a[::-1])
# 长度len
# a=[1,2,3]
# print(len(a))
# for 循环
# a=[1,2,3,4,5,6,"skirt"]
# for x in a:
#     print(x)
# 统计个数 count 统计某个东西出现的次数
# a=[1,2,2,2,2,3,3,3]
# print(a.count(2))
# 查找索引 index 返回找到的第一个索引 找不到报错
# a=[1,2,2,2,2,3,3,3]
# print(a.index(2))
# 清空列表 clear 括号无参数
# a=[1,2,2,2,2,3,3,3]
# a.clear()
# print(a)
# 把列表倒过来 不是排序 reverse 无参数
# a=[1,2,2,2,2,3,3,3]
# a.reverse()
# print(a)
# 排序 sort只能对同种类型排序  默认为升序(小到大) 降序（大到小）加reverse=True
# a=[1,2,3,5,7,9,2,4,6]
# a.sort()
# print(a)
# a=[1,2,3,5,7,9,2,4,6]
# a.sort(reverse=True)
# print(a)
# 、、、、、、、、、、、、、、、、
# 队列 先进先出
# 入队操作
# a=[]
# a.append(1)
# a.append(2)
# a.append(3)
# print(a)
# #出队操作
# a.pop(0)
# a.pop(0)
# a.pop(0)
# print(a)
# 堆栈 后进先出
# 入栈操作
# a=[]
# a.append(1)
# a.append(2)
# a.append(3)
# print(a)
# # 出栈操作
# a.pop()
# a.pop()
# a.pop()
# print(a)
# ///////////////////////////////////
# 元组 tuple是不可变的列表(内存地址不变)与浅拷贝一样
# 作用:只存和取不可改
# 定义:在小括号内用逗号分开多个不同类型的元素
# a=(1,"skirt",3,4,5)
# 注意: 如果只有一个元素 必须逗号
# a=(1,)
# 类型转化tuple
# a="skirt"
# b=[1,2,3,4]
# c={"k1":1,"k2":2}
# print(tuple(a))
# print(tuple(b))
# print(tuple(c))
# 内置方法
# 1.按索引取值 正向取反向取
# 2.切片 顾头不顾尾 有步长
# a=(1,2,3,4,6)
# print(a[0:4])
# # 倒过来
# print(a[::-1])
# 3.长度len
# a=(1,2,3,4,6)
# print(len(a))
# 成员运算 in,not in
# 4.循环
# a=(1,2,3,4,6)
# for x in a:
#     print(x)
# 5.index 查索引 返回找到的第一个索引 找不到报错
# a=(1,2,3,4,6,6,4,4,4,)
# print(a.index(4))
# 6.统计元素个数 count
# a=(1,2,3,4,6,6,4,4,4,)
# print(a.count(4))
# ////////////////////////////////////////////////////
# ////////////////////////////////////////////////////
# 字典类型
# 定义字典
# 1.直接定义
# 2.dict造字典
# a=dict(x=1,y=2,z=3)
# print(a)
# a={}默认定义空字典
# 类型转化
# 1.循环造
# a=[["name","韦业"],("age",16),["girl","skirt"]]
# b={}
# for x,y in a:
#     b[x]=y
# print(b)
# 2.dict 简单一点 必须有两个值
# a=[["name","韦业"],("age",16),["girl","skirt"]]
# b=dict(a)
# print(b)
# 3. 列表内的为ker 值为None
# ker = ["name","age"]
# a={}
# for k in ker:
#     a[k]=None
# print(a)
# 4..fromkeys  要同种类型的
# a=[1,2,3,4,5,]
# a={}.fromkeys(a,None)
# print(a)
# 内置方法
# 1.取值 可存 可取 可改
# a={"k1":1,"k2":2}
# print("k1")
# a["k2"]=10
# a["k3"]=45# 当ker不存在时创建key
# print(a)
# 2.长度len
# 3.成员运算 in not in 只定key
# 删除
# 1.通用删除法 del
# a={"k1":1,"k2":2}
# del a["k1"]
# print(a)
# 2.pop 根据ker删除 返回删除key的对应值
# a={"k1":1,"k2":2}
# b=a.pop("k1")
# print(a)
# print(b)
# 3.popitem 删除 随机删除 返回一个元组（删除的key:value）
# a={"k1":1,"k2":2}
# b=a.popitem()
# print(a)
# print(b)
# for循环 keys 取key
# a={"k1":1,"k2":2}
# for x in a.keys():
#     print(x)
# 直接用for循环取key
# a={"k1":1,"k2":2}
# for b in a:
#     print(b)
# 取ker 和value 用items
# a={"k1":1,"k2":2}
# for x,y in a.items():
#     print(x,y)
# 用list 代替for实现以上三种方法
# a={"k1":1,"k2":2}
# print(list(a.keys()))
# print(list(a.values()))
# print(list(a.items()))
# //////////////////////
# 其他内置方法
# clear 清空字典
# a={"k1":1,"k2":2}
# a.clear()
# print(a)
# update 更新字典 用一个新字典去更新就旧字典  旧的没有的会加上去 一切以新字典的为尊准 不可用于赋值
# a={"k1":1,"k2":2}
# b={"b1":3,"b2":4}
# a.update(b)
# print(a)
# get 取值 key不存在不报错 返回None
# a={"k1":1,"k2":2}
# # #print(a["k3"])#key不存在报错 不推荐使用、、、、、、、、、、、、、、、、、、、、
# print(a.get("k3"))
# setdefault 判断key是否存在 不存在则加上 会返回字典中key对应的值
# a={"name":"韦"}
# a.setdefault("age",10)
# print(a)
# # if判断复杂实现
# a={"name":"韦"}
# if "name" in a:
#     ...#(占位符啥都不干与pass等效)
# else:
#     a["age"]=10
#     print(a)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 集合类型 用途 关系运算 去重（有局限性）
# 集合当做一个整体来用
# 定义 {}内用逗号隔开多个元素，元素满足以下条件
# 1.集合内元素必须为不可变类型
# 2.集合内元素无序
# 3.集合内元素不可重复
# 定义空集合
# a=set()
# print(a,type(a))
# 类型转换set
# 转换的东西不能存在子列表......
# a="apples"#去重表现 相同的只保留一个
# b=set(a)
# print(b)
# 内置方法
# 求交集  &   还有intersection
# a={1,2,3,4,5,6,7,8}
# b={"a","b",1,2,3,4,6}
# c=a&b
# print(c)
# print(a.intersection(b))
# 求并集  |   还有  union
# a={1,2,3,4,5,6,7,8}
# b={"a","b",1,2,3,4,6}
# c=a|b
# print(c)
#  取差集   取a中独有的 -   还有difference
# a={1,2,3,4,5,6,7,8}
# b={"a","b",1,2,3,4,6}
# c=a-b
# print(c)
#  对称差集 ^  求两个集合所独有的元素 （即去掉共有的）  还有symmetric_difference
# a={1,2,3,4,5,6,7,8}
# b={"a","b",1,2,3,4,6}
# c=a^b
# print(c)
# 父子集 包含关系 等于互为父子  大的叫爹  还有issuperset大于 issubset 小于
# a={1,2,3,4}
# b={1,2,}
# print(a>b)
# 去重局限性 一般不会用集合去重
# 1.只能针对不可变类型
# 2.无法保证原来的顺序
# 其他去重法
# a=[{"你":"吃饭","age":10},
#    {"你":"吃饭","age":10},
#    {"我":"睡觉","age":18},
#    {"它":"吃饭","age":10}]
# b=[]
# for x in a:
#    if x not in b:
#       b.append(x)
# print(b)
# //////////////////////////////////
# 长度len
# 成员运算in not in
# for循环
# 其他内置方法
# discard 删除 删除不存在的元素不报错
# a={1,2,3}
# a.discard(3)
# print(a)
# a.discard(5)
# print(a)
# update 更新  更新老集合去重得到新集合
# a={1,2,3}
# a.update({1,5,6,9,3})
# print(a)
# pop 删除  随机删除   有返回值
# a={1,2,3,4,5,6,7,8,9}
# b=a.pop()
# print(a)
# print(b)
# add 添加单个元素
# a={1,2,3}
# b=a.add(4)
# print(a)
# print(b)
# 总结
# 只能存一个值（可称标量/原子类型）:数字 字符串
# 可存多个值（容器类型）:列表 元组 字典
# 直接访问(可通过变量名访问整个值):数字
# 顺序访问（通过索引访问指定值 索引代表顺序 又称序列类型）:字符串 列表 元组
# key访问 （通过key访问指定放额值 又称映射类型）:字典
# 可变类型 列表 字典
# 不可变类型 数字 字符串 元组
# /////////////////////////////////////////////////
# ///////////////////////////////////////////////////
#              字符---------------内存-------------unicode格式（只可以改存入硬盘的格式）
#                                                     |
#                                                   io延迟（写入硬盘的速度）
#                                                     |
#                                                   utf_8
#                                                     |
#                                                     |
#                                                    硬盘
# =====================文件基础=================
# 乱码问题解决方法
# 1.存乱 编码格式应设置成支持文件内字符串的格式
# 2.取乱 文件以什么编码格式存入硬盘 就以什么编码格式读取
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 指定文件头修改默认编码（读文件）
# 在py文件的首行写:#coding:编码格式（和文件存时用的编码一样）
# python2 默认编码 ASCII
# python3 默认编码 utf-8
# 第三阶段不乱码
# python3 啥都不用做
# python2 字符串要加u
# a = u"wei"
# ////////////////////////////////
# # 编码解码
# # 编码 unicode 转为其他编码
# # 解码 其他编码转为unicode
# # python转编码无语法 .encode
# # 写文件用utf-8存 不乱码
# # 在主文件加# coding:utf-8 就行
# ///////////////////////////////////////////
# ///////////////////////////////////////////
# ===============文件处理====文件处理===========
# ===============文件处理====文件处理===========
# ///////////////////////////////////////////
# ///////////////////////////////////////////
# 用户/应用程序========直接======文件=======直接========硬盘
#      |                                             |
#      |                                             |
#      —————————————————--------间接------------------|
# 1.如何使用文件:open()
# 控制文件读写内容的模式: t和b
#                 强调:t和b不能单独使用，必须与r/w/a连用
# t 文本 （默认的模式）
#     1.读写都以字符串（str/unicode）为单位
#     2.只针对文本文件
#     3.必须指定:encoding="utf-8"
# 文件操作基本流程
# with open(r'D:\应用\代码位置\新代码位置\文件\a.txt',mode='rt',encoding='utf-8') as b:
#   mode='rt'  encoding='utf-8
#       |              |
#       |              |
#       |              |
#    指定模式            |
#    指定模式            |
#    指定模式            |
#                      |
#                      |
#                      |
#                   指定字符编码


# 1.打开文件
# #open(r'那个盘:\文件路径\文件路...')or open('那个盘:/文件路径/文件路径...')
# x = open('D:/应用/代码位置/新代码位置/文件/bb.txt',mode='rt',encoding='utf-8')
# print(x)
# # 2.操作文件 读/写文件
# a=x.read()
# print(a)
# 3.关闭文件
# x.close()
# ========== with 语法操作文件 它会自动调用close
# with open(r'D:\应用\代码位置\新代码位置\文件\a.txt', mode='rt', encoding='utf-8') as b:  # as b 即b=
#     c = b.read()#t模式会将b.read()读出的结果解码成unicode
#     print(c)
# with 多开
# with open(r'路径', mode='rt', encoding='utf-8') as b:,open(r'路径', mode='rt', encoding='utf-8') as h:........
# “”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“
# 以t模式为基础进行内存操作
# 1.r模式 read （默认的操作模式）:只读模式，当文件不存在时会报错 当文件存在时文件指针跳到开始位置
# with open(r'D:\应用\代码位置\新代码位置\文件\a.txt', mode='rt', encoding='utf-8') as b:
#     c = b.read()  # 把所有文件读到内存 不适用于较大文件
#     print(c)
# 对以前学过的改进==========案例
# user = input("你的账号:").strip()  # 防止多输入空格
# age = input("你的密码:").strip()
# with open(r'D:\应用\代码位置\新代码位置\文件\用户信息.txt') as ten:  # 从文件中取出用户信息
#     for L in ten:  # for循环读出文件的每一行
#         username, number = L.strip().split(":")  # strip()去除\n split(":")以:切分
#         if username == user and number == age:
#             print("登陆成功")
#             break
#     else:  # 不放在if中
#         print("账号或密码错误")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# w 模式(用于创建新文件) write 只写模式 当文件不存在时会创建 文件存在时会清空文件（数据全没 不要用重要文件尝试），指针位于开始位置
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt",mode="wt",encoding="utf-8") as w:
#     w.write("开始")
# =====注意1=====在以w模式打开文件没有关闭的情况下，连续写入，新的内容会跟在就内容后
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt",mode="wt",encoding="utf-8") as w:
#     w.write("你")
#     w.write("我")
#     w.write("她")
# ======注意2======如果重新以w模式打开文件，则会清空文件内容
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="wt", encoding="utf-8") as w:
#     w.write("你")
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="wt", encoding="utf-8") as w:
#     w.write("我")
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="wt", encoding="utf-8") as w:
#     w.write("她")

# 案====================================================================例 文件拷贝 针对文本文件
# q=input("要复制的的文件的文件路径:").strip()
# w=input("要粘贴的的文件的文件路径:").strip()
# with open (r"{}".format(q),mode="rt",encoding="utf-8") as a,\
#         open(r"{}".format(w),mode="wt",encoding="utf-8") as b:
#     c=a.read()  # 读取数据过大内存会爆满
#     b.write(c)
# =====================改进
# q=input("要复制的的文件的文件路径:").strip()
# w=input("要粘贴的的文件的文件路径:").strip()
# with open (r"{}".format(q),mode="rt",encoding="utf-8") as a,\
#         open(r"{}".format(w),mode="wt",encoding="utf-8") as b:
#     for p in a:  # 省空间
#         b.write(p)
# print("复制成功")
# //////////////////////////////////////////////////////////
# a 模式（用于对旧文件追加写 比如日志，注册功能） 只追加写模式 （不关闭文件情况下与w模式不关是一样的）， 当文件不存在时会创建空文件，当文件文件存在时指针会跳到最末尾
# with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="at", encoding="utf-8") as w:
#     w.write("你 question")
# ======注册功能=======
# W = 0
# c = True
# while W <= 1 and c:
#     user = input("你的账号:")
#     age = input("你的密码:")
#     with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="rt", encoding="utf-8") as p:
#         for L in p:  # for循环读出文件的每一行
#             username, number = L.strip().split(":")  # strip()去除\n split(":")以:切分
#             if username == user and number == age:
#                 print("该用户已注册过")
#                 W += 1
#                 print("你还有一次机会")
#                 break
#         else:
#             with open(r"D:\应用\代码位置\新代码位置\文件\bb.txt", mode="at", encoding="utf-8") as w:
#                 w.write("{}:{}\n".format(user, age))  # \n换行
#                 print("注册成功")
#                 c = False
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# b模式 通用模式 （控制文件读写内容的模式）（不做转换是啥模式就是啥模式）
# 1.不可指定字符编码（读写都以bytes为单位---二进制）
# 2.什么都可以读
# 3.需要手动编码解码
# ==========================拷贝工具（通用拷贝）
# x = input("源文件路径：").strip()
# n = input("要复制到的路径：").strip()
# with open(r'{}'.format(x), mode='rb') as f1, \
#         open(r'{}'.format(n), mode='wb') as f2:
#     for p in f1:  # (不占用内存)（也有局限性，当一行过长时）
#         f2.write(p)
# print("复制成功")
# /.................../././、、、、、、、#。。。for循环处改进。。。。
# 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
# x = input("要拷贝的文件路径：").strip()
# n = input("要复制到的路径：").strip()
# with open(r'{}'.format(x), mode='rb') as f1, \
#         open(r'{}'.format(n), mode='wb') as f2:
#     while True:
#         res = f1.read(1)  # 自定单次读入字节
#         f2.write(res)
#         if len(res) == 0:
#             break
# print("复制成功")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 文件指针移动 seek
# 1.指针移动的单位都是以bytes（字节）为单位（特殊:t模式下read（n）n代表字符个数）
# 语法
# .seek(n,模式) # n指移动的字节个数
# 模式
# # 0:参照物为文件开头
# .seek(2,0)
# # 1:参照物为当前指针所在位置
# .seek(2,1)
# # 2:参照物为文件末尾（要倒着移动，要为负数）
# .seek(-2,2)
# 、、强调 只有0模式可以在t模式下使用 1 2必须在b模式下使用
# 、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、 .tell() #  获取文件指针当前位置
# with open('a.txt',mode='rb') as a:
#     a.seek(24,1)
#     # print(a.tell())
#     print(a.read().decode('utf-8')) #  解码
# 案例（日志）(与备用环境代码同时使用)
# import time  # 让循环休息一段时间
# with open('a.txt', mode='rb') as b:
#     b.seek(0, 2)  # 将指针跳转到末尾 0不跳动位置
#     while True:
#         a = b.readline()  # 读一行
#         if len(a) == 0:  # 判断是否添加了东西
#             time.sleep(0.5)
#         else:
#             print(a)
#             print(a.decode('utf-8'))  # 解码
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 文件修改的两种方式
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 函数
# 先定义再调用
# 1.定义函数
# 语法
# def 函数名（参数1，参数2.。。。。。）:  #必须有
#      """"函数描述"""
#      函数体  #  必须有
#      return（值）
# ///////////////////////////////
# 定义函数发生的事
# 1.申请内存空间保存函数体代码
# 2.将函数体内存地址绑定函数名
# 3.定义时不运行函数体代码 但会检测语法
# 、、、、、、、、、、、、、、、、、、、、、、、、、、
# 定义函数的三种形式
# 1（无参函数）
# def time():
#     print("开始")

# 2.（有参函数）
# def trip(x,y):
#     print(x,y)

# 3.空函数(函数体代码为pass)
# def test():
#     pass
# 、、、、、、、、、、、、、、、、、、、
# 调用函数时发生的事
# 1.通过函数名找到函数体内存地址
# 2.然后加括号就是触发代码的运行
# /////////////////////////////////
# 调用函数的三种方式
# 1.语句形式（只调用函数）
# 2.表达式形式(用到返回值)
# def a(x, y):
#     res = x + y
#     return res
# # 赋值表达
# res = a(1, 2)
# print(res)
# # 数学表达
# res=a(1,2)*10
# print(res)
# 3.函数调用可以当作参数
# res=a(a(1,2),10)
# print(res)
# //////////////////////////////
# 函数返回值的三种形式
# 1.None:函数内没有return或者return或者return None
# 2.返回一个值:return 值
# 3.返回多个值:用逗号分隔开多个值，会被return返回为元组
# def a():
#     return 10,"aa",[2,1]
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 函数参数的使用
# 型参与实参
# 1.型参:在定义函数阶段定义的参数 相当于变量名
# 2.实参：在调用函数的阶段传入的值 相当于变量值
# 关系
# 在调用时，实参会绑定形参
# 这种绑定关系只能在函数体内使用
# 实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系
# 实参是个值，有多种形式
# 形式一
# a(2,3)
# 形式二
# a=1
# b=2
# a(a,b)
# 形式三
# a(int("1"),2)   #........(只要结果是个值就可以)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 1.位置参数:从左到右的顺序依次定义的参数
# 1.1位置形参:在函数定义阶段，从左到右的顺序直接定义的“变量名”
# 特点：必须被传值，数量要对应
# def a(x, y):
#     print(x,y)
# 1.2位置实参：在函数调用阶段，按照从左到右的顺序依次传入的值
# 特点：按照顺序与形参一一对应
# def a(1,2):
# def a(2,1):
# 、、、、、、、、、、、、、、、、、、、
# 关键字实参：在函数调用阶段，按照key=value的形式传入的值
# 特点：可以不按照顺序给某个形参传值
# def a(x, y):
#     print(x,y)
# a(y=5,x=8)
# 注意
# 1.、、、混合使用时位置实参必须放在关键字实参前
# 2.不能为同一个形参传多个值
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、默认形参、、、、、、、、、
# 定义： 在定义阶段，就已经被赋值的形参，
# 特点:在调用阶段可以不对其赋值，（意味着如果赋值时结果以赋值为准）
# def foo (x=1,y=3):
#     print(x+y)
# foo()
# 两种形参的混用
# 1.位置形参必须在默认形参的左边
# 2.默认形参的值是在定义阶段被赋值的，也就是被赋予的是内存地址
# 3.默认值可以被指定为任意类型，但是不推荐可变类型
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 可变长度参数（*与**的用法）(类for循环)
# 可变长度指的是在调用函数时，传入的值（实参）的个数不固定
# 1.可变长度的位置参数
# 1.1 *形参名(形参名一般为args（规范）):用于接收溢出的位置实参（*的用法）溢出的位置实参会被*保存为元组的格式，然后赋值给紧跟其后的形参名
# 用途:
# 1.累加
# def k_sum(*args):
#     x=0
#     for y in args:
#         x+=y
#     return x
# x=k_sum(1,2,3,4,5,6,7,8,9)
# print(x)
# 2.*可以用在实参中，实参中带*，*的值会呗被打散为位置实参(打散后的数量要与形参数量一样)
# def foo(x,y,z):
#     print(x,y,z)
# foo(*[11,22,33])
# 3.形参与实参都带*
# def kkk(x,y,*args):
#     print(x,y,args)
# kkk(1,2,*[3,4,5,6])
# //////////////////////////////////////////////////////
# 2.可变长度的关键字参数
# 2.1 **形参名(形参名一般为kwargs（规范）:用于接收溢出的关键字字实参，（**的用法）溢出的位置实参会被**保存为字典的格式，然后赋值给紧跟其后的形参名
# 3.用法
# 1.**可以用在实参中（**后跟的只能是字典），实参中带**，先将**后的值打散为关键之实参（数量要对应，key与形参要一样）
# def ccc(x, y, z):
#     print(x, y, z)
# ccc(**{"x": 1, "y": 2, "z": 3})
# 2.形参实参中都带**
# def vvv(x,y,**kwargs):
#     print(x,y,kwargs)
# vvv(**{"y":1,"x":2,"c":22,"d":66})
# /////////////////////////////////////////
# *与**混用
# *aegs必须在**kwargs之前
# 1.
# def vv(x,*args,**kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
# vv(1,2,3,4,5,6,y=1,z=2,a=5)
# 2.不变互传
# def aa(x, y):
#     print(x, y)
# def bb(*args, **kwargs):
#     aa(*args, **kwargs)  # aa(y=2,x=1)
# bb(y=2, x=1)
# ////////////////////////////////////////////
# 了解(极其少用)
# 1.命名关键字参数(不是位置参数，必须按key=value的形式传值)
# 定义:在定义函数时，*后定义的参数，如下a,b
# def vv(x,y,*,a,b):
#     pass
# vv(1,2,a=4,b=3)
# 2.组合使用（略）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 重点:名称空间:存放名字的地方，是对栈区的划分（可以在栈区中存放相同的名字）
# 名称空间分为三种
# 1.内置名称空间
# 存放的名字:存放python解释器内置的名字
# 存活周期:解释器启动时产生，关闭时销毁

# 2.全局名称空间
# 存放的名字:除函数内定义、内置的名字其他的都为全局 or 运行顶级代码所产生的名字
# 存活周期:运行时产生，结束时销毁

# 3.局部名称空间
# 存放的名字:在调用函数时，运行函数体代码过程中产生的函数内分名字
# 存活周期:在调用函数时产生，调用完毕后销毁
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 名称空间加载顺序
# 内置>全域>局部
# 、、、、、、、、、、、、、、、、、、、、、、、、
# 作用域:作用范围
# 1.全局作用域：内置名称空间，全局名称空间
# 1.全局存活
# 2全局有效：被所有函数共享

# 局部作用域：局部名称空间
# 1.临时存活
# 局部有效：函数内有效
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 函数对象：可以把函数当变量去用
# 1.可以赋值
# def func():
#     print("aa")
# f=func
# print(f,func)
# f()
# 2.可以当作参数
# def func():
#     print("aa")
# def foo(x):
#     print(x)
#     x()
# foo(func)
# 3.可以当作另一个函数的返回值
# def func():
#     print("aa")
# def foo(x):
#     return x
# foo(func)
# 4.当作容器类型的一个元素
# def func():
#     print("aa")
# l=[func,11]
# print(l)
# l[0]()
# dic={"k":func}
# print(dic)
# dic["k"]()
# 小应用
# def aa():
#     print("查询")
#
#
# def bb():
#     print("登录")
#
#
# def cc():
#     print("取款")
#
#
# def dd():
#     print("转账")
#
#
# dictionary = {
#     "0": ['退出', None],
#     "1": ['查询', aa],
#     "2": ['登录', bb],
#     "3": ['取款', cc],
#     "4": ['转账', dd]
# }  # 只读把列表改为元组更好
# while True:
#     for p in dictionary:
#         print(p, dictionary[p][0])
#
#     u = input("请输入命令编号:").strip()
#     if not u.isdigit():
#         print("必须为数字，小牛马")
#         continue
#     if u == "0":
#         break
#     if u in dictionary:
#         dictionary[u][1]()
#     else:
#         print("输入的命令不存在")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 函数嵌套
# 1.函数嵌套调用:在调用一个函数的过程又调用其他函数
# 比较大小
# def q(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def qq(a,b,c,d):
#     res1=q(a,b)
#     res2=q(res1,c)
#     res3=q(res2,d)
#     return res3
#
#
# res=qq(1,2,3,4)
# print(res)
# 2.函数的嵌套定义：在函数内定义其他函数
# 圆形
# def x(u, i=0):
#     g = 3.1415926535
#
#     def l(u):  # 求周长
#         return 2 * g * u
#
#     def c(u):  # 求面积
#         return g * (u ** 2)
#
#     if i == 0:
#         return l(u)
#     elif i == 1:
#         return c(u)
# x(55,1)
# //////////////////////////////////
# 闭包函数
# 闭包函数=名字空间作用域+函数嵌套+函数对象
# 核心点:名字的查找关系是以函数定义阶段为准
# 闭:内嵌函数
# 包:该函数包含对外层函数作用域名字的引用(不是对全局作用域)(f2就是闭包函数)
# 名字空间作用域+函数嵌套引用
# def f1():
#     x=1
#     def f2():
#         print(x)
# 名字空间作用域+函数嵌套+函数对象应用
# def f1():
#     x=1
#     def f2():
#         print(x)
#     return f2
# q=f1()
# print(q)
# 传参的两种方式
# 1.直接传
# import requests
# def too(x):
#     res=requests.get(x)
#     print(res.text)
# w="https://lenovo.ilive.cn/?f=stle"
# too(w)
# 2.用闭包函数
# import requests
# def out(q):
#     def get():
#         z=requests.get(q)
#         print(len(z.text)) # 去len没事
#     return get
#
# baidu=out("https://www.baidu.com/")
# baidu()
# print("======================================================")
#
# lianxiang=out("https://lenovo.ilive.cn/?f=stle")
# lianxiang()
# print("======================================================")
#
# dm=out("http://www.9damaogame.net/")
# dm()
# print("======================================================")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 装饰器
# 啥是装饰器:定义的一个函数或其他，用来装饰其他函数或其他（为其添加额外功能）
# 为什么要有装饰器
# 1.开放封闭原则
# 开放:指拓展功能是开放的
# 封闭:指修改源代码是封闭的
# 作用:在不修改被装饰对象以及调用方式的前提下为其添加新功能
# 示例:计算运行时间
# import time
# def t(x, y, z):
#     time.sleep(3)
#     print("%s====%s=====%s" % (x, y, z))
# def tt(*args, **kwargs):
#     a = time.time()
#     t(*args, **kwargs)
#     b = time.time()
#     print(b - a)
# tt(116, 561, z=5445)
# 改进 真正的装饰器(t原函数，uot装饰器)
# import time
# def t(x, y, z):
#     time.sleep(3)
#     print("%s====%s=====%s" % (x, y, z))
# def out(value):  # value=t的内存地址
#     def tt(*args, **kwargs):
#         a = time.time()
#         value(*args, **kwargs)  #t的内存地址
#         b = time.time()
#         print(b - a)
#     return tt
# t=out(t)  #t=out（t的内存地址），t=当初那个tt函数的内存地址
# t(1,2,3)
# 再优化=============
# import time
# def t(x, y, z):
#     time.sleep(3)
#     print("%s====%s=====%s" % (x, y, z))
# def home(name):
#     time.sleep(2)
#     print("==========================",name)
#     return 888
# def out(value):  # value=t的内存地址
#     def tt(*args, **kwargs):
#         a = time.time()
#         res=value(*args, **kwargs)  #t的内存地址
#         b = time.time()
#         print(b - a)
#         return res
#     return tt
# t=out(t)  #t=out（t的内存地址），t=当初那个tt函数的内存地址
# t(1,2,3)
# home=out(home)
# res=home("T")
# print("返回值=",res)
# 语法糖:偷梁换柱更方便（在被装饰对象正上方的单独一行写@装饰器名字）就无需home=out(home)语句了（用此法装饰器需放在被装饰函数之前）
# import time
# def out(value):  # value=t的内存地址
#     def tt(*args, **kwargs):
#         a = time.time()
#         res=value(*args, **kwargs)  #t的内存地址
#         b = time.time()
#         print(b - a)
#         return res
#     return tt
# @out
# def t(x, y, z):
#     time.sleep(3)
#     print("%s====%s=====%s" % (x, y, z))
#
# @out
# def home(name):
#     time.sleep(2)
#     print("==========================",name)
#     return 888
# t(1,2,3)
# res=home(122)
# print(res)
# 总结:无参装饰器模板
# def out(value):  # value=t的内存地址
#     def tt(*args, **kwargs):
#         res=value(*args, **kwargs)  #t的内存地址
#         return res
#     return tt
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 补充:极致伪装（用模块wraps（form functools import wraps ））（不用没问题）
# from functools import wraps
# def out(value):  # value=t的内存地址
#     @wraps(value)  # value=value
#     def tt(*args, **kwargs):
#         res=value(*args, **kwargs)  #t的内存地址
#         return res
#     return tt
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 有参装饰器（暂略）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 迭代器:指迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一个结果而继续，单纯的重复不是迭代（一种能够不依赖于索引的取值方式，这就是迭代器）
# 1.可迭代对象:内置有__iter__方法的都称为可迭代对象(字符串，列表，元组，字典，文件，集合)
# x=""
# x.__iter__()
# 2.调用可迭代对象的__iter_方法可以得到一个迭代器
# a = {"a": 1, "b": 2, "c": 3}
# dd = a.__iter__()
# print(dd.__next__())  # 迭代器内置方法没每执行一次就可以得到一个返回值
# print(dd.__next__())  # 迭代器内置方法没每执行一次就可以得到一个返回值
# print(dd.__next__())  # 迭代器内置方法没每执行一次就可以得到一个返回值
# print(dd.__next__())  # 抛出异常代表已经取完
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、
# a = {"a": 1, "b": 2, "c": 3}
# dd = a.__iter__()
# while True:
#     try:
#         print(dd.__next__())
#     except StopIteration:  # 捕捉异常
#         break
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 对同一个迭代器取值取干净的情况下，再对其取值娶不到
# 示例 （麻烦）
# a = {"a": 1, "b": 2, "c": 3}
# dd = a.__iter__()
# while True:
#     try:
#         print(dd.__next__())
#     except StopIteration:  # 捕捉异常
#         break
# print("================")
# while True:
#     try:
#         print(dd.__next__())
#     except StopIteration:  # 捕捉异常
#         break
# //////////////////////////////////////////
# for循环与迭代器（迭代器循环）
# 、、、、、、、、、、、、、、、、、、、、
# 生成器（只定义迭代器）
# 1.yield关键字用法
# yield（生成器__next__方法调用才会有用）可以用于返回值，不同于return,函数一遇到yield会保留运行状态，用于多个返回值
# def foo():
#     print("第一次")
#     yield
#     print("第二次")
#     yield
# q=foo()
# x1=q.__next__()
# x2=q.__next__()
# x3=q.__next__() #返回玩会报错（和迭代器一样）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 叠加多个装饰器的加载，运行分析（暂略）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# yield的表达式形式（了解）
# 1.形式一
# def foo(name):
#     print("开始了")
#     while True:
#         x=yield None  # None可以没有
#         print("%s开始了"%(x))
# q=foo("哈哈")
# next(q)#类——next--
# q.send("你妹") #send会将值传给yield（此时yield后的值不会被传）（如果是 q.send(None) 就等于next（q））
# q.send("一同随")
# q.send("开髓")
# q.send("钢结构")
# q.close()#关闭后无法传值（也就是其后面send没用）
# 2.形式二（深入学习==略）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 三元表达式
# 格式:条件成立使要返回的值（可以不是条件包含的东西） if 条件 else 条件不成立时要返回的值（可以不是条件包含的东西）
# x = 1
# y = 2
# res = x if x > y else y  # or res=pear if x>y else milk
# print(res)
# ////////////////////////////////////////////////////
# 列表生成式:要加入列表的值 for 任何东西 in 一个对象 条件(无条件则为True)
# l=[1,2,3,4,5,5,5,5,6,7,8]
# res=[18 for x in l if x==5]
# print(res)
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 字典生成式及其他生成式（略）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 函数递归 :是函数嵌套调用的一种特殊方式（再调用一个函数的过程中又直接或间接调用了函数本身）(最多调用一次)
# 1.直接调用
# import time
# def foo():
#     print("=========")
#     time.sleep(1)
#     foo()
# foo()
# 2.间接调用
# import time
# def foo():
#     print("=========")
#     time.sleep(1)
#     fu()
# def fu():
#     print("///////////")
#     foo()
# foo()
# 递归本质就是循环
# 但是递归不应该无限调用，必须满足一定条件结束
# import time
# def f1(n):
#     if n==100:
#         return
#     time.sleep(1)
#     print(n)
#     n+=1
#     f1(n)
# f1(0)
# /////////////////////////////////
# 递归调用的两个阶段
# 1.回溯:一层一层调用下去
# 2.递推:满足某种结束条件，结束递归调用，然后一层一层返回
# 应用
# l = [1, 8, [2, 3, 4]]
# p = [1, 2, 3, [5], [4],[2]]
# def f1(list):
#     for x in list:
#         if type(x) is list:
#             f1(x)
#         else:
#             print(x)
# f1(p)
# //////////////////////////
# 算法:高效决解问题的方法
# 1.二分法
# 需求:有一个按照从小到大顺序排列的数字列表
# 从中找一个想要的值
# l = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 89, 100, 101, 200]
# x = 100
# def qq(x, l):
#     print(l)
#     if len(l) == 0:
#         print("找的值不存在")
#         return
#     y = len(l) // 2
#     if x > l[y]:  # 接下来的查找应该是列表的右半部分
#         l = l[y + 1:]
#         qq(x, l)
#     elif x < l[y]:  # 接下来的查找应该是列表的左半部分
#         l = l[:y]
#         qq(x, l)
#     else:
#         print("find it")
# qq(x, l)
# /////////////////////////////////////////////////
# 面向过程编程（略）
# 、、、、、、、、、、、、、、、、、、、、
# 函数式
# 1.匿名函数（lambda 用于定义匿名函数）
# 公式:lambda 参数,参数......:字代码 #为了简化所以一行写完
# 用于:临时调用一次的场景:跟多的是将匿名函数与其他函数配合使用
# lambda x,y:x+y
# 匿名函数的一个应用(找出值最大的)
# l={"x":100,
#    "y":90,
#    "w":600,
#    "z":900}
# # max 迭代key 输出最大的key（min与之相反）
# res=max(l,key=lambda k:l[k])
# print(res)
# 、、、、、、、、、、、、、、、、、
# map(映射)，filter 略
# 、、、、、、、、、、、、、、、、、、、、、、、
# 、、、、、、、、、、、、、、、、、、、、、、、、
# 模块
# 1.首次导入模块发生的事（之后的导入都是使用第一次所产生的东西）
# 1.1执行模块
# 1.2申请内存空间（名称空间........）
# 在当前文件中产生的有一个名字模块，该名字指向2中所产生的名称空间
# import导入模块
# 1.可以给模块命名
# 格式: import 模块 as 定义名
# import time as dirty
# dirty.sleep(1)
# print("hb")
# 模块是第一类对象
# 只定义模块应该以纯小写加下划线命名
# 可以在函数中导入模块
# def foo():
#     import time
# /////////////////////////////////////
# from import 导入模块
# 格式: from 主模块 import 模块中的功能
# import在导入模块是使用时必须加前缀（form import 导入就不用这样了）
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 模块查找优先级
# sys模块:（值为一个列表，存放一系列的文件夹，其中第一个文件夹是当前执行文件所在的文件夹）
# 1.内存（内置模块）====硬盘
# import sys
# print(sys.path)
# 查看已经加载到内存中的模块
# import sys
# print(sys.modules)
# 、、、、、、、、、、、、、、、、、、、、、、、、、
# 用sys模块导入其他路径的模块
# import sys
# sys.path.append(r"D:\DDDLLLL")
# import 模块 as a
# print(a)
# 编写模块的规范
# 1.模块的文档描述
# 2.导入模块
# 3.定义变量
# 4.定义类
# 5.定义函数
# 6.主程序
# 函数补充（类型提示）
# 在变量后+:提示信息（写啥都行）
# def x(name:str,age:int,hobbies:tuple)->int:  #(->int:规定返回值)
#     print(name)
#     print(age)
#     print(hobbies)
#     return 111
# x(1,2,(1,2))
# # 查看提示信息用
# print(x.__annotations__)
# /////////////////////////////////
# 包（模块的一种）是一个含有__init__.py的文件夹 被当做模块导入用的
# 1.产生一个名称空间
# 2.导入时是运行包下的__init__.py的文件 将运行时产生的名称空间放入1中
# 3.在当前执行文件的名称空间中拿到一个名字"包:（文件夹名）"文件夹名指向1的名称空间
# 包的使用
# 1.__init__.py的作用:用于导入子模块功能
# 2.__init__.py的用法
#    1.绝对导入，以包的为文件夹为起始进行导入
#      from 包.子模块 import 功能名（写入__init__.py中）
# 相对导入（略）
# ///////////////////////////////////
# 软件开发目录规范
# 文件名（主文件夹）
#       bin文件夹（存放可执行文件）
#       conf文件夹（配置文件夹）
#       db文件夹（数据库文件调用代码）
#       lib文件夹(模块文件夹)
#       core（名称可自定义）文件夹（核心代码）
#       README文件夹(软件解释文件夹（版本解释软件介绍等）)
#       等。。。。。。。
#  ///////////////////////////
# 常用模块学习
# ============1 time模块========
# 时间的三种格式
# 1.时间戳（用于时间间隔计算）:从1970年到现在的秒数
# import time
# print(time.time())
# 2.按照某种格式显示的时间（用于显示时间）:2020-03-30 11:11:11
# import random
import shutil
import sys
import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))#  (Y表示年 m表示月d表示天H表示M表示分钟S表示秒 %为固定格式 其他为自定义格式（注%H:%M:%S=%X）)
# print(time.strftime("%Y年-%m月-%d日 %H时:%M分:%S秒"))
# 3.结构化的时间（用于获取时间的某一部分）
# import time
# res=time.localtime()
# print(res.tm_yday)#  (通过(.要获取的内容）可获取其内容)
# =========datatime模块=========(用于时间的加减)
# 1.#(可直接获取时间)
# import datetime
# res=datetime.datetime.now()
# print(res)
# 2.用于时间的加减
# import datetime
# res=datetime.datetime.now() + datetime.timedelta(days=1) #(参数很多)
# print(res)
# ///////////////////////////////////
# 时间格式之间的转化
# 时间戳===转===结构化的时间===转===按照某种格式显示的时间 或 按照某种格式显示的时间===转===结构化的时间===转===时间戳
# 格《=== ==strftime=====结《=======localtime======时
# 式--------------------构-----------------------间
# 化=======strptime====》化========mktime========》戳
# import time
# #  1结构化的时间===转===时间戳
# res=time.localtime()
# x=time.mktime(res)
# print(x)
# # 2.时间戳===转===结构化的时间
# r=time.time()
# p=time.localtime(r)
# print(p)
# # 3.结构化的时间===转===按照某种格式显示的时间
# e=time.localtime()
# s=time.strftime("%Y-%m-%d %X",e)
# print(s)
# # 4.0按照某种格式显示的时间===转===结构化的时间
# j="2022-07-30 10:15:22"
# q=time.strptime(j,"%Y-%m-%d %X")#  制表符要一样
# print(q)
# # 其他
# # 1.time.sleep()#  延迟
# ////////////////////////////////////////
# ============2 random模块（随机模块）========
# w=random.random()#  得到的只能是0和1之间的浮点数
# print(w)
# # 2.可指定范围
# res=random.randint(1,3)#  有区间限制[,]只能取整数
# print(res)
# 3random.randrange有区间限制[,)
# 4 random.choice 自定义（）里可自定义任何格式
# 5 random.sample自定义列表元素随机配
# print(random.sample(["韦","玉","婷","尾","语","停"],3))#3为指定随机数量
# print(random.sample(["哈","宝","刚","刚","臭","婷","玉","米","粒"],3))
# random.uniform自定义区间（闭区间）内取随机浮点数
# print(random.uniform(3,6))
# 6 洗牌（打乱顺序）
# x=[1,2,3,4,5,6,7,8,9]
# random.shuffle(x)
# print(x)
# random综合应用：验证码
# 前提（chr函数65-90分别代表26个大写字母）
# import random
# res=""#空列表
# for i in range(4):#循环次数
#     z=chr(random.randint(65,90))#从26个大写字母中随机取一个
#     s=str(random.randint(0,9))#str转为字符串方便后面加减 从10个数字中随机取一个
#     res+=random.choice([z,s])#从筛选中再筛选其中一个
# print(res)
# //////////////////////////////////
# # ============3 os模块（系统控制模块）========
# import os


# # 1 os.getcwd获取当前文件路径
# print(os.getcwd())
# # 2 os.makedirs创建多级文件目录
# os.makedirs("D:/A/o/u/l")#注意斜杠
# # 3 os.mkdir创建一个文件夹
# os.mkdir("D:/q")
# # 4 os.listdir()获取文件夹中所有文件目录包括隐藏文件
# res=os.listdir("D:/")
# print(res)
# 5 os.path.getsize获取文件大小
# c=os.path.getsize("D:/")
# print(c)
# 6 os.remove()删除一个文件
# import shutil
# shutil.rmtree("D:/q")#(访问权限好)
# os.mkdir("D:/q")
# print("创建成功")
# os.remove("D:/q")
# print("已删除")
# 7 os.system()#执行系统命令
# 8 os.environ #获取系统环境变量
# ////////////////////////////////////////////
# ============4 sys模块（模块）========
#  1 sys.path#反回模块的收索路径
# ////////////////////////////////////////////
# 打印进度条
# import time
# 当前下载量 = 0
# 总下载量 = 102400
# while 当前下载量 < 总下载量:
#     time.sleep(0.01)  # 假设下载了1024
#     当前下载量 += 1024
#     # 打印进度条
#     数值 = 当前下载量/总下载量
#     if 数值 > 1:  # bug修复
#         数值 = 1  # bug修复
#     进度条 = int(100*数值) * "="  # int是取整100是打印长度>是打印字符
#     print("\r[%-100s] %d%%" % (进度条, int(100*数值)), end="")
    #  \r是跳到开头打印，-是左对其，100是长度，%%是输出一个%，int是取整，100是百分比，end=""是不换行答应
# 做成函数调用（优化）
# def 进度条(数值):
#     if 数值 > 1:  # bug修复
#         数值 = 1  # bug修复
#     进度条 = int(100*数值) * "="  # int是取整100是打印长度>是打印字符
#     print("\r[%-100s] %d%%" % (进度条, int(100*数值)), end="")
# import time
# 当前下载量 = 0
# 总下载量 = 102400
# while 当前下载量 < 总下载量:
#     time.sleep(0.01)  # 假设下载了1024
#     当前下载量 += 1024
#     数值 = 当前下载量 / 总下载量
#     进度条(数值)
# /////////////////////////////////
# ============4 shutil模块（模块）========后面前缀shutil省略
# 1 shutil.copyfileobj(open("要拷贝的文件","r"),open("要被拷贝到的文件","w"))将文件内容拷贝到另一个文件中
# 2 copyfile("文件路径”，“文件路径”)目标文件可以不存在
# ////////////////////////////////////
# 序列化与反序列化
# 序列化是把内存的数据类型转换为一种特定的格式，可用于储存（存档一般用pickle）或传输给其他平台（跨平台交互用json）
# 内存数据=====序列化======（json（通用格式）或pickle格式）
# （json或pickle格式）====反序列化====内存数据
# 1 json.dumps序列化  json.loads反序列化
# import json
# w=[1,2,3,4,"5","开始"]
# q=json.dumps(w)
# print(q)
# # 储存
# with open ("序列化.txt",mode="wt",encoding="utf-8") as f:
#     f.write(q)
# # 读
# with open ("序列化.txt",mode="rt",encoding="utf-8") as f:
#     k=f.read()
# # 反序列化
# l=json.loads(k)
# print(l)
# ======================简化代码(dump和load)=================
# import json
# w=[1,2,3,4,"5","开始"]
# # 序列化与储存
# with open ("序列化.txt",mode="wt",encoding="utf-8") as f:
#     json.dump(w,f)
# # 反序列化与读
# with open ("序列化.txt",mode="rt",encoding="utf-8") as f:
#     l=json.load(f)
#     print(l)
# json兼容通用类型 但是一些语言的特有类型不可转化
# //////////////////////////////////////
# ============ confiqparser模块（加载特定格式的配置文件）========（略）
# ============hashlib模块（可用于密码加密，文件校验）========
# 是一类算法，接受内容，经过运算得到一串hash值
# hash值特点
#           1只要传入的内容一样，得到的hash值一定一样
#           2不能由hash值反解成内容
#           3只要使用的hash算法不变，无论内容多大，得到的hash值长度是固定的
# 1 密码加密（盐）
# import hashlib
# x=hashlib.md5()  # 调用算法md5()还有其他算法等
# x.update("111".encode("utf-8"))  # "111"加密内容 encode("utf-8" 因为必须为拜齿类型
# x.update("print".encode("utf-8"))
# res=x.hexdigest()  # 获取hash值(结果为"111"与"print"的hash值合并)
# print(res)
# 2 文件校验(略)
# /////////////////////////////////
# 撞库(破译加密密码)（略）
# 密码加盐（提升撞库成本）
# 1 将密码与安全码一起转为hash值
# //////////////////////////////
# ============3 logging模块（日志模块）========
# import logging      # 级别debug=10，info=20 warning=30 error=40 critical=50 （默认输出warning以上的日志）
# # 日志程序化设计(basicConfig定制日志)
# logging.basicConfig(
#     # 日志输出位置（不指定默认为终端）
#     # filename="日志.log", # 文件名其他路径D:/qq/新建 文本文档.log
#     # 日志格式
#     format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",  # %（*）s 为固定格式其他可自己改
#     #         获取时间     获取日志名字    日志等级       哪个模块报的信息  级别输出信息
#     # 时间格式
#     datefmt="%Y-%m-%d %x",
#     # 日志级别
#     level=10,
# )
# # 输出级别
# logging.debug("调试")  # （）可自定义
# logging.info("消息")
# logging.warning("警告")
# logging.error("错误")
# logging.critical("严重")
# # //////////////////////////////////////////////
# # ///////////////////////////////////////////////
# # 日志字典
# 变量名1=" 打印到文件  时间:%(asctime)s - 日志名字:%(name)s - 日志等级:%(levelname)s - 模块:%(module)s级别:%(message)s"
# 变量名2="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"
# 变量名3=" 打印到终端 %(levelname)s -%(asctime)s - %(name)s - %(lineno)d - %(module)s: %(message)s"
#                                                 # 日志输出行数
# LOGGING_DIC = {
#     "version":1,
#     "disable_existing_loggers":False,
#     "formatters": {
#         "自定义名称1":{
#             "format":变量名1},
#         "自定义名称2":{
#             "format":变量名2},
#         "自定义名称3":{
#             "format":变量名3},},
#     "handlers":{
#         "打印到终端（自定义名称）":{
#             "level":10,  # 日志级别数字或大写的日志级别都可以
#             "class":"logging.StreamHandler",  # 打印到屏幕
#             "formatter":"自定义名称3"},  # 自定义名称1或3
#         "默认(default)":{
#             "level":10,
#             "class":"logging.handlers.RotatingFileHandler",  # 保存到文件
#             "maxBytes": 1024*1024*10,  # 日志大小 这样1024*1024*5最好 当文件中大小大于指定大小时会新建一个文件将后产生的内容会存在新文件中
#             "backupCount": 50,  # 允许创建的新文件数
#             "formatter": "自定义名称1",  # 自定义名称1或3
#             "filename": "日志.log",  # 文件路径 os.path.join(os.path.dirname(os.path.dirname(__file__)),"log","日志.log")
#             "encoding": "utf-8",
#         },
#         "打印到文件的日志2(自定义名称)":{
#             "level":10,
#             "class":"logging.FileHandler",  # 保存到文件
#             "formatter":"自定义名称1",  # 自定义名称1或3
#             "filename":"C:/pycharm/日志/日志.log",  # 文件路径（换路径不能和其他的log文件在一个文件夹）
#             "encoding":"utf-8",},  # 指定字符编码
#     },
#     "loggers":{
#         "日志产生者(自定义名称)":{
#             "handlers":["打印到终端（自定义名称）","打印到文件的日志2(自定义名称)"],
#             "level":10,
#             "propagate":False,},  # 默认为True False最好 不用改
#         "":{
#             "handlers":["默认(default)"],
#             "level":10,
#             "propagate":False,},  # 此日志产生者用于后面getLogger输入不存在的日志产生者时，将输入日志产生者命名到""中输出（默认日志）
#         },
# }
# # formatters 里是多个日志格式  handlers是控制日志输出位置 loggers（可指定多个日志产生者）是产生不同级别的日志
# # 综合
# # import 日志字典文件
# from logging import config,getLogger
# config.dictConfig(LOGGING_DIC)  # 拿到字典 如果在不同文件为 文件.LOGGING_DIC
# 拿到日志产生者=getLogger("日志产生者(自定义名称)")  # 拿到日志产生者
# 拿到日志产生者.info("成功得到一条日志")  # 打印日志也就是debug("调试")info("消息")warning("警告")error("错误")critical("严重")
# 拿到日志产生者2=getLogger("不存在日志产生者")
# 拿到日志产生者2.info("这是默认日志输出的")
# # /////////////////////////////////////////////
# # 补充
# # 日志名的命名  就是日志产生者(自定义名称)的命名 （信息明确就好）
# # 日志轮转
# # 日志记录着程序运行过程中的关键信息，如果存在一个文件中可能会很大，需要定期分割（剪切到其他文件）（上面的 默认（"default"））
# # ////////////////////////////////////////////
# # /////////////////////////////////////////////
# 正则表达式
# import re
# 案例="a\rbc\tdef123\n456_+\f__=_-__+=_ _"
# # 1 findall() #从左到右匹配一边
# # 匹配单个字符的

# # \w 匹配字母数字及下划线（匹配单个，返回一个列表）  \W 取反（与小w比）
# print(re.findall("\w",案例))  # (匹配规则，匹配对象)
# print(re.findall("\W",案例))

# # \s匹配任意空白字符 匹配单个（就是\r \t \n \f 空格） \S匹配非空字符（取反\s）
# print(re.findall("\s",案例))
# print(re.findall("\S",案例))

# # \d 匹配任意数字（0-9）  \D取反（非数字的）
# print(re.findall("\d",案例))
# print(re.findall("\D",案例))
# 案例2="index index list"

# # \A 匹配字符串开头是否是定义的规则 \Z 匹配字符串结尾是否是定义的规则  了解就好

# # ^ 匹配字符串开头是否是定义的规则 $ 匹配字符串结尾是否是定义的规则
# print(re.findall("\Aindex",案例2))
# print(re.findall("list\Z",案例2))
# print(re.findall("^index",案例2))
# print(re.findall("list$",案例2))
# print(re.findall("^list$",案例2))  # 开头是l 结尾是t 中间是is (也就是只能是list)
# 重复匹配
#
# . 匹配任意字符(一个.代表一个字符)，除了换行符（\n） 当指定re.DOTALL时可以匹配所有字符
# 案例="a\rbc\tdef1323\n456_+\f=-+=_ _"
# print(re.findall(".",案例))
# print(re.findall("3.3",案例))
# print(re.findall("=.=",案例))
# print(re.findall(".",案例,re.DOTALL))
#
# * 左侧字符重复0次或无穷次 必须和其它字符连用
# x="axbababababaaxaaaabbbbbbbbdgdgabbb"
# print(re.findall("ab*",x))  # a必须有b可以有一次或多次或零次
#
# # + 左侧字符重复一次或无穷次
# print(re.findall("ab+",x))  # a必须有b可以有一次或多次
#
# # ? 左侧字符重复零次或一次
# print(re.findall("ab?",x))  # a必须有b可以有零次或一次
#
# # {} 左侧字符重复n次到m次
# print(re.findall("ab{2,4}",x))  # a 必须有至少出现两次最多三次
# ////////////////////////////////
# 找小数点
# print(re.findall("\d+\.?\d*","dsf12.asff123vxv1.13fsfsf12sfffdff3"))
# \d匹配任意数字,+左侧字符重复一次或无穷次\转义.不是.而是代表一的字符 ? 左侧字符重复零次或一次 \d匹配任意数字* 左侧字符重复0次或无穷次
# []可以匹配其中的一个其中的指定字符
# print(re.findall("a[1-9]b","egegsega1ba2ba3ba4ba5ba6bthwhnshsh"))
# print(re.findall("a[0123456789]b","a8ba9ba7ba6bsega1ba2ba3ba4ba5ba6b"))  # 其中的一个其中的指定字符
# print(re.findall("a[0-9a-zA-X]b","a8ba9ba7ba6bsega1ba2ba3ba4ba5ba6baxbaybaDbaOb"))  # 0-9范围的意识
# print(re.findall("a[^0-9a-zA-X]b","a@ba!ba%ba8ba9ba7ba6bsega1ba2ba3ba4ba5ba6baxbaybaDbaOb"))  # 加^是取反的意思 放在中括号外是原意
# print(re.findall("a[0-9a-zA-X\-]b","a-ba8ba9ba7ba6bsega1ba2ba3ba4ba5ba6baxbaybaDbaOb"))  # \-匹配- \是转意的意思
# /////////////////////////////////
# 面向对象编程
# 对象是一个容器，用来存放数据以及功能（将程序整合）
# 程序=数据+功能
# 1 类（也是容器用来存放同类对象的相同数据）
# 先定义类，在调用类产生对象
# 类是对象相似数据与功能的集合体
# 类中最常见的是变量与函数的定义，但是类体中可以包含任何代码
# 类体代码在类的定义阶段就会运行，会产生类的名称空间
# class 定义类
# 案例代码
# 学生1={"姓名":"韦叶富","年龄":20,"学号":123,"学校":"大学","选课号":321,"班级":1,"学生信息":"学生信息","选课信息":"选课信息"}
# 学生2={"姓名":"韦玉听","年龄":22,"学号":456,"学校":"大学","选课号":654,"班级":2,"学生信息":"学生信息","选课信息":"选课信息"}
# class 学生:
#     # 变量的定义（共用的）
#     学校="大学"
#     # 功能的定义
#     def 学生信息(学生1):
#         print("学生信息:姓名:%s年龄:%s学号:%s"%(学生1["姓名"],学生1["年龄"],学生1["学号"]))
#     def 选课信息(学生1,x,y,z):
#         学生1["姓名"]=x
#         学生1["年龄"]=y
#         学生1["选课号"]=z

# 下面不和上面相连
# print(学生.__dict__) # 查看类的名称空间 (下面出现的可以忽略只是查看信息的)
# print(学生.学生信息)  # 属性访问语法（类.内部信息）
# ///////////////////////////////////////
# 调用类产生对象（调用类的过程也叫实例化）
# 1 先产生一个空对象
# 2 python会自动调用__init__方法将空对象以及调用类时括号内传入的参数一同传给__init__方法
# 3 返回初始化完的对象
# 对象1=学生()  # 产生对象 对象1（自定义）
# 对象2=学生()
# 对象3=学生()
# /////////////区间内的看看就好不用使用////////////
# 对象1.姓名="哈宝"  # 将信息放入对象
# 对象1.年龄=10  # 将信息放入对象
# 对象1.学号=111  # 将信息放入对象
# print(对象1.__dict__)  # 查看名称空间
# 对象2.姓名="宝哈"
# 对象2.年龄=12
# 对象2.学号=222
# print(对象2.__dict__)
# 对象3.姓名="哈宝比"
# 对象3.年龄=22
# 对象3.学号=333
# print(对象3.__dict__)
# /////////////区间内的看看就好不用使用////////////
# 解决问题 重复代码
# def 添加信息(对象,x,y,z):
#     对象.姓名=x
#     对象.年龄=y
#     对象.学号=z
# 添加信息(对象1,"哈宝",10,111)
# 添加信息(对象2,"宝哈",12,222)
# 添加信息(对象3,"哈宝比",22,333)
# print(对象1.__dict__)
# print(对象2.__dict__)
# print(对象3.__dict__)

# /////////////区间内的看看就好不用使用////////////
# 解决问题 不够整合的问题
# __init__方法的使用
# 1 会在调用类时自动触发，并初始化对象
# 2 __init__是一个函数可以放其他代码
# 3 __init__的返回值只能是None
# class 学生:
#     # 变量的定义（共用的）
#     学校="大学"
#
#     def __init__(对象,x,y,z):  # __init__不能自定义名称，默认的意思  就是def 添加信息(对象(一般写self),x,y,z):函数
#         对象.姓名=x
#         对象.年龄=y
#         对象.学号=z
#     # 功能的定义
#     def 学生信息(对象):
#         print("学生信息:姓名:%s年龄:%s学号:%s"%(对象["姓名"],对象["年龄"],对象["学号"]))
#     def 选课信息(对象,x,y,z):
#         对象["姓名"]=x
#         对象["年龄"]=y
#         对象["选课号"]=z
# 对象1=学生("哈宝",10,111)  # def __init__(对象,x,y,z):中的 对象 不用传 底层自己传了（只需要传剩下的参数）
# print(对象1.__dict__)
# 属性查找顺序
# 类中存放的是对象共有的数据和功能（类改对象改
# 类可以访问
# 1 类的数据属性
# 对象3=学生("rr",10,11)
# 对象4=学生("ooo",1,22)
# 学生.学校="小学"
# 对象3.学校="大大学"
# 对象4.姓名="宝宝哈"
# print(学生.学校)
# print(对象3.学校)
# print(对象4.姓名)
# 类的函数属性（是绑定给对象用的）
# 绑定方法（谁调用绑定方法就会将谁当做第一个参数自动传入）
# 对象3.学生信息()  # 某种原因报错无法解决
# //////////////////////////////
# 面向对象三大特性（封装，继承，多态）
# 封装=整合
# 隐藏属性（加__）(对外部对内在类内部可以调用)(意义严格控制用户对属性的操作)
# class foo:
#     __x=1
#     def __f1(self):
#         print("ggg")
# foo.x #无法调用到
# ////////////////////
# class foo:
#     def __init__(self,name):
#         self.__name=name
#     def get_name(self):  # self.__name的接口函数
#         print("拿到名字了吧")
#         print(self.__name)
#     def 修改名字(self,a):
#         if a=="打你":
#             print("请输入规范名字")
#         self.__name=a
#
# z=foo("为叶夫")
# z.get_name()
# z.修改名字("打你")
# 隐藏函数（为了在内部使用，不给外部使用）
# ////////////////////////////////////////
# property 装饰器的一种（将类中的功能伪造成一个数据）
# 装饰器 在不改变被装饰对象源代码以及调用方法的前提下为被装饰对象添加新功能的可可调用对象
# 案例1
# class 体质参数:
#     def __init__(self,名字,身高,体重):
#         self.名字=名字
#         self.身高=身高
#         self.体重=体重
#     @property # 不用时返回值时函数
#     def BMI(self):
#         return self.体重/(self.身高*2)
#
# 对象1=体质参数("尾叶富",1.69,50)
# print(对象1.BMI)
# 案例2
# class foo:
#     def __init__(self,名字):
#         self.__名字=名字
#     def get_name(self):
#         return self.__名字
#     def 修改名字(self,q):
#         if q=="打你":
#             print("违规名字")
#             return
#         self.__名字=q
#     def del_name(self):
#         del self.__名字
#         print("删除成功")
#     名字=property(get_name,修改名字,del_name)  # 将三个接口伪装为一个数据属性
# 对象=foo("weiyefu")
# print(对象.名字)
# 案例3=案例2
# class foo:
#     def __init__(self,名字):
#         self.__名字=名字
#     @property
#     def name(self):
#         return self.__名字
#     @name.setter
#     def name(self,q):
#         if q=="打你":
#             print("违规名字")
#             return
#         self.__名字=q
#     @name.deleter
#     def name(self):
#         del self.__名字
#         print("删除成功")
# 对象=foo("weiyefu")
# print(对象.name)
# ////////////////////////////
# 继承(解决类与类之间代码冗余问题)
# 是一种创建新类的方式，新建的类称为子类或派生类，父类也叫基类或超类（python支持多继承：新建的类可以继承一个或多个类）
# class x1:
#     pass
# class x2:
#     pass
# class x3:
#     pass
# class 继承1(x1):  # 单继承
#     pass
# class 继承2(x1,x2):  # 多继承
#     pass
# print(继承1.__bases__)  # 查看父类
# print(继承2.__bases__)
# # 新式类:继承了object类的子类，以及该子类的子类子类。。。。。。
# # 经典类:没有继承object类的子类，以及该子类的子类子类。。。。。。
# # python全是新式类
# print(x1.__bases__)
# 多继承（不推荐使用）
# 优点：子类可以同时继承多个父类的属性，最大限度的重用代码
# 缺点：与人的逻辑冲突（违背人的思维习惯），引发菱形问题，代码可读性差，扩展性差（用Mixins机制就好）
#  如何实现继承
# ////////////////////////////////区间内为问题代码///////////////////////
# （类与类之间出现冗余问题）
# class 学生:
#     学校="大学"
#
#     def __init__(self,名字,年龄,性别):
#         self.名字=名字
#         self.年龄=年龄
#         self.性别=性别
#     def 选课(self):
#         print("学生%s选课中"%self.名字)
# class 老师:
#     学校 = "大学"
#
#     def __init__(self,名字,年龄,性别,薪资,等级):
#         self.名字=名字
#         self.年龄=年龄
#         self.性别=性别
#         self.薪资=薪资
#         self.等级=等级
#     def 打分(self):
#         print("老师%s正在打分"%self.名字)
# ////////////////////////////////区间内为问题代码///////////////////////
# class 整体:
#     学校 = "大学"
#
#     def __init__(self, 名字, 年龄, 性别):
#         self.名字 = 名字
#         self.年龄 = 年龄
#         self.性别 = 性别
#
#
# class 学生(整体):  # 继承整体(调用子类时现在自己找如果没有就去父类中找)
#
#     def 选课(self):
#         print("学生%s选课中" % self.名字)
#
# class 老师(整体):
#     学校 = "大学"
#
#     def __init__(self, 名字, 年龄, 性别, 薪资, 等级):
#         整体.__init__(self, 名字, 年龄, 性别)  # 部分功能调用到父类的，  (self, 名字, 年龄, 性别)中必须要有参数(调用的是函数必须传参)
#         self.薪资 = 薪资
#         self.等级 = 等级
#
#     def 打分(self):
#         print("老师%s正在打分" % self.名字)
# 对象1=学生("lili",10,"女")
# print(对象1.__dict__)
# 对象2=老师("wyf",10,"男",5000,1)
# print(对象2.__dict__)
# 对象2.打分()
# //////////////////////////////////////////////////////
# 单继承背景下的属性查找顺序(先从对象找没有再从对象的类找没有再从对象的父类找)
# class foo:
#     def f1(self):
#         print("foo.f1")
#     def f2(self):
#         print("foo.f2")
#         self.f1()
# class fpp(foo):
#     def f1(self):
#         print("fpp.f1")
# 对象=fpp()
# 对象.f2()  # fpp找没有再去foo父类找，有了f2，self.f1()再在对象类中找有了执行
# //////////////////////////////
# 菱形问题:D继承了BC，BC同时继承了A(非object类)，这样带来的一种问题(略)
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# //////////////////////////////////
# Mixins机制（多继承的正确打开方式）（一种规范）
# 核心:在多继承背景下尽可能的提升多继承的可读性
# class 交通工具:
#     pass
#
# class 飞Mixin:  # 创建一个特殊的类但又不是父类只是为了添加一些功能的
#     def 飞行(self):
#         pass
#
# class 大飞机(交通工具,飞Mixin):  # 真正的父类是交通工具
#     pass
#
# class 小飞机(交通工具,飞Mixin):
#     pass
#
# class 汽车(交通工具):
#     pass
# //////////////////////////////////
# 子类重用父类功能的两种方法
# 1 直接调用父类的函数，不依赖继承关系（略，上面多是）
# 2 super()调用父类提供给自己的方法(super会得到一个特殊的对象，该对象会参照MRO(底层原理)去当前父类中找属性)
# class 整体:
#     学校 = "大学"
#
#     def __init__(self, 名字, 年龄, 性别):
#         self.名字 = 名字
#         self.年龄 = 年龄
#         self.性别 = 性别
#
#
# class 学生(整体):  # 继承整体(调用子类时现在自己找如果没有就去父类中找)
#
#     def 选课(self):
#         print("学生%s选课中" % self.名字)
#
# class 老师(整体):
#     学校 = "大学"
#
#     def __init__(self, 名字, 年龄, 性别, 薪资, 等级):
#         # super会得到一个特殊的对象，该对象会参照MRO(底层原理)去当前父类中找属性(python3中不需要在括号加任何东西)
#         # # # super(老师,self).__init__(self, 名字, 年龄, 性别)
#         super().__init__(名字, 年龄, 性别)  # 部分功能调用到父类的（self要去掉默认帮你传了）
#         self.薪资 = 薪资
#         self.等级 = 等级
#
#     def 打分(self):
#         print("老师%s正在打分" % self.名字)
# 对象1=学生("lili",10,"女")
# print(对象1.__dict__)
# 对象2=老师("wyf",10,"男",5000,1)
# print(对象2.__dict__)
# 对象2.打分()
# ///////////////////////////////////////
# 多态（同一事物的多种形态）
# //////////////////////////////////////
# 反射机制（动态语言的）
# 反射 （指在程序运行过程当中可以“动态”获取对象的信息）
# 如何实现反射？
# 实现反射的步骤
# 1.先通过dir函数查看某一对象下的属性
# class obj:  # （一切皆对象，可将类改为obj=100试试）
#     z=100
#     def x(self):
#         print("qqqqq")
#
#     def y(self):
#         print("ssss")
#
# print(dir(obj))
# 2.可以通过字符串反射到真正的属性上，得到属性值(4个内置函数的使用)
# hasattr()  # 判断属性是否存在
# getattr()  # 得到属性
# setattr()  # 做一个赋值属性操作（obj.x=某个值）
# delattr()  # 删除属性
# //////////////////
# print(hasattr(obj,"z"))
# print(getattr(obj,"z"))
# setattr(obj,"z",200) # (将z的原值改为200)（此函数没有返回值不用打印（打印只有None））
# print(getattr(obj,"z"))
# delattr(obj,"z")
# print(obj.__dict__)  # 查看名称空间
# ////////////////////////////
# 补充
# class obj:
#     z=100
# print(hasattr(obj,"z"))
# print(getattr(obj,"l",None))  # 加个None没有该属性则返回空不会报错
# setattr(obj,"z",200) # (将z的原值改为200)（此函数没有返回值不用打印（打印只有None））
# print(getattr(obj,"z"))
# delattr(obj,"z")
# print(obj.__dict__)  # 查看名称空间
# //////////////////////
# 案例
# class 网络传输:
#     def 上传(self):
#         print("正在上传")
#     def 下载(self):
#         print("正在下载")
#     def 用户输入(self):
#         输入=input("请输入:").strip()
#         if hasattr(self,输入):  # 判断是否存在输入功能
#             getattr(self, 输入)()  # 加括号运行
#         else:
#           print("输入的指令不存在")
# x=网络传输()  # 赋值
# x.用户输入()  # 运行
# /////////////////////////////////
# 内置方法（在类内部以__开头以__结尾的方法）
# 特点:会在某种情况下自动触发执行
# 用处:为了定制我们的类或对象
# ////////////////
# 如何使用内置方法
# 1.__str__  在打印的时候自动触发，然后将返回值当作本次打印的结果输出（在这里是使提示信息更明显的作用）
# 2.__del__在删除对象事触发，会先执行该方法(主要在程序中有使用到系统功能的地方)
# class 整体:
#     学校 = "大学"
#
#     def __init__(self, 名字, 年龄, 性别):
#         self.名字 = 名字
#         self.年龄 = 年龄
#         self.性别 = 性别
#
#
# class 学生(整体):  # 继承整体(调用子类时现在自己找如果没有就去父类中找)
#
#     def 选课(self):
#         print("学生%s选课中" % self.名字)
#
# class 老师(整体):
#
#     def __init__(self, 名字, 年龄, 性别, 薪资, 等级):
#         整体.__init__(self, 名字, 年龄, 性别)  # 部分功能调用到父类的，  (self, 名字, 年龄, 性别)中必须要有参数(调用的是函数必须传参)
#         self.薪资 = 薪资
#         self.等级 = 等级
#
#     def 打分(self):
#         print("老师%s正在打分" % self.名字)
#
#     def __str__(self):
#         return "{0}:{1}".format(self.名字,self.年龄)
#     def __del__(self):
#         print("结束")
# obj=老师("贵人",11,"男",100,2)
# print(obj)
# print("eeeeeeeeeeeeeeeeeeeeeeeeeee")  # 标记而已
# /////////////////////////////
# 元类:调用类的类（一切皆对象）
# 关系:元类=====>实例化=====>类=====>实例化======>对象
# 1.type是内置的元类
# 2.查看内置的元类:用class定义的类以及内置的类都是由内置的元类type实例化产生的
# class x:
#     pass
# print(type(x))
# print(type(int))
# ///////////////////
# # class 机制（class定义类的过程）
# # 类的特征
# # 1.类名
# class_name="未知"
# # 2.类的基类（父类）
# class_bases=(object,)
# # 3.执行类体代码拿到类的名称空间
# class_dic={}
# class_body="""
# def __init__(self,名字,年龄,性别):
#     self.名字=名字
#     self.年龄=年龄
#     self.性别=性别
# def 选课(self):
#     print("学生%s选课中"%self.名字)
# """
# exec(class_body,{},class_dic)  # 此函数了解就好
# # 4.调用元类
# p=type(class_name,class_bases,class_dic)
# # //////////////////////////////////////
# x=p("维耶夫",12,"男")  # 调用类可忽略
# print(x.__dict__)  # 调用类可忽略
# ///////////////////////////////////
# 如何自定义元类来控制类的产生
# class 要继承的类(type):  # 只有继承了type类的类才是元类
#     def __init__(self,x,y,z):  # 需要再加三个参数用于接收空对象(x=类名，y=基类，z=类的名称空间 {可自定义名称})
#         print("run")
#     pass
#
# class 人(metaclass=要继承的类):  # metaclass=是固定的
#     pass
# """
# 人=要继承的类(类名，基类，类的名称空间)
# 调用要继承的类发生的三件事
# 1.先造一个空对象=人，调用类内的__new__方法（早于__init__方法）
# 2.调用要继承的类内的--init--方法，完成初始化对象的操作
# 3.返回初始化好的对象
# """
# 案例
# class A(type):  # 只有继承了type类的类才是元类
#     def __init__(self,x,y,z):  # 需要再加三个参数用于接收空对象(x=类名，y=基类，z=类的名称空间 {可自定义名称})
#         print("run")
#         if not x.istitle():  # （判断类名首字母是否大写）
#             raise NameError("类名的首字母必须大写")  # 主动抛出异常
#
# class w(metaclass=A):
#     pass
# //////////////////////////////
# 元类后面的暂略(难度高)
# 元类下的属性查找
# 对象--类--父类
# 父类不是元类
# ////////////////////////////////
# 异常处理
# 异常的特征 1异常的追踪信息 2异常的类型 3异常的内容
# 1.什么是异常——异常是程序发生错误的信号，程序一旦发生错误就会抛出异常，程序的运行也会终止
# 2.为何要处理异常
# 2.1为了增强程序的健壮性，即程序在运行过程中出错了，也不会终止程序，而是捕捉异常并处理——将出错信息记录在日志内
# 3.如何处理异常
# 1语法错误 （不在异常处理范围内）
# 2逻辑错误
# 2.1错误发生的条件是可以预知的（略）
# 2.1错误发生的条件是不可以预知的
# 处理异常的语法格式
# ///////////////////////////////////
# try:
#     子代码块1  # 有可能会抛出异常的代码
#     子代码块2
#     子代码块3
#     ......
# except 异常类型1 as x:  # as x (将异常赋值给x，x可以改)
#     pass
# except 异常类型2 as x:  # as x (将异常赋值给x，x可以改)
#     pass
# ......
# else:
#     子代码（如果被检测的子代码块没有发生异常，则会执行else的子代码）
# finally:
#     子代码（无论被检测的子代码快有没有发生异常，都会执行finally的子代码{如果子代码n前的代码错误还可以运行子代码n}）
# ///////////////////////////////////////////
# 注意:try 不能和else单独连用，可以和 except 以及 finally单独连用
# 案例
# print("开始执行")
# try:
#     print("子代码块1开始")
#     l=[1,2]
#     print(l[3])  # 这个会错误
#     print("子代码块2开始")
#     x  # 这个会错误
#     print("子代码块3开始")
#     q={"name":"土豆"}
#     print(q["name"])
# except IndexError as e:  # 在不知道异常类型的情况下可加多个异常类型捕捉（当一个异常类型捕捉不成功，会捕捉第二个异常类型以此类推）
#     print("异常已收集",e)
# except NameError as e:
#     print("异常已收集",e)
# except SyntaxError as e:
#     print("异常已收集",e)
# //////////////////////////////////////////////
# /////////////////////////////////////////////////
# """
# 网络通信基础
# 一，CS架构与BS架构
# 1.CS架构（客户端服务与服务端）
# 2.BS架构（浏览器与服务端）
# 
# 客户端                              服务端
# 操作系统                            操作系统
# 计算机硬件《========================》计算机硬件

# 二， 网络通信
# 网络＝物理连接介质＋互联网通信协议
# 三 互联网通信协议
# 1.OSI七层协议
#                    五层协议
# 应用层
# 表示层              
# 会话层              （三合一）应用层
# 传输层              传输层
# 网络层              网络层
# 物理链路层          
# 物理层             （二合一）网络接口层
# 
# 协议:规定数据的组织形式
# 格式:头部＋数据部分
# ///////////////////////////

#============= 1.物理层（协议不用知道）==============
# 规定:一组数据称之为为（bit）

# ==============2.物理链路层（以太网协议）==========
# 规定1:一组数据称之为帧
# 规定2:帧分成两部分（头部+数据）
# 头部包含:原地址+目标地址＋数据类型（该地址为mac地址）
# 数据包含:网络层整体的内容
# 规定3:接入互联网的主机都必须有一块网卡，每块网卡都有一个独一无二的地址，改地址为max地址
# 注意:计算机通信靠广播（吼）

# =============3.网络层:IP协议==================
# 划分广播域
# 广播域与外部通信需要用到网关
# 网关与外部通信使用路由协议
# 规定1:一组数据称之为一个数据包
# 规定2:数据包分为两部分即头部+数据
# 头部包含:原地址+目标地址 该地址为IP地址
# 数据包含:传输层包含的整体内容

# /////////////////////////////////
# =====================IP地址================
# 最新的为IPv6，ipv4应用最多
# IPv4地址（用32位二进制数表示）
# 8bit.8bit.8bit.8bit
# 范围（十进制）（0.0.0.0——255.255.255.255）

# ================子网掩码:（用32位二进制数表示）=======
# 8bit.8bit.8bit.8bit
# 一个合法的ipv4地址组成部分:ip地址/子网掩码地址

# 3.1计算两个计算机是否在同一个局域网
# 计算机1：
# 172.16.10.1：      （IP地址）     （十进制）    10101100.00010000.00001010.000000001（二进制）
# 255255.255.255.0： （子网掩码）    （十进制）    11111111.11111111.11111111.000000000（二进制）
# 172.16.10.0：      （结果）       （十进制）    10101100.00010000.00001010.000000000（二进制）
# 计算机2：                                              （计算方法：IP地址与子网掩码对比都为1才取1其他取0）
# 172.16.10.2：      （IP地址）    （十进制）   10101100.00010000.00001010.000900010（二进制）
# 255.255.255.255.0：（子网掩码）   （十进制）   11111111.11111111.11111111.000000000（二进制）
# 172.16.10.0：      （结果）      （十进制）   10101100.00010000.00001010.000000000（二进制）
# ////////////////////////////////////////////////////////////////////////////////////////////
# ===============四ARP协议（解析协议）=============
# 将ip地址解析成mac地址
# ///////////////////////////
# 两台计算机在同一个局域网内
# 计算机1                          直接             计算机2
# ARP:判断是否在同一个局域网，计算自己的ip与对方的ip
# 1.计算两者网络地址，如果一样，拿到计算机2的mac地址就可以了
# # 两台计算机不在同一个局域网内
# 计算机1                          网关             计算机2
# ARP:判断是否在同一个局域网，计算自己的ip与对方的ip
# 1.计算两者网络地址，如果不一样，应该拿到网关的mac地址
# 2.发送广播包
# 3.发送端mac    FF:FF:FF:FF:FF（请求网关mac地址）    我的ip地址  目标（网关）的ip地址  数据
# ////////////////////////
# =============五注意==============
# ip地址+mac地址==>标识全世界内独一无二的一台计算机  或者  ip地址==>标识全世界内独一无二的一台计算机(有ARP协议)

# 五 传输层（基于端口）TCP协议/UDB协议
# 端口范围 0——65535  0——1023为系统占用
# ip+port   标记全世界范围内独一无二的一个基于网络通信的应用程序
# 基于tcp协议通信:必须建立一个双向通信的链接(三次握手建立链接，请求，确认+请求，确认)
# c——————————>s
# s<——————————c
# 断链接(四次握手)
# tcp协议的半连接池:服务端对客户端的请求有上限，当超过链接池的容量时请求无法发出，防止服务端崩溃
#
# tcp是可靠传输
# (发送数据必须等到对方确认才算完成，才会将自己内存中的数据清理掉)
#
# udb协议(传输速度快，但不可靠)
# 不需要建立链接
# 传输数据无需对方确认
#
# 注意:当服务端大量处于TIME_WAIT状态时意味着服务端正在经历高并发状态
#
# 六 应用层与Socket(套接字)

# 可以自定义协议=》头部+数据部分
# 自定义协议需要注意的问题：
# 1、两大组成部分=头部+数据部分
# 头部：放对数据的描述信息
# 比如：数据要发给谁，数据的类型，数据的长度
# 数据部分：想要发的数据
# 2、头部的长度必须固定
# 因为接收端要通过头部获取所接接收数据的详细信息
#
# 其他协议介绍
# dhcp协议:用于获取网络通信的一些地址(也可以手动配置地址)。
# DNS:域名解析
# """
# ///////////////////////////////////////////////////
# ==================================================
# Socket(套接字)实例(详见文件，客户端，服务端)
# ===================================================
# 并发（socketserver模块）(详见文件，客户端，服务端)
# ===================================================
# 并发编程
# 理论
# 1.并发:看起来像同时运行的
# 2.并行:真正意义上的同时执行
# 3.单核（一个核时）计算机不能实现并行，但能并发
# 一:创建子进程方法
# from multiprocessing import Process
# def 主进程():
#     print("一个主进程")
# def 子进程():
#     print("子进程")
# if __name__=="__main__":
#     # 1.创建一个对象
#     对象=Process(target=子进程)  # target=函数名 如果函数有参数加关键字args=(参数1,参数2...)是一元组
#     # 2.开启进程
#     对象.start()  # (会在主进程运行完后再运行)
#     主进程()
#     print("主进程")
# 二.join方法（让子进程先运行）
# from multiprocessing import Process
# def 主进程():
#     print("一个主进程")
# def 子进程():
#     print("子进程")
# if __name__=="__main__":
#     # 1.创建一个对象
#     对象=Process(target=子进程)  # target=函数名 如果函数有参数加关键字args=(参数1,参数2...)是一元组
#     # 2.开启进程
#     对象.start()
#     对象.join()  # 子进程会先运行
#     主进程()
#     print("主进程")
# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 三.其他方法
# 查看进程号(pid):终端输入:tasklist     或os.getpid()
# import os
# a=os.system("tasklist")
# print(os.getpid())
# 、、、、、、、、、、、、、、、、、、、、、、、
# 四.守护进程:（了解）（主进程起，守护起，主进程死，守护死）
# from multiprocessing import Process
# def 守护进程():
#     print("守护进程开启")
# if __name__=="__main__":
#     p = Process(target=守护进程)
#     p.daemon = True  # 必须放在进程创建之前
#     p.start()
#     print("主程序")
# 五.互斥锁（了解，会遇到，但不会解决）:并发会出现数据错乱，将并发变为串行，保证数据的可靠性