import requests,re,time,os,parsel,random

def 日志():
    变量名1=" %(message)s : 时间:%(asctime)s - 日志名字:%(name)s - 日志等级:%(levelname)s - 模块:%(module)s"
    变量名2="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"
    变量名3=" 终端显示: %(message)s : -%(asctime)s - %(name)s - %(module)s"
                                       # 日志输出行数
    LOGGING_DIC = {
        "version":1,
        "disable_existing_loggers":False,
        "formatters": {
            "自定义名称1":{
                "format":变量名1},
            "自定义名称2":{
                "format":变量名2},
            "自定义名称3":{
                "format":变量名3},},
        "handlers":{
            "打印到终端（自定义名称）":{
                "level":10,  # 日志级别数字或大写的日志级别都可以
                "class":"logging.StreamHandler",  # 打印到屏幕
                "formatter":"自定义名称3"},  # 自定义名称1或3

            "打印到文件的日志2(自定义名称)":{
                "level":10,
                "class":"logging.FileHandler",  # 保存到文件
                "formatter":"自定义名称1",  # 自定义名称1或3
                "filename":"D:\爬虫/基本日志.log",  # 文件路径（换路径不能和其他的log文件在一个文件夹）
                "encoding":"utf-8",},  # 指定字符编码
        },
        "loggers":{
            "使用日志":{
                "handlers":["打印到终端（自定义名称）","打印到文件的日志2(自定义名称)"],
                "level":10,
                "propagate":False,},  # 默认为True False最好 不用改
            },
    }

    from logging import config,getLogger
    config.dictConfig(LOGGING_DIC)  # 拿到字典 如果在不同文件为 文件.LOGGING_DIC
    拿到日志产生者=getLogger("使用日志")  # 拿到日志产生者
    拿到日志产生者.info("日志已记录")  # 打印日志也就是debug("调试")info("消息")warning("警告")error("错误")critical("严重")
# /////////////////////////////////////////////////////
def 次元():
    页数=random.randint(200,500)
    print("当前页为",页数,"页")
    u="http://ciyuandao.com/photo/show/134{页数}".format(页数=页数)
    # u=input("网页:")
    # u="http://ciyuandao.com/photo/show/133161"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) Applewebkit/537.36(KHTWL,like Gecko) chrome/58.0.3029.110 Safari/537.3"}  # 伪造用户
    response = requests.get(u, headers)
    print("======================================响应中=============第三方浏览器————《《chrome》》====================")
    # print(response.request.headers)
    time.sleep(1)
    html = response.text
    # print(html)
    # print("===================获取数据中======================")
    # # ====================================解析网页=================================

    # x = re.findall(r'<div class="article mbottom10">(.*?)</div>', html)[-1]
    x=random.randint(0,999999)
    if not os.path.exists(x):
        os.mkdir("D:\爬虫\次元/{x}".format(x=x))
    print("创建成功")
    # print("================解析网页中====================")
    urls = re.findall('<a href="javascript:;"><img src="(.*?)\?x-oss-process=image/auto-orient,1/resize,m_lfit,w_1440/quality,q_100"></a>', html)
    print(urls)
    # print("=====================保存中，这会花费一点时间===================")
    m = 1
    for url in urls:
        time.sleep(1)
        print("读取到的图片", m, "==", url,)
        print("==================================================")
        m += 1
        name = url.split("/")[-1]
        response = requests.get(url, headers=headers)
        # with open("D:/qq/{name}".format(name=name), 'ab') as f:
        with open("D:/爬虫/次元/{x}/{name}".format(x=x,name=name), 'ab') as f:
            f.write(response.content)
    print("===爬取成功===")
    print("创建了{x}文件夹".format(x=x))
    日志()
    response.close()
# ////////////////////////////////////////////////////////
def 绝对():
    页数=random.randint(1,163)
    print("当前页为",页数,"页")

    # 页数=input("网页数允许在2-163:")
    # 目标网页=input("网页:")
    目标网页="https://www.jdlingyu.com/tuji/mzitu/page/{页数}".format(页数=页数)
    伪造请求方 ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) Applewebkit/537.36(KHTWL,like Gecko) chrome/58.0.3029.110 Safari/537.3"}
    #
    # 发送请求请求数据
    网页请求 = requests.get(目标网页, headers=伪造请求方)  # （网页，headers=请求方）发送网页请求

    网页请求数据=网页请求.text  # .text获取对象数据
    #
    # 解析数据（用xpath）
    解析数据=parsel.Selector(网页请求数据)  # 转换类型（xpath不能对字符串解析只有正则而表达才可以）
    # 需要提取相册标题及详情页的地址
    li标签=解析数据.xpath('//div[@id="post-list"]/ul/li')  # 获取所有li标签
    print(li标签)
    ll=1
    for li in li标签:

        time.sleep(2)
        相册标题=li.xpath('.//h2/a/text()') .get() # 获取相册标题 .get()是从对象中提取数据
        相册链接=li.xpath('.//h2/a/@href') .get() # 获取相册链接 .get()是从对象中提取数据
        if not os.path.exists('D:/爬虫/绝对/' + 相册标题):
            os.mkdir('D:/爬虫/绝对/' + 相册标题)
        # print(相册标题,相册链接)

    # 对相册链接进行发送网页请求
        相册链接数据=requests.get(url=相册链接,headers=伪造请求方)
        相册链接数据对象数据=相册链接数据.text  # 详情页数据

        # 解析详情页数据
        详情页数据转换=parsel.Selector(相册链接数据对象数据)
        详情页数据转换详解析=详情页数据转换.xpath('//div[@class="entry-content"]//img/@src').getall()#详情页所有图片链接
        # print(详情页数据转换详解析)
        for 数据 in 详情页数据转换详解析:
            # time.sleep(1)
            二进制数据=requests.get(url=数据,headers=伪造请求方)
            #
            # 数据保存
            图片名称=数据.split('/')[-1]
            # print(图片名称)
            with open ('D:/爬虫/绝对/{文件夹}/{图片名称}'.format(文件夹=相册标题,图片名称=图片名称),mode='wb') as f:
                f.write(二进制数据.content)  # content转为二进制
                二进制数据.close()
                print("\r保存成功  图片", 图片名称, "已保存", ll, "张", end="")
                ll += 1
    日志()
    print("===已完成=========已完成=====已完成======已完成======已完成======已完成====已完成=====已完成=====")
# ////////////////////////////////////////////////////////
def 唯美():
    网页 = "https://www.vmgirls.net/18618.html"
    伪造请求方 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) Applewebkit/537.36(KHTWL,like Gecko) chrome/58.0.3029.110 Safari/537.3"}
    网页请求 = requests.get(网页, headers=伪造请求方)  # （网页，headers=请求方）发送网页请求
    # print(网页请求.text)  # 用于测试是否获取到网页数据
    网页数据 = 网页请求.text

    # 二 解析网页
    # 1  解析文件夹名字
    需要的文件数据 = '<h1 class="post-title mb-3">(.*?)</h1>'  # 网页标题数据
    文件夹名字=re.findall(需要的文件数据, 网页数据)[-1]
    # a = "my name is {name},my age is {age}".format(name=name, age=age)
    if not os.path.exists("D:/爬虫/唯美/文件夹名字"):  # 判断文件是否存在
        os.mkdir("D:/爬虫/唯美/{文件夹名字}".format(文件夹名字=文件夹名字))  # 没有就创建
    # (.*?)代替图片(.*?)内的数据将被提取出来 .*?代替其他标签不会被提取
    需要的图片数据 = '<a rel="nofollow" href="(.*?)" alt=".*?" title=".*?">'
    # '<a rel="nofollow" href="(.*?)" alt=".*?" title=".*?">''<img alt=".*?" src="(.*?)" alt=""/>'
    匹配结果 = re.findall(需要的图片数据, 网页数据)  # （网页）解析网页专用（匹配规则，匹配对象）
    print(匹配结果)

    # 三 保存图片
    for 最终数据 in 匹配结果:
        time.sleep(0)  # 指定速度
        图片名=最终数据.split('/')[-1]  # 分割提取图片名
        网页请求 = requests.get(最终数据, headers=伪造请求方)  # 获取图片内容（拿到图片下载地址）
        # 打开文件
        with open("D:/爬虫/唯美/{文件夹名字}".format(文件夹名字=文件夹名字) + '/' + 图片名,"wb") as f:  # "/"表示目录的替换
            f.write(网页请求.content)  # content二进制
    网页请求.close()
    日志()
# /////////////////////////////////////////////////////
def 次元小镇():
    # 尾号=input("请输入页面标识码:")
    # # 尾号="109564"
    # web="https://dimtown.com/{尾号}.html".format(尾号=尾号)
    web="https://dimtown.com/123661.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) Applewebkit/537.36(KHTWL,like Gecko) chrome/58.0.3029.110 Safari/537.3"}  # 伪造用户
    response = requests.get(web, headers)
    print("======================================响应中=============第三方浏览器————《《chrome》》====================")
    # print(response.request)
    time.sleep(1)
    html = response.text
    # print(html)
    print("===================获取数据中======================")
    # # ====================================解析网页=================================
    file=random.randint(0,999999)
    if not os.path.exists(file):
        os.mkdir("D:\爬虫\次元小镇/{file}".format(file=file))
    print("文件夹创建成功")
    print("================解析网页中====================")
    urls = re.findall(r'<img decoding=".*?" src="(.*?)"  alt=".*?"/>', html)
    print(urls)
    print("=====================保存中，这会花费一点时间===================")
    m = 1
    for url in urls:
        time.sleep(1)
        print("读取到的图片", m, "==", url,)
        print("==================================================")
        m += 1
        name = url.split("/")[-1]
        response = requests.get(url, headers=headers)
        # with open("D:/qq/{name}".format(name=name), 'ab') as f:
        with open("D:/爬虫/次元小镇/{file}/{name}".format(file=file,name=name), 'ab') as f:
            f.write(response.content)
    print("===爬取成功===")
    print("创建了{file}文件夹".format(file=file))
    # 日志()
    response.close()
# ////////////////////////////////////////////////
# 网络  f5刷新
# ///////////////////////////////////////////////
# 次元()
# 绝对()
# 唯美()
# 次元小镇()