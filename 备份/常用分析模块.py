import numpy as np
import pandas as pd
one_all=np.arange(10)
s_all=np.array([[1,2,3,4],[4,5,6,7]])
# ==========numpy库(科学计算)============
# 一，创建数组
# 1.array():创建数组,参数(多级列表或元组,dtype="可指定数组类型"),当传入的数据类型不止一种时,会转化为同一种类型(优先级:str>float>int)
# 2.数组对象.dtype:获取数组类型,不加括号
# ls = [[1, 2, 3], [9, 8, 7]]
# x = np.array(ls)
# print(x)
# print(x.dtype)
# array函数使用已有的python数据类型创建数组效率并不高，因此需要专门的函数创建数组。
# 3.arange:创建数组，(对象)或(起始值,终止值,步长),顾头不顾尾，对浮点数不太友好
# 4.linspace:创建数组，(起始值,终止值,元素个数),顾头顾尾，对浮点数友好
# 5.logsspace:创建数组(等比数列)，(起始幂,终止幂,元素个数)，默认底数为10
# 6.zeros:创建指定形状全为0的数组，(整数、列表[行，列]或元组)
# 7.ones:创建指定形状全为1的数组，(整数、列表[行，列]或元组)
# 8.diag:创建对角矩阵，对角线为0或指定值其他为0的矩阵(整数、列表[对角线值]或元组)
# 二，数组对象属性及类型转换（不加括号）
# 1.ndim:秩(行)
# 2.shape:维度
# 3.size:元素个数
# 4.dtype:类型
# 5.itemsize:每个元素的字节大小
# 6.可修改维度
# y = np.array([[1, 2, 3], [9, 8, 7]])
# y.shape = 3, 2
# 7.astype:修改数据类型，数组对象.astype(np.类型) np为导入的as np
# 三，numpy.random模块的使用
# 1.randint:生成指定范围的随机整数，顾头不顾尾。(范围x,范围y,size=(行,列))
# x = np.random.randint(1, 20, size=(4, 5))
# 2.rand:生成[0,1]的随机数。(行，列)
# ==================================================
# 3.seed:确饰随机数生成器的种子
# 4.permutation:返回一个序列的随机排列或返回一个随机排列的范围
# 5.shuffle:对一个序列进行随机排序
# 6.binomial:产生二项分布的随机数
# 7.normal:产生正态(高斯)分布的随机数
# 8.beta:产生 beta 分布的随机数
# 9.chisquare:产生卡方分布的随机数
# 10.gamma:产生 gamma分布的随机数
# 11.uniform:产生在[o,1)中均匀分布的随机数
# ===================================================
# 四，数组变换
# (一)，数组重塑(原数组不会改变)(数组对象.x)
# 1.reshape:改变数组的维度。(行，列)，可以指定一个未知维度，把某一个参数设置为-1即可
# 2.ravel:数组散开(即改为一维数据)，无参
# (二)，数组合并(每一行算一个整体)
# 1.hstack:横向合并数组。((数组1,数组2))
# 2.vstack:纵向合并数组。((数组1,数组2))
# 3.concatenae:可横向或纵向合并数组。((数组1,数组2),axis=横纵向合并参数) 方向合并参数1横向0为纵向
# (三)，数组分割
# 1.hsplit:横向分割数组。(数组,分割个数)
# 2.vsplit:纵向分割数组。(数组,分割个数)
# 3.split:可横向或纵向分割数组。(数组,分割个数,axis=横纵向分割参数)方向合并参数1横向0为纵向
# (四)，数组转置和轴对称
# 1.transpose:数组转置
# x=np.array([[1,2,3,4],[4,5,6,7]])
# a=x.transpose()或a=np.transpose(x)
# print(a)
# 2.数组的T属性:数组转置
# print(s_all.T)
# 3.swapaxes:数组的轴对换。(0,1)
# print(s_all.swapaxes(0,1))
# 五，数组的切片和索引
# (一)，一维数组索引，和列表一样
# (二)，多维数组的索引。[行,列]当涉及到多行多列时，行和列可以分别细分为x:y形式
# print(s_all[1,0:2])
# 六，数组的运算
# （一），数组和标量间的运算（ufunc函数）
# 1.四则运算：+、-、*、/、** 数组形状必须相同
# 2.比较运算:>、>=、<、=<、==、！= 返回的结果是一个布尔数组
# 3.ufunc函数的广播机制
# 广播：是指不同形状的数组之间执行算术运算的方式。广播机制需要遵循4个原则：
# (1)让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐。
# (2)输出数组的shape是输入数组 shape的各个轴上的最大值。
# (3)如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错。
# (4)当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值。
# 4.条件逻辑运算
# where:(条件,返回值1,返回值2)，满足条件返回1，否则返回2
# x=np.where([True],[[1,9],[2,8]],[[2,8],[2,8]])
# print(x)
# 七，numpy中的数据统计与分析
# 1.排序
# sort:(数组,axis=值,king=排序算法,字段,)
# axis=1：沿横轴排序，axis=1：沿纵轴排序，axis=None：将数组平坦化后再排序，排序算法：默认quicksort，字段：如果数组包含字段，则为要排序的字段。
# x=np.array([["x","y"],
#             [0,1],
#             [1,2],
#             [2,3],
#             [3,4],
#             [4,5]])
# y=np.sort(x,axis=1,)
# print(y)
# 2.重复数据与去重
# 重复tile/repeat:（数组，重复次数）、（数组，重复次数，axis=值），axis：0按行重复，1按列重复
# x=np.array([[1,2],[8,9]])
# print(np.tile(x,3))
# print(np.repeat(x,3,axis=0))
# unique:去重(数组)
# x=np.array([1,2,3,4,5,6,7,8,1,23])
# print(np.unique(x))
# 八，常用统计函数，针对二维数组时，都需要注意轴的概念：axis参数，0为沿着纵轴计算，1为沿着横轴计算。不指定为所有元素总和
# x=np.array([[1,2],[3,4]])
# 1.sum:求和，数组中元素之和
# print(np.sum(x,axis=0))
# 2.mean:均值
# print(np.mean(x,axis=1))
# 3.std:标准差,每个值减去平均值之和除以元素个数再开方。
# print(np.std(x,axis=1))
# 4.var:方差，方差=标准差^2
# print(np.var(x))
# 5.min:最小值
# 6.max:最大值
# ======================================
# ======pandas模块(基于np的数据分析模块)====
# ======================================
# 一，数据结构(三种)
# series类型：类似于数组。Series是一种一维数组对象，包含一个值序列，并且包含数据标签，称为索引(index),通过索引来访问数组中的数据。
# 1.Series:创建series，第一列为索引，第二列为值。
# print(pd.Series([1,2,3,4,5]))
# 2.可指定索引：Series(转换目标，index=索引列表，name=名字)
# print(pd.Series([1,2,3,4,5],index=[9,8,7,6,5],name=1))
# 3.通过字典创建Series，当传入一个字典时且不指定index时，索引是字典的键。当指定index时，index与值不匹配时，index的值将为NaN
# 4.修改Series的index。
# x=pd.Series([1,2,3,4])
# y=x.index=[9,8,7,6]
# print(x,y)
# DataFrame类型：是一个表格型的数据结构，它含有一组有序的列，每列可以是不同类型的值(数值、字符串、布尔值等)。DataFrame既有行索引也有列索引。
# 常用的是直接传入一个由等长列表或NumPy数组组成的字典来形成DataFrame。
# 1.DataFrame：创建DataFrame,(转换目标,columns=字段列表,index=索引列表)
# data={
#     "a":[1,2],
#     "b":[3,4],
#     "c":[5,6],
# }
# x=pd.DataFrame(data)
# print(x)
# 2.DataFrame会自动加上索引(跟Series一样),且全部列会被有序排列。当指定了列名顺序时，DataFrame的列会按照指定顺序进行排列。
# data={
#     "a":[1,2],
#     "b":[3,4],
#     "c":[5,6],
# }
# x=pd.DataFrame(data,columns=["a","c","b"])
# print(x)
# 3.当传入的字段在数据中找不到时，和Series会出现NaN
# 索引对象：存在索引对象。索引对象不能更改
# data={
#     "a":[1,2],
#     "b":[3,4],
#     "c":[5,6],
# }
# x=pd.DataFrame(data,columns=["z","x","c"],index=[9,8])
# print(x.index)
# print(x.columns)
# 1.索引对象的属性（x.index.属性）
#     1.append:        连接另一个Index对象，产生一个新的Index
#     2.diff:          计算差集，并得到一个Index计算交集计算并集
#     3.intersection:  计算交集
#     4.union:         计算并集
#     5.isin:          计算一个指示各值是否都包含在参数集合中的布尔型数组
#     6.delete:        删除索引i处的元素，并得到新的Index
#     7.drop:          删除传入的值，并得到新的Index
#     8.insert:        将元素插入索引i处，并得到新的Index
#     9.is_monotonic:  当各元素均大于或等于前一个元素时，返回True
#     10.is_unique:    当Index没有重复值时，返回True
#     11.unique:       计算Index中唯一值的数组
# 2.DataFrame的常用属性
#     1.values:查看所有值
#     2.columns:查看所有列（字段）
#     3.size:获取元素个数
#     4.ndim:获取维度
#     5.shape:形状
# data={
#     "a":[1,2],
#     "b":[3,4],
#     "c":[5,6],
# }
# x=pd.DataFrame(data)
# print(x.shape)
# 3.reindex 重建索引(Series,DataFrame（多一个columns参数）都可以用)：
# 索引对象无法修改，对已有索引进行排序或添加,(索引列表，fill_value=默认值)，fill_value（非必须）当由NaN值时设置默认值
# x=pd.Series([4,5,6,7],index=["a","b","c","d"])
# s=x.reindex(["g","b","c","d","e"],fill_value="是")
# print(s)
# 4.对于时间序列，重建索引可能需要进行插值或填值(值填充，基于已有值)，
# 使用method参数，"ffill"/"pad"前向填充(向下)，"bfill"/"backfill"后向填充(向上)。
# x=pd.Series(["2的","4的","8的"],index=[2,4,8])
# print(x)
# c=x.reindex([0,1,2,3,4,5,6,7,8],method="pad")
# print(c)
# reindex常用参数
#     1.index：新的索引序列
#     2.method:插值/填充方式
#     3.fill_value:代替缺失值
#     4.limit：最大填充量
# 5.DataFrame更换索引
# set_index:使用列作为索引 (列字段)
# reset_index:使用行作为索引 ()是set_index的反操作，如果不希望将索引添加为列则加上参数drop=True
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":["5块","4块"]})
# y=x.set_index("价格")
# z=y.reset_index()
# print(x)
# print(y)
# print(z)
# 6.DataFrame数据查询与编辑
# x=pd.DataFrame({"种类":["苹果","香蕉","火龙果","葡萄","菠萝","芒果"],
#                 "颜色":["红色","黄色","红色","绿色","黄色","黄色"],
#                 "价格":["5元","4元","3.5元","12元","3元","4.5元"]})
#     1.选取列：不能使用切片。
# print(x["价格"])
#     2.选取行：
#         1.通过索引实现,顾头不顾尾。
# print(x[1:2])
#         2.通过head、tail、sample获取。head/tail默认获取前/后5行，可传入值指定行数，sample随机获取n行
# print(x.head())
# print(x.head(6))
# print(x.tail())
# print(x.tail(6))
# print(x.sample(3))
#     3.选取行与列
#         1.loc:[行列表,列列表)]  :代表所有行或列
# print(x.loc[:,["种类","价格"]])
#         2.iloc:[行列表,列列表)]，列表为数字索引,第一行/列以0开始
# print(x.iloc[:,2])
# print(x.iloc[[1,4]])
# print(x.iloc[[1,5],[1,2]])
# 7.DataFrame布尔选择（!=,==,&(与),|(或)等等）
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":["5块","4块"]})
# print(x["价格"]=="4块")
# 8.DataFrame数据编辑
# 8.1添加数据
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":["5块","4块"]})
#     1._append添加一行,ignore_index=True时不使用index标签
# print(x._append({"种类":"橡果","颜色":"黄色","价格":"1块"},ignore_index=True))
#     2.添加一列：创建新的列并赋值即可
# x["口感"]=["甜","很甜"]
# print(x)
# 8.2drop：删除数据
#     1.删除行：(行索引)
# y=x.drop(1)
# print(y)
#     2.删除列：（列索引,axis=参考轴(0为行，1为列)）
# y=x.drop("价格",axis=1)
# print(y)
#     3.修改数据:对要修改的数据赋值即可，是对元数据的修改。
# x["价格"]="2块"
# print(x)
# ============================
# 二，pandas数据运算
# ==============================
# Pandas的数据对象在进行算术运算时，如果有相同索引则进行算术运算，如果没有则会进行数据对齐，但会引入缺失值。
# 1.相加
#     1.Series相加
# s1=pd.Series([1,2,3,4])
# s2=pd.Series([7,8,9,10,100])
# s3=s1+s2
# print(s3)
#     2.DataFrame相加：对齐会发生在行和列上
# x1=pd.DataFrame({"种类":["苹果"],"颜色":["红色"],"价格":["5块"],"s":["d"]})
# x2=pd.DataFrame({"种类":["香蕉"],"颜色":["黄色"],"价格":["4块"]})
# x3=x1+x2
# print(x3)
# 2.函数应用与映射
# 在数据分析时，经常会对数据进行较复杂的运算，此时需要定义函数。定义好的函数可以应用到Pandas数据中，有三种方法可以实现。
# 1.map函数：将函数套用到Series的每个元素中/DataFrame指定元素中。
# 2.apply函数：将函数套用到DataFrame的行与列上，行与列通过axis参数设置。
# 1.map使用方法(定义的函数名)
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":["5块","4块"]})
# def f(x):
#     return x.split("块")[0]  # (去掉块)切分为一个列表,这个只要第一个元素
# x["价格"]=x["价格"].map(f)  # 调用map函数传入f函数
# print(x)
# xx=pd.Series(["5块","4块","100块","52块"])
# y=xx.map(f)
# print(y)
# 2.apply用法
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":["5块","4块"]})
# y=x.apply(len)
# print(y)
# 3.排序
# 3.1在Series中，sort_index方法对索引排序，sort_values对值排序。默认为升序，降序排序时加参数ascending=False
# x=pd.Series([5,4,100,52],index=["d","b","c","a"])
# print(x.sort_index())
# print(x.sort_values())
# 3.2对于DataFrame排序，使用sort_index函数对行或列索引进行排序。把列名传给by参数即可。
# x=pd.DataFrame({"种类":["苹果","香蕉"],"颜色":["红色","黄色"],"价格":[5,400]},index=["b","a"])
# print(x.sort_index())
# print(x.sort_values(by="价格",ascending=False))
# 4.sum数据汇总:默认按列汇总，指定axis=1按行汇总
# x=pd.DataFrame({"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]},index=["windows","linux","mac"])
# print(x.sum())
# print(x.sum(axis=1))
# 5.描述性统计：
# x=pd.DataFrame({"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]},index=["windows","linux","mac"])
# print(x)
# y=x.describe()
# print(y)
# 常用数据描述性统计量
#     1.min：      最小值    |     max：  最大值
#     2.mean：     均值      |     ptp：  极差
#     3.median：   中位数    |     std：  标准差
#     4.var：      方差     |      cov：  协方差
#     5.sem：      标准误差  |      mode： 众数
#     6.skew：     样本偏度  |      kurt： 样本峰度
#     7.quantile： 四分位数  |      count：非空值数目
#     8.describe： 描述统计  |      mad：  平均绝对离差
# 6.类别型特征的描述性统计
#     1.unique：获取不重复的数组
# x=pd.Series([5,4,100,52,52],index=["d","b","c","a","k"])
# print(x.unique())
#     2.value_counts：频数统计
# print(x.value_counts())
# 7.数据分组
#     1.groupby方法（得到的是一个对象,可以调用多个方法。）
#     参数：
#         1.by：        可以传入函数、字典、Series等，用于确定分组的依据
#         2.axis：      接收int,表示操作的轴方向，默认为0
#         3.level：     接收int或索引名，代表标签所在级别，默认为None
#         4.as_index：  接收布尔类型,表示聚合后的聚合标签是否以DataFrame索引输出
#         5.SOrt：      接收布尔类型,表示对分组依据和分组标签排序，默认为True
#         6.group_keys：接收布尔类型,表示是否显示分组标签的名称，默认为True
#         7.squeeze：   接收布尔类型,表示是否在允许情况下对返回数据降维，默认为False
#         8.对于参数by,如果传入的是一个函数，则对索引进行计算并分组；如果传入的是字典或Series,则字典或Series的值作为分组依据；
#         如果传入的是NumPy数组，则数据元素作为分组依据；如果传入的是字符串或字符串列表，则用这些字符串所代表的字段作为分组依据。
# x=pd.DataFrame({"大":[2000,1000],"中":[500,200],"小":[5,4]},index=["b","a"])
#     2.分组
#         1.按列名分组
# y=x.groupby("大")
# print(y.mean())
#         2.按列表或元组分组：长度和DataFrame行数相同的列表或元组，相当于将列表或元组看作DataFrame的一列，然后将其分组。
# y=x.groupby(["y","w"]).mean()
# print(y)
#         3.按字典分组：通过字典作为分组键，分组时各字母不区分大小写。
# x=pd.DataFrame({"大":[2000,1000,2500],"中":[500,200,42],"小":[5,4,8]},index=["b","a","A"])
# y=x.groupby({"b":"x1","A":"x2","a":"x2"})
# print(y.mean())
#         4.按函数分组：
# x=pd.DataFrame({"大":[2000,1000,1002],"中":[500,200,285],"小":[5,4,5],"分组":[-1,2,2]},index=["b","a","c"])
# def f(x):
#     if x>0:
#         return "x1"
#     else:
#         return "x2"
# y=x["分组"].groupby(x["分组"].map(f))
# print(y.sum())
# 8.数据聚合:数据聚合就是对分组后的数据进行计算，产生标量值的数据转换过程。
# 聚合函数(可用于agg内)：
#     1.count：计数
#     2.sum：求和
#     3.mean：求平均值
#     4.median：求中位数
#     5.std：无偏标准差
#     6.var：方差
#     7.min：求最小值
#     8.max：最大值
#     9.Prod：求积
#     10.first：第一个值
#     11.last：最后一个值
#     需要注意的是，在聚合运算中空值不参与计算。
#     常见的聚合运算都由相关的统计函数快速实现，当然也可以自定义聚合运算。要使用自定义的聚合函数，将其传人aggregate或agg方法即可。
# 9.聚合数据(使用时需要将非计算类型字段后移)
# agg、aggregate方法都支持对每个分组应用某个函数，包括Python内置函数或自定义函数。同时，这两个方法也能够直接对DataFrame进行函数应用操作。
# 在正常使用过程中，agg和aggregate函数对DataFrame对象操作的功能基本相同，因此只需掌握一个即可。
# 使用：
# def 使用示例():  # 该函数可忽略
#     datas={"淋巴细胞计数":[2.5,3,2.1,1.3],"白细胞计数":[5.2,5.7,6.4,8.5],"血小板计数":[245.2,325.1,285.4,265.3],
#            "姓名":["小惠","大明","二楞","小芳"],"性别":["女","男","男","女"]}
#     d=pd.DataFrame(datas)
#     y=d[["淋巴细胞计数","白细胞计数"]].agg(["sum","median"])  # 使用agg求出当前数据对应的统计量d[]为格式，["",""]为一个参数
#     #d[["淋巴细胞计数","白细胞计数"]]单独获取这两列，["sum","median"]对这两列调用不同函数，函数直接传入字符串即可
#     print(y)
#     z=d.agg({"淋巴细胞计数":"sum","白细胞计数":"median"})  # 对各字段的不统计量
#     print(z)
#     k=d.groupby("性别")["血小板计数"].agg("sum")  # 分组后计数，也是一样的
#     print(k)
#     k2 = d.groupby("性别",as_index=False)["血小板计数"].agg("sum")  # 分组后，不希望以分组键为索引，加上参数as_index=False
#     print(k2)
# 使用示例()
# 10.分组运算
#     1.transform方法：transform可以将运算(函数、方法)分布到"每一行"。
# datas={"淋巴细胞计数":[2.5,3,2.1,1.3],"白细胞计数":[5.2,5.7,6.4,8.5],"血小板计数":[245.2,325.1,285.4,265.3],
#         "姓名":["小惠","大明","二楞","小芳"],"性别":["女","男","男","女"]}
# d=pd.DataFrame(datas)
# x=d.groupby(["性别","姓名"])["血小板计数"].transform("mean")  # d.groupby(["性别","姓名"])["血小板计数"]=x["血小板计数"]
# print(x)
#         2.apply方法：类似于agg方法，能够将函数应用于"每一列"
# x=d.groupby(["性别","姓名"],group_keys=False)["血小板计数"].apply("mean")
# print(x)
# 注意：
# 1.如果希望返回的结果不以分组键为索引，在groupby中加参数group_keys=False。
# 2.区别：只是使用agg方法能够实现对不同的字段应用不同的函数，而apply则不行。
# 三，数据透视表
# 1.透视表：在Pandas中，除了使用groupby对数据分组聚合实现透视功能外，还可以使用pivot table函数实现。
# 语法：
# pivot_table(data,values=None,index=None,columns=None,aggfunc='mean',
#             fill_value=None,margins=False,dropna=True,margins_name='All')
# 参数解析
# data：    接收DataFrame,表示创建表的数据
# values：  接收string,指定要聚合的数据字段，默认为全部数据
# index：   接收string或list,表示行分组键
# columns： 接收string或list,表示列分组键
# aggfunc； 接收函数,表示聚合函数，默认为mean
# margins： 接收布尔类型,表示汇总功能的开关
# dropna：  接收布尔类型,表示是否删掉全为NaN的列，默认为False
# 示例：
# 创建透视表
# data={"字段一":["A","C","B","A","B","C","B","A","B","C","A","C"],"字段二":[1,3,2,1,3,2,1,3,1,2,3,2],
#       "x":np.random.rand(12),"y":np.random.rand(12)}
# d=pd.DataFrame(data)
# table=d.pivot_table(index="字段一",columns="字段二")
# print(table)
# 分类汇总并求和
# table2=d.pivot_table(index="字段一",columns="字段二",aggfunc="sum")
# print(table2)
# 2.交叉表：交叉表是一种特殊的透视表，主要用于计算分组“频率”。使用Pandas提供的crosstab函数可以制作交叉表。
# 语法：
# crosstab(index,columns,values =None,rownames =None,colnames =None,
#          aggfunc =None,margins=False,dropna=True,normalize=False)
# 参数解析
# index：     接收string或list,表示行索引键，无默认值
# columns：   接收string或list,表示列索引键
# values：    接收array,表示聚合数据，默认为None
# rownames：  表示行分组键名，无默认
# colnames：  表示列分组键名，无默认
# aggfunc：   接收函数,表示聚合函数，默认为None
# margins：   接收布尔,表示汇总功能的开关
# dropna：    接收布尔,表示是否删掉全为NaN的列，默认为False
# normalize： 接收布尔,表示是否对值进行标准化，默认为False
# 示例
# data={"字段一":["A","C","B","A","B","C","B","A","B","C","A","C"],"字段二":[1,3,2,1,3,2,1,3,1,2,3,2],
#       "x":np.random.rand(12),"y":np.random.rand(12)}
# d=pd.DataFrame(data)
# x=pd.crosstab(d["字段一"],d["字段二"],margins=True)  # margins=True添加汇总项
# print(x)
# ==============================
# ==============================
# 四，pandas可视化
# Pandas中集成了Matplotlib中的基础组件，让绘图更加便捷。
import matplotlib.pyplot as plt
# 以下为解决使用中文图例乱码问题(针对windows)
# 显示中文字体
from pylab import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号：有时候;字体更改后;会导致坐标轴中的部分字符无法正常显示;此时需要更改axes.unicode_minus参数
matplotlib.rcParams["axes.unicode_minus"] = False
# ==============================
# ==============================
# plot方法：用于绘制各类图表，默认绘制线形图
# 1.plot:线型图
#       1.对于Series
# s=pd.Series(np.random.normal(size =10))
# x=s.plot()  # 创建图标
# plt.show()  # 显示图像
#       2.对于DataFrame:会为各列绘制一条线，并会创建好图例。
# x=pd.DataFrame({"x":np.random.randint(1,80,size=25),"y":np.random.randint(5,400,size=25)})
# x.plot()
# plt.show()
# 2.柱状图（针对DataFrame）：柱状图一般用来描述各类别之间的关系。只需在plot函数中加参数kind='bar',如果类别较多，可以绘制水平柱状图kind='barh'
# data={"姓名":["小惠","大明","二楞","小芳"],"性别":["女","男","男","女"],"工资":[4280,6582,7582,5450],"工龄":[5,9,12,8]}
# d=pd.DataFrame(data)
# x=d.plot(kind="bar")
# plt.show()
# 水平柱状图
# data2={"工资":[4280,6582,7582,5450],"工龄":[5,9,12,8],"资产":[104257,78451,150241,91243]}
# d2=pd.DataFrame(data2)
# y=d2.plot(kind="barh")
# plt.show()
# 3.直方图、密度图
#     1.直方图用于频率分布，Y轴为数值或比率。绘制直方图，可以观察数据值的大致分布规律。Pandas中的直方图可以通过hist方法绘制。
#     2.核密度估计是对真实密度的估计，其过程是将数据的分布近似为一组核(如正态分布)。通过plot函数的kind='kde'可以进行绘制。
# hilt:方法：
# hist(column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None,
#      sharex=False, sharey=False, figsize=None, layout=None, bins=10, backend=None, legend=False, **kwargs)
# 参数：
# bins：     默认值10。它是指要使用的直方图bin的数量。如果给出整数值, 则它将返回bin +1 bin边缘的计算值。
# grid：     它也是可选参数。用于显示轴线网格线。默认值True。
# figsize：  指要创建的画布大小(以英寸为单位，是一个元组(长，宽))。默认情况下, 它使用matplotlib.rcParams中的值。
# 直方图：
# x=pd.Series(np.random.normal(size=80))  # 产生80行正态分布
# x.hist(bins=20,grid=False)  # 柱子个数为15，柱子高度为出现在柱子两端区间内的数的频率
# plt.show()
# 密度图：
# x.plot(kind="kde")
# plt.show()
# 4.散点图
# wd=pd.DataFrame({"A":[1,2,3,4,5,6,7,8,9],"B":[6,8,10,12,14,16,18,20,22]})
# wd.plot(kind ='scatter',x ='A',y ='B')  # x:x轴，y:y轴
# plt.show()
# ======================
# 五，Pandas数据载入与预处理
# ======================
# 1.文本（txt）文件读取
# pd.read_table("文件路径",sep='\t',header='infer',names=None,index_col =None,dtype=None,engine=None,nrows =None)
# 2.读取csv文件
# pd.read_csv("文件",sep='\t',header='infer',names =None,index_col =None,dtype=None,engine =None,nrows =None)
# 参数：
# filepath：   接收string,代表文件路径，无默认
# sep：        接收string,代表分隔符。read_csv默认为“,”,read_table默认为制表符“[Tab]”,如果分隔符指定错误，在读取数据的时候，每一行数据将连成一片
# header：     接收int或sequence,表示将某行数据作为列名，默认为infer,表示自动识别
# names：      接收array,表示列名，默认为None
# index_col：  接收int、sequence或False,表示索引列的位置，取值为sequence则代表多重索引，默认为None
# dtype：      接收dict,代表写入的数据类型(列名为key,数据格式为values),默认为None
# engine：     接收c或者python,代表数据解析引擎，默认为c
# nrows：      接收int,表示读取前n行，默认为None
# 示例：
# x=pd.read_table("data.txt",sep=",")
# print(x)
# y=pd.read_table("data_csv.csv",sep=",")
# print(y)
# 2.文本文件的储存
# 结构化数据可以通过Pandas中的to_csv函数实现以CSV文件格式存储文件
# DataFrame.to_csv("文件路径",sep =',',na_rep="",columns =None,header =True,index=True,index_label =None,mode='w',encoding =None)
# y.to_csv("save_csv.csv")
# 3.读/写excel文件
# read_excel方法：可以读取xls(微软)和xlsx(wps)文件
# pd.read_excel("文件路径",sheetname,header =0,index_col =None,names =None,dtype)
# 参数：
# sheetname:接收字符串、整形。代表Excel表内的数据的分表(excel中其中一个表)位置，默认为0
# header:接收字符串、seq(列表、元组..)，表示将某行数据作为列名，默认为infer，表示自动识别
# names:接收int,sequence或者False,表示索引列的位置，取值为sequence则代表多重索引，默认为None
# index_col:接收int、sequence或者False,表示索引列的位置，取值为sequence则代表多重索引，默认为None
# dtype:接收dict,代表写入的数据类型(列名为key,数据格式为values),默认为None
# 示例：读取Excel文件
# xls=pd.read_excel("data.xls","Sheet1")
# print(xls)
# 4.excel文件的储存
# pd.to_excel方法(xls文件存在问题不要导出为xls)
# DataFrame.to_excel("文件路径",sheet_name=None,na_rep="",header =True,index=True,index_label =None,mode='w',encoding =None)
# 注：sheetname为保存到的工作表名，默认为Sheet1
# 示例：
# xls.to_excel("save_data.xlsx",sheet_name="Sheet1")
# 5.==========合并数据=======在实际的数据分析中，可能有不同的数据来源，因此，需要对数据进行合并处理。
# 5.1merge数据合并（类似msql中的join）
# merge(left,right,how="inner",on=None,left_on=None,right_on=None,left_index=False,right_index=False,sort=False,
#       suffixes=("_x","_y"),copy=True,indcator=False,validate=None)
# 参数：
# left：合并左侧DataFrame
# right：合并右侧DataFrame
# how:连接方法（inner,left,right,outer）
# on:用于链接的列名（有相同列时默认为相同列）可以右多个列用，[]
# left_on:左侧DataFrame中用于连接键的列
# riht_on:右侧DataFrame中用于连接键的列
# left_index:左侧DataFrame中行索引作为连接键
# right_index:右侧DataFrame中行索引作为连接键
# sort:合并后会对数据排序，默认为True
# suffixes:修改重复名
# 示例：
# j1=pd.DataFrame({"IP":["12","123","654","8","65"],"time":["0.5","1","0.75","85","85"]})
# j2=pd.DataFrame({"IP":["12","123","654","8","65"],"out_time":["42","2","75","8.5","84.5"]})
# j3=pd.merge(j1,j2)
# print(j3)
# 5.2========concat方法（可以对Seriesj进行连接,参数自己看）==========
# 示例1（连接Series）
# s1=pd.Series([1,2,3],index=["a","b","c"])
# s2=pd.Series([10,11,12],index=["b","z","y"])
# s3=pd.Series([50,60],index=["yes","no"])
# s4=pd.concat([s1,s2,s3])
# print(s4)
# 示例2：（连接DataFrame）
# j11=pd.DataFrame({"IP":["12","123","654","8","65"],"time":["0.5","1","0.75","85","85"]})
# j22=pd.DataFrame({"IP":["12","123","654","8","65"],"out_time":["42","2","75","8.5","84.5"]})
# j33=pd.concat([j11,j22])
# print(j33)
# 5.3=========combine_fiest方法（合并的DataFrame存在重复索引，只能用它，相当于去重）
# x1=pd.DataFrame({0:[1,2],1:[2,3]},index=["a","b"])
# x2=pd.DataFrame({0:[1,2,3,4],1:[2,3,4,5]},index=["a","b","c","d"])
# x3=x1.combine_first(x2)
# print(x3)
# 6.========数据清洗=============
# 6.1=========检测与处理缺失值===========
# ==========缺失值的检测统计===========
# 6.1.1===缺失值的检测：isnull()函数判断是否是缺失值，注意python内置的None同等于缺失值
# 6.1.2===缺失值的统计：isnull().sum()
# 示例：检测缺失值
from numpy import nan  # 导入NA值使用
# se=pd.Series([100,200,300,400,None,nan])
# da=pd.DataFrame({0:[None,"df",nan],1:[1,5,nan]},index=["a","b","c"])
# x=se.isnull()
# da1=da.isnull()
# print(x)
# print(da1)
# 示例：统计缺失值
# x1=se.isnull().sum()
# da2=da1.isnull().sum()
# print(x1)
# print(da)
# print(da2)
# 6.2======缺失值的处理：dropna方法
# 数据.dropna(axis=0,how="any",thresh=None,subset=None,inplace=False)
# 参数：
# axis：默认为axis=0,当某行出现缺失值时，将该行丢弃并返回；当axis=1,且某列出现缺失值时，将该列丢弃
# how：确定缺失值个数，缺省时how='any',how='any'表明只要某行有缺失值就将该行丢弃，how='all'表明某行全部为缺失值才将其丢弃
# thresh：阈值设定，当行列中非缺失值的数量少于给定的值就将该行丢弃
# subset：部分标签中删除某行列，例如subset=['a','d'],即丢弃子列ad中含有缺失值的行
# inplace：bool取值，默认为False,当inplace=True,即对原数据操作，无返回值
# 注：对于Series返回一个仅含非空数据和索引值的Series
# x=pd.Series([1,2,nan,4])
# y=pd.DataFrame({0:[1,2],1:[3,nan]},index=["a","b"])
# print(x.dropna())
# print(y.dropna())

