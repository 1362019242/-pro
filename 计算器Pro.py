# coding=utf-8
print("欢迎使用老唐写的超级计算器Pro")
jisuan = int(input("请告诉我你要执行什么运算或者其他选项(1.加法2.减法3.乘法4.除法5.关于6.更新日志):"))
if jisuan == 1:
    shuju = int(input("请输入相加的数："))
    shuju2 = int(input("请再次输入相加的数："))
    he = shuju + shuju2
    print("运算结果为：", he)
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
elif jisuan == 5:
    print("名称：计算器Pro")
    print("版本：3.0.0")
    print("开发者：老唐")
elif jisuan == 6:
    print("3.0.0的更新内容")
    print("1.优化部分代码")
    print("2.新增关于和更新日志")
    print("3.增加输入错误提示")
else:
    print("输入错误程序退出")