# coding=utf-8
while 1 == 1: #可以使程序一直运行
    jisuan = int(input('''
        ╔*****************老唐的超级计算器**************╗
        *                                            *
        *   =============== 功能菜单 ===============   * 
        *                                            *
        *   1 加法                                    *
        *   2 减法                                    *
        *   3 乘法                                    *
        *   4 除法                                    *
        *   5 更新日志                                 *
        *   6 关于                                    *
        *   7 其他                                    *
        *   8 闰年判段                                 *                               
        *  ========================================  * 
        *                                            *
        ╚********************************************╝
        '''))  # 用户输入
    if jisuan == 1: #判断用户选择的是什么运算
        shuju = int(input("请输入相加的数："))#执行运算
        shuju2 = int(input("请再次输入相加的数："))
        he = shuju + shuju2 #算法部分
        print("运算结果为：", he)#结果

    elif jisuan == 2:
        shuju = int(input("请输入相减的数："))
        shuju2 = int(input("请再次输入相减的数："))
        he = shuju - shuju2
        print("运算结果为：", he)

    elif jisuan == 3:
        shuju = int(input("请输入相乘的数："))
        shuju2 = int(input("请再次输入相乘的数："))
        he = shuju * shuju2
        print("运算结果为：", he)

    elif jisuan == 4:
        shuju = int(input("请输入相除的数："))
        shuju2 = int(input("请再次输入相处的数："))
        he = shuju / shuju2
        print("运算结果为：", he)

    elif jisuan == 5:#更新日志
        print("**********4.3.0的更新内容**********")
        print("          1.新增闰年判断            ")
        print("          2.单位换算持续更新中       ")
        print("********* 3.优化算法顺带修复bug******")

    elif jisuan == 6:#关于软件
        print("**********名称：计算器Pro(内测版)**********")
        print(             "版本：4.3.0"                )
        print("*************开发者：老唐****************")

    elif jisuan == 8:#判断闰年算法
        try:
            year=int(input("请输入一个年份："))
            if (year%4==0) and (year%100 !=0) or (year%400)==0:
                print("{}年是闰年".format(year))
            else:
                print("{}年不是闰年".format(year))
        except:
            print("您输入有误！")

    elif jisuan == 7: #二级菜单部分
        qt = int(input('''
        ╔*****************老唐的超级计算器*****************╗                                                 
        *                                              *
        *   =============== 功能菜单 ===============     *
        *                                              *
        *   0 单位换算                                   *
        *                                              *
        *  ========================================    *
        *                                              *
        ╚**********************************************╝
        '''))

        if qt == 0: #三级菜单部分
            hs = int(input(''' 
        ╔*****************老唐的超级计算器*****************╗                                                 
        *                                              *
        *   =============== 功能菜单 ===============     *
        *                                              *
        *   1 距离换算                                   *
        *   2 时间换算                                   *
        *   3 温度换算                                   *
        *                                              *
        *  ========================================    *
        *                                              *
        ╚*********************************************╝
        '''))
        if hs == 1:#换算的算法部分
            jl = int(input("请输入距离：（米）"))
            jl2 = 1000
            he = jl / jl2
            print("转换成功数据为",he,"(km)")
        elif hs == 2:
            sj = int(input("请输入时间：（秒）"))
            sj2 = 60
            he = sj / sj2
            print("换算成功数据为(分)",he)
        elif hs == 3:#数据的算法部分
            TempStr = input("请输入一个带有符号的温度值：")
            if TempStr[-1] in ['C', 'c']:
                f = eval(TempStr[:-1]) * 1.8 + 32
                print("转换后温度是{:.2f}F".format(f))
            elif TempStr[-1] in ['F', 'f']:
                c = (eval(TempStr[:-1]) - 32) / 1.8
                print("转换后温度是{:.2f}C".format(c))
            else:
                print("输入错误")
else:
    print("输入错误程序退出") #Error部分输入错误程序退出



