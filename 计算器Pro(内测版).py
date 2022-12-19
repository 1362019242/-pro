import math
import datetime
import time
import re
import sys
import os
import tkinter
from tkinter.messagebox import *
import requests
from lxml import etree


while True:  # 可以使程序一直运行
    try:
        Menu = int(input('''
         ╔*****************老唐的计算器Pro**************╗
         *                                             *
         *   =============== 功能菜单 ===============   * 
         *   1 混合计算               11.亲戚称呼计算器   *
         *   2 更新日志               12.矩阵运算        *
         *   3 关于                                    *
         *   4 其他                                    *
         *   5 闰年计算                                 *
         *   6 房贷计算                                *
         *   7 年龄计算                                *
         *   8 汇率计算                                *
         *   9 BMI计算                                 *
         *   10 退出程序                                *
         *  ========================================  *
         *                                            *
         ╚********************************************╝
        '''))  # 用户输入

        if Menu == 1:  # 混合运算算法部分

            __author__ = "Colby"


            def format_mark(express):
                '''
                def替换过程中可能出现一些组合符号，
                机器无法辨别，此函数负责处理这些组合符号
                :param express:
                :return:
                '''
                express = express.replace('+-', '-')
                express = express.replace('-+', '-')
                express = express.replace('++', '+')
                express = express.replace('--', '+')
                express = express.replace('*+', '*')
                express = express.replace('+*', '*')
                express = express.replace('+/', '/')
                express = express.replace('/+', '/')
                return express


            def com_jiajian(express):
                '''
                :param express:
                :return:
                '''
                expr = express
                sub_expr = re.search(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", expr)
                if not sub_expr:
                    return expr
                else:
                    sub_expr2 = sub_expr.group()
                    # print('sub_expr1',sub_expr1,'19行结果express:',div_express)
                if len(sub_expr2.split('+')) > 1:
                    n1, n2 = sub_expr2.split('+')
                    result = float(n1) + float(n2)
                else:
                    n1, n2 = sub_expr2.split('-')
                    result = float(n1) - float(n2)
                re_sub_expr = re.sub(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", str(result), expr, count=1)
                # 反复调用除法
                print('加减运算：', re_sub_expr)
                bb = com_jiajian(str(re_sub_expr))
                return bb


            def com_chengchu(expr_div):
                '''
                :param expr_div:
                :return:
                '''
                expr = expr_div
                sub_expr = re.search(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*", expr)
                if not sub_expr:
                    return expr
                else:
                    sub_expr2 = sub_expr.group()
                    if len(sub_expr2.split('/')) > 1:
                        n1, n2 = sub_expr2.split('/')
                        result = float(n1) / float(n2)
                    if len(sub_expr2.split('*')) > 1:
                        n1, n2 = sub_expr2.split('*')
                        result = float(n1) * float(n2)
                    else:
                        # 只计算乘除，加减直接pass，放入加减函数执行
                        pass
                re_sub_expr = re.sub(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*", str(result), expr, count=1)
                # 反复调用除法
                print('乘除运算：', re_sub_expr)
                bb = com_chengchu(format_mark(re_sub_expr))
                return bb


            def compute(express):
                express = com_chengchu(format_mark(express))
                express = com_jiajian(format_mark(express))
                return express


            def delkuohao(express):
                # 检测表达式是否存在括号，如果存在就去括号，否则直接执行
                res = re.compile(r'[()]')
                sub_expr1 = re.search('(\([\+\-\*\/\.0-9]+\))', express)
                if not sub_expr1:
                    return express
                else:
                    sub_expr1 = sub_expr1.group()
                    # delkuohao(express)
                    # 匹配括号，将计算结果替换到表达式
                    sub_expr2 = sub_expr1[1:len(sub_expr1) - 1]
                    sub_expr3 = compute(sub_expr2)
                    sub_expr3 = re.sub('(\([\+\-\*\/\.0-9]+\))', str(sub_expr3), express, count=1)
                    print('括号运算：', sub_expr3)
                    delkuohao_expr = delkuohao(format_mark(sub_expr3))
                return delkuohao_expr


            if __name__ == "__main__":
                # while True:
                # express=input("请输入要计算的表达式：")
                print('\n================================')
                print('\033[33m 混合运算计算器\033[0m')
                print('================================')
                # express ='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
                while True:
                    express = input('\033[32m请输入表达式,规范点哦 | (退出:q)\033[0m')
                    express = re.sub('\s*', '', express)
                    if len(express) == 0:
                        continue
                    elif express == 'q' or express == 'Q':
                        print('已退出')
                        break
                    elif re.search('[^0-9\.\-\+\*\/\(\)]', express):
                        print('\033[31m 不是有效的算数表达式哦，请重新输入!!!\033[0m')
                    else:
                        express = express.replace(' ', '')
                        print('您输入的表达式：', express)
                        '''调用去除括号的函数'''
                        express2 = delkuohao(express)
                        # 删除括号
                        express2 = compute(format_mark(express2))
                        # 删除括号后再调用一次计算函数
                        print('\033[31m表达式:%s' % express, '=', str(express2), '\033[0m')



        elif Menu == 2:  # 更新日志
            window = tkinter.Tk()
            window.withdraw()  # 退出默认 tk 窗口
            result = showinfo('2022.12.2 更新内容', '1.重大更新：矩阵运算\n'
                                                    '2.汇率算法升级\n')
            print(f'提示: {result}')



        elif Menu == 3:  # 关于软件
            window = tkinter.Tk()
            window.withdraw()  # 退出默认 tk 窗口

            result = showinfo('关于软件', '版本：7.1.0\n''开发者：老唐')
            print(f'提示: {result}')


        elif Menu == 4:  # 二级菜单部分
            Menu2 = int(input('''
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

            if Menu2 == 0:  # 三级菜单部分
                hs = int(input(''' 
            ╔*****************老唐的超级计算器*****************╗                                                 
            *                                              *
            *   =============== 功能菜单 ===============     *
            *                                              *
            *   1 距离换算           6.面积换算               *
            *   2 时间换算                                   *
            *   3 温度换算                                   *
            *   4 重量换算                                   *
            *   5 进制换算                                   *
            *  ========================================    *
            *                                              *
            ╚*********************************************╝
            '''))
            if hs == 1:  # 换算的算法部分
                jl = int(input("请输入距离：（米）"))
                jl2 = 1000
                he = jl / jl2
                print("转换成功数据为", format(he), "(km)")

            elif hs == 2:
                second = int(input("请输入秒数:"))
                hour = second // 3600
                minute = second % 3600 // 60
                second1 = second % 60
                print("输入秒换成时间是", hour, ":", minute, ":", second1)

            elif hs == 3:  # 数据的算法部分
                TempStr = input("请输入一个带有符号的温度值：")
                if TempStr[-1] in ['C', 'c']:
                    f = eval(TempStr[:-1]) * 1.8 + 32
                    print("转换后温度是{:.2f}F".format(f))
                elif TempStr[-1] in ['F', 'f']:
                    c = (eval(TempStr[:-1]) - 32) / 1.8
                    print("转换后温度是{:.2f}C".format(c))
                else:
                    print("输入错误")

            elif hs == 4:  # 重量换算的算法
                Quality = input("请输入带有符号的质量值:")
                if Quality[-1] in ['T', 't']:
                    Kg = (eval(Quality[0:-1])) * 1000
                    print("转换后的质量是{:.2f}Kg".format(Kg))
                elif Quality[-1] in ['G', 'g']:
                    T = (eval(Quality[0:-2])) * 0.001
                    print("转换后的质量是{:.3f}T".format(T))
                else:
                    print("输入格式错误")

            elif hs == 5:  # 进制转换算法
                dec = int(input("输入数字："))
                print("十进制数为：", dec)
                print("转换为二进制为：", bin(dec))
                print("转换为八进制为：", oct(dec))
                print("转换为十六进制为：", hex(dec))

            elif hs == 6:
                area = input("请输入带有单位的面积值:")  # 输入示例 1亩/1平方千米
                if area[-1] in ["平", "方", "千", "米"]:  # 判断字符尾单位是否为平方千米
                    M = (eval(area[0:-4])) * 1500
                    print("转换后的面积值是:{:.2f}亩".format(M))
                elif area[-1] in ["亩"]:  # 判断字符尾单位是否为亩
                    QM = (eval(area[0:-1])) / 1500
                    print("转换后的面积值是:{:.7f}平方千米".format(QM))
                else:
                    print("输入格式错误")  # 做好格式输入错误提示

        elif Menu == 5:  # 判断闰年算法
            try:
                year = int(input("请输入一个年份："))
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400) == 0:
                    print("{}年是闰年".format(year))
                else:
                    print("{}年不是闰年".format(year))
            except:
                print("您输入有误！")
        elif Menu == 6:  # 房贷计算的算法
            years = int(input("请输入贷款期限（年）："))
            if years > 5:
                print("请输入贷款类型：1商业贷款，2公积金贷款")
                choic = int(input("请输入贷款类型:"))
                if choic == 1:
                    r = 4.90 / 100
                elif choic == 2:
                    r = 3.25 / 100
                if 0 < years <= 5:
                    print("请输入贷款类型：1商业贷款，2公积金贷款")
                    choic = int(input("请输入贷款类型:"))
                    if choic == 1:
                        r = 4.75 / 100
                    elif choic == 2:
                        r = 2.75 / 100
                    else:
                        print('输入错误')

                mr = r / 12  # 月利率
                m = 12 * years  # 贷款总月数
                p = int(input('请输入贷款本金：'))  # 贷款本金
                mrp = mr * p  # 月利息

                mrp1 = p * mr * pow(1 + mr, m) / (pow((1 + mr), m) - 1)  # 每月月供参考
                total = mrp1 * years * 12  # 还款总额
                li = total - p
                print('您的每月月供参考为：', mrp1)
                print('您的还款总额为：', total)
                print('您需还的利息为：', li)

        if Menu == 7:
            birthday = datetime.date(  # 输入生日
                year=int(input('请输入你的出生年份：')),
                month=int(input('请输入你的出生月份：')),
                day=int(input('请输入你的出生日期：'))
            )
            today = datetime.date.today()  # 现在的日期
            age = round((today - birthday).days / 365, 7)
            # 今天的日期与生日相减的天数除以365得出年龄

            birth = datetime.date(  # 最近的生日
                year=today.year,  # 今年
                month=birthday.month,
                day=birthday.day
            )
            if birth < today:  # 如果今年过过了
                birth = datetime.date(
                    year=today.year + 1,  # 算明年的
                    month=birthday.month,
                    day=birthday.day
                )
            print(f"今天是{today.year}年{today.month}月{today.day}日")
            print(f"你今年大约{age}岁了！")
            print(f"距离你的生日还有{(birth - today).days}天")

        elif Menu == 8:
            # @CSDN      :  https://blog.csdn.net/weixin_47723732
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
            }
            url = "https://www.huilv.cc/USD_CNY/"


            def Get_huilv(url, headers1):
                res = requests.get(url=url, headers=headers1, timeout=2)
                # print(res.status_code)#打印状态码
                html = etree.HTML(res.text)
                USD_VS_RMB_0 = html.xpath('//div[@id="main"]/div[1]/div[2]/span[1]/text()')
                for a in USD_VS_RMB_0:
                    b = a
                USD_VS_RMB_1 = float(b)
                print("实时汇率为：{}".format(USD_VS_RMB_1))

                currency_str_value = 0
                while currency_str_value != "":
                    USD_VS_RMB = float(str(USD_VS_RMB_1))
                    # 输入带单位的货币金额
                    currency_str_value = input('请输入带单位货币的金额(cny和usd)： ')
                    # 获取货币单位
                    unit = currency_str_value[-3:].upper()  # 第一次判断
                    if unit == 'CNY':
                        exchange_rate = 1 / USD_VS_RMB
                        string = "美元"
                    elif unit == 'USD':
                        exchange_rate = USD_VS_RMB
                        string = "元"
                    else:
                        exchange_rate = -1
                    if exchange_rate != -1:
                        in_money = eval(currency_str_value[0:-3])
                        # 使用lambda定义函数
                        convert_currency2 = lambda x: x * exchange_rate
                        # 调用lambda函数
                        out_money = convert_currency2(in_money)
                        print('转换后的金额是：{} {} '.format(out_money, string))
                    else:
                        print('无法计算')


            Get_huilv(url, headers)

        elif Menu == 9:
            print('----欢迎使用BMI计算程序----')
            name = input('请键入您的姓名:')
            height = eval(input('请键入您的身高(m):'))
            weight = eval(input('请键入您的体重(kg):'))
            gender = input('请键入你的性别(F/M)')
            BMI = float(float(weight) / (float(height) ** 2))
            # 公式和算法
            if BMI <= 18.4:
                print('姓名:', name, '身体状态:偏瘦')
            elif BMI <= 23.9:
                print('姓名:', name, '身体状态:正常')
            elif BMI <= 27.9:
                print('姓名:', name, '身体状态:超重')
            elif BMI >= 28:
                print('姓名:', name, '身体状态:肥胖')

            nowtime = (time.asctime(time.localtime(time.time())))  # 获取时间
            if gender == 'F':
                print('感谢', name, '女士在', nowtime, '使用本程序,祝您身体健康!')
            if gender == 'M':
                print('感谢', name, '先生在', nowtime, '使用本程序,祝您身体健康!')

        elif Menu == 10:
            sys.exit('程序已退出 欢迎下次使用')

        elif Menu == 11:
            # 首先声明全局变量，十个基本称呼及基本关系代号
            call_list = ['女儿', '儿子', '丈夫', '妻子', '哥哥', '弟弟', '姐姐', '妹妹', '爸爸', '妈妈']
            code_list = ['N', 'Z', 'F', 'Q', 'G', 'D', 'J', 'S', 'B', 'M']


            def input_check(str_in):
                """
            正则表达式检查输入是否合法
            :param str_in: 中文字符串输入
            :return bool: 返回是否满足输入要求的逻辑值
                """
                correct_enter = re.compile('^([女儿|儿子|丈夫|妻子|老公|老婆|哥哥|弟弟|姐姐|妹妹|爸爸|妈妈][的]?)*$')
                return correct_enter.match(str_in)


            def input_handle(str_in):
                """
                中文输入的基本分词
                :param str_in: 符合输入要求的中文字符串
                :return seq: 返回中文字符串对应的完整代号序列字符串
                """
                # 补充几个常用的称呼提升输入多样性
                call_addition1 = ['老公', '老婆', '']
                call_addition2 = ['F', 'Q', '']
                call_dic = dict(zip(call_list + call_addition1, code_list + call_addition2))  # 中文转换识别字典
                str_in_split = str_in.strip().split("的")  # 简单粗暴的按“的”分词
                return ''.join([call_dic[i] for i in str_in_split])


            def gender_check(seq_in):
                """
                性别判定
                :param seq_in:
                :return: 返回各个代号的性别，1男，0女
                """
                gender_dic = dict(zip(code_list, [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]))
                return gender_dic[seq_in[-1]]


            def seq_simplify(seq_in):
                """
                @@关键算法@@，替换序列中48种无效或重复的代号组合，防止出现自递归迭代
                :param seq_in:完整序列
                :return:返回已处理好的有效代号组合
                """
                # 可直接替换的32组可折叠代号组合
                folded_call = ['NG', 'ND', 'NJ', 'NS', 'ZG', 'ZD', 'ZJ', 'ZS', 'FN', 'FZ',
                               'QN', 'QZ', 'GG', 'GJ', 'GB', 'GM', 'DD', 'DS', 'DB', 'DM',
                               'JG', 'JJ', 'JB', 'JM', 'SD', 'SS', 'SB', 'SM', 'BQ', 'MF',
                               'FQ', 'QF']
                replaced_call_1 = ['Z', 'Z', 'N', 'N', 'Z', 'Z', 'N', 'N', 'N', 'Z',
                                   'N', 'Z', 'G', 'J', 'B', 'M', 'D', 'S', 'B', 'M',
                                   'G', 'J', 'B', 'M', 'D', 'S', 'B', 'M', 'M', 'B',
                                   '', '']
                # 需判断前点性别的16组可折叠代号组合
                wrong_call = ['GD', 'GS', 'DG', 'DJ', 'JD', 'JS', 'SG', 'SJ',
                              'NB', 'NM', 'ZB', 'ZM', 'BN', 'BZ', 'MN', 'MZ']
                replace_call_2 = ['D', 'S', 'G', 'J', 'D', 'S', 'G', 'J',
                                  'F', 'Q', 'F', 'Q', 'S', 'D', 'M', 'D']
                replace_dic = dict(zip(folded_call + wrong_call, replaced_call_1 + replace_call_2))  # 2种拼成一个字典

                while True:
                    k = 0  # 设置循环跳出判断标志
                    for x, y in replace_dic.items():
                        i = seq_in.find(x)
                        # 只要有无效代号就进入判定及处理
                        if i != -1:
                            k += 1
                            # 把三种处理方式通过字典与列表的分离而放到一块
                            if x in folded_call:
                                seq_in = seq_in.replace(x, y)  # 可折叠的直接折叠
                            elif x in wrong_call and (
                                    i == 0 or (gender_check(seq_in[i - 1]) != gender_check(seq_in[i + 1]))):
                                seq_in = seq_in.replace(x, y)  # 判定不同性别的折叠
                            elif x in wrong_call and (gender_check(seq_in[i - 1]) == gender_check(seq_in[i + 1])):
                                seq_in = seq_in.replace(x, '')  # 判定不同性别的直接去掉无用代号
                    if k == 0:
                        break  # 一次循环检查48个全都没有匹配才能跳出
                return seq_in


            def seq_check(seq_in):
                """
                代号序列压缩完毕，再检查是否有错误代号或超长
                :param seq_in:
                :return: 返回逻辑值
                """
                error_call = ['NQ', 'ZF', 'FF', 'QQ', 'GF', 'DF', 'JQ', 'SQ', 'BF', 'MQ']
                result = True
                for i in error_call:
                    if i in seq_in:
                        print("输入有误，还不明确该如何处理同性婚姻……")
                        result = False

                if len(seq_in) > 6:
                    print("这个人好像跟你没什么关系啊")  # 压缩后还超过6个节点说明实在太远
                    result = False
                return result


            def main_cal(s):
                """
                主题计算算法，通过三层嵌套字典实现代号序列的有效遍历
                :param s: 压缩无误可计算的代号序列
                :return: 返回计算结果中文序列号
                """
                # 粗暴建立三级节点
                sunzi = {"N": "曾孙女", "Z": "曾孙", "Q": "孙媳妇", "I": "孙子"}
                sunnv = {"N": "曾外孙女", "Z": "曾外孙", "F": "孙女婿", "I": "孙女"}
                waisun = {"N": "外曾孙女", "Z": "外曾孙", "Q": "外孙媳", "I": "外孙"}
                waisunnv = {"N": "外增外孙女", "Z": "外曾外孙", "F": "外孙女婿", "I": "外孙女"}
                zhizi = {"N": "侄孙女", "Z": "侄孙", "Q": "侄媳妇", "I": "侄子"}
                zhinv = {"N": "外侄孙女", "Z": "外侄孙", "F": "侄女婿", "I": "侄女"}
                waisheng = {"N": "外甥孙女", "Z": "外甥孙", "Q": "外甥媳妇", "I": "外甥"}
                waishengnv = {"N": "外甥孙女", "Z": "外甥孙", "F": "外甥女婿", "I": "外甥女"}
                erxi = {"G": "姻侄", "D": "姻侄", "J": "姻侄女", "S": "姻侄女", "B": "亲家公", "M": "亲家母",
                        "I": "儿媳"}
                nvxu = {"G": "姻侄", "D": "姻侄", "J": "姻侄女", "S": "姻侄女", "B": "亲家公", "M": "亲家母",
                        "I": "女婿"}
                dimei = {"G": "姻兄弟", "D": "姻兄弟", "J": "姻姐妹", "S": "姻姐妹", "B": "姻伯父（叫叔叔就行）",
                         "M": "姻伯母（叫阿姨就行）",
                         "I": "弟妹"}
                saozi = {"G": "姻兄弟", "D": "姻兄弟", "J": "姻姐妹", "S": "姻姐妹", "B": "姻伯父（叫叔叔就行）",
                         "M": "姻伯母（叫阿姨就行）",
                         "I": "嫂子"}
                jiefu = {"G": "姻兄弟", "D": "姻兄弟", "J": "姻姐妹", "S": "姻姐妹", "B": "姻伯父（叫叔叔就行）",
                         "M": "姻伯母（叫阿姨就行）",
                         "I": "姐夫"}
                meifu = {"G": "姻兄弟", "D": "姻兄弟", "J": "姻姐妹", "S": "姻姐妹", "B": "姻伯父（叫叔叔就行）",
                         "M": "姻伯母（叫阿姨就行）",
                         "I": "妹夫"}
                xiaojiuzi = {"N": "内侄女", "Z": "内侄", "Q": "舅弟媳", "I": "小舅子"}
                dajiuzi = {"N": "内侄女", "Z": "内侄", "Q": "舅嫂", "I": "大舅子"}
                dayizi = {"N": "姨甥女", "Z": "内甥", "F": "大姨夫，跟着叫姐夫吧", "I": "大姨子"}
                xiaoyizi = {"N": "姨甥女", "Z": "内甥", "F": "小姨夫，跟着叫妹夫吧", "I": "小姨子"}
                xiaoshuzi = {"N": "侄女", "Z": "叔侄", "Q": "小婶子", "I": "小叔子"}
                dabozi = {"N": "侄女", "Z": "叔侄", "Q": "大婶子", "I": "大伯子"}
                daguzi = {"N": "姑甥女", "Z": "姑甥", "F": "大姑父，跟着叫姐夫吧", "I": "大姑子"}
                xiaoguzi = {"N": "姑甥女", "Z": "姑甥", "F": "小姑父，跟着叫妹夫吧", "I": "小姑子"}
                shufu = {"N": "堂姐妹", "Z": "堂兄弟", "Q": "婶婶", "I": "叔父"}
                bofu = {"N": "堂姐妹", "Z": "堂兄弟", "Q": "婶婶", "I": "伯父"}
                gugu = {"N": "姑表姐妹", "Z": "姑表兄弟", "F": "姑父", "I": "姑姑"}
                jiujiu = {"N": "舅表姐妹", "Z": "舅表兄弟", "Q": "舅妈", "I": "舅舅"}
                yima = {"N": "姨表姐妹", "Z": "姨表兄弟", "F": "姨父", "I": "姨妈"}
                yuefu = {"G": "伯岳父（媳妇咋叫你咋叫）", "D": "叔岳父（媳妇咋叫你咋叫）", "J": "姑岳母（媳妇咋叫你咋叫）",
                         "S": "姑岳母（媳妇咋叫你咋叫）", "B": "太岳父（媳妇咋叫你咋叫）", "M": "太岳母（媳妇咋叫你咋叫）",
                         "I": "岳父"}
                yuemu = {"G": "舅岳父（媳妇咋叫你咋叫）", "D": "舅岳父（媳妇咋叫你咋叫）", "J": "姨岳母（媳妇咋叫你咋叫）",
                         "S": "姨岳母（媳妇咋叫你咋叫）", "B": "外太岳父（媳妇咋叫你咋叫）",
                         "M": "外太岳母（媳妇咋叫你咋叫）", "I": "岳母"}
                gongong = {"G": "伯翁（老公咋叫你咋叫）", "D": "叔公（老公咋叫你咋叫）", "J": "姑婆（老公咋叫你咋叫）",
                           "S": "姑婆（老公咋叫你咋叫）", "B": "祖翁（老公咋叫你咋叫）", "M": "祖婆（老公咋叫你咋叫）",
                           "I": "公公"}
                popo = {"G": "舅公（老公咋叫你咋叫）", "D": "舅公（老公咋叫你咋叫）", "J": "姨婆（老公咋叫你咋叫）",
                        "S": "姨婆（老公咋叫你咋叫）", "B": "外公", "M": "外婆", "I": "婆婆"}
                yeye = {"G": "伯祖父", "D": "叔祖父", "J": "姑奶奶", "S": "姑奶奶", "B": "曾祖父", "M": "曾祖母",
                        "I": "爷爷"}
                nainai = {"G": "舅公", "D": "舅公", "J": "姨奶奶", "S": "姨奶奶", "B": "曾外祖父", "M": "曾外祖母",
                          "I": "奶奶"}
                laoye = {"G": "伯外祖父", "D": "伯外祖父", "J": "姑姥姥", "S": "姑姥姥", "B": "外曾祖父",
                         "M": "外曾祖母", "I": "姥爷"}
                laolao = {"G": "外舅公", "D": "外舅公", "J": "姨姥姥", "S": "姨姥姥", "B": "外曾外祖父",
                          "M": "外曾外祖母", "I": "姥姥"}
                # 建立二级节点
                nver = {'N': waisunnv, 'Z': waisun, 'F': nvxu, 'I': "女儿"}
                erzi = {'N': sunnv, 'Z': sunzi, 'Q': erxi, 'I': "儿子"}
                zhangfu = {'G': dabozi, 'D': xiaoshuzi, 'J': daguzi, 'S': xiaoguzi, 'B': gongong, 'M': popo,
                           'I': "丈夫"}
                qizi = {'G': dajiuzi, 'D': xiaojiuzi, 'J': dayizi, 'S': xiaoyizi, 'B': yuefu, 'M': yuemu, 'I': "妻子"}
                gege = {'N': zhinv, 'Z': zhizi, 'Q': saozi, 'I': "哥哥"}
                didi = {'N': zhinv, 'Z': zhizi, 'Q': dimei, 'I': "弟弟"}
                jiejie = {'N': waishengnv, 'Z': waisheng, 'F': jiefu, 'I': "姐姐"}
                meimei = {'N': waishengnv, 'Z': waisheng, 'F': meifu, 'I': "妹妹"}
                baba = {'G': bofu, 'D': shufu, 'J': gugu, 'S': gugu, 'B': yeye, 'M': nainai, 'I': "爸爸"}
                mama = {'G': jiujiu, 'D': jiujiu, 'J': yima, 'S': yima, 'B': laoye, 'M': laolao, 'I': "妈妈"}
                # 建立一级节点
                The_dict = dict(zip(code_list, [nver, erzi, zhangfu, qizi, gege, didi, jiejie, meimei, baba, mama]))
                L = len(s)
                a = '这位是你的'

                # 根据序列长度遍历称呼，待优化，应使用递归算法
                # ？？？？？？？？？？？？？？？？？？？？？？
                # try:
                #     if L == 1:
                #         a += The_dict[s[0]]['I']
                #     elif L == 2:
                #         a += The_dict[s[0]][s[1]]['I']
                #     elif L == 3:
                #         a += The_dict[s[0]][s[1]][s[2]]
                #     elif L == 4:
                #         a += The_dict[s[0]][s[1]][s[2]] + '的' + The_dict[s[3]]['I'] + "，隔得好像有点远"
                #     elif L == 5:
                #         a += The_dict[s[0]][s[1]][s[2]] + '的' + The_dict[s[3]][s[4]]['I'] + "，隔得好像有点远"
                #     elif L == 6:
                #         a += The_dict[s[0]][s[1]][s[2]] + '的' + The_dict[s[3]][s[4]][s[5]] + "，隔得好像有点远"
                # except KeyError:
                #     a = "出现了好像还没有搞定的小问题，换一个试试"

                def test1(seq_in):
                    l = len(seq_in)
                    b = ''
                    if l == 1:
                        b = The_dict[seq_in[0]]['I']
                    elif l == 2:
                        b = The_dict[seq_in[0]][seq_in[1]]['I']
                    elif l == 3:
                        b = The_dict[seq_in[0]][seq_in[1]][seq_in[2]]
                    return b

                if L < 4:
                    a += test1(s)
                else:
                    a += test1(s[:3]) + '的' + test1(s[3:]) + "，隔得好像有点远"

                return a


            def menu():
                """
                初始界面打印程序
                :return: 无
                """
                print("#" * 70, end='\n\n')
                print("     欢迎使用极其简易版亲戚计算器 Kinship_Calculation 0.1      \n")
                print("#" * 70, end='\n\n')
                print("目前功能还很低级，只能计算以下十种关系的组合：\n"
                      "女儿  儿子  丈夫  妻子  哥哥  弟弟  姐姐  妹妹  爸爸  妈妈\n"
                      "请用“的”连接你想计算的亲戚关系，如爸爸的妈妈的姐姐，按Enter查看结果，按Q退出：\n")


            def example():
                """
                举例程序，show一下典型的输入输出，省去打字
                :return: 无
                """
                exa = ["爸爸的妈妈的姐姐的老公的弟弟的老婆",
                       "老婆的哥哥的妹妹的姐姐的爸爸的老婆的爸爸的姐姐的老公",
                       "哥哥的儿子的姐姐的老公的爸爸的妹妹的老公",
                       "哥哥的弟弟的姐姐的妹妹的爸爸的妈妈的姐姐的妈妈的女儿的老公的姐姐"]
                for i in exa:
                    j = input_handle(i)
                    j = seq_simplify(j)
                    if seq_check(j):
                        print(i)
                        print(main_cal(j))
                print("………………\n举例完毕，请输入你想计算的关系：")


            if __name__ == '__main__':
                menu()
                # 主函数循环体，无主动清屏功能，待改善。 i = os.system('cls')
                while True:
                    the_str = input()
                    if the_str.upper() == "Q":  # 见Q就退出
                        print("退出计算器")
                        break
                    elif the_str == 'show':  # 加一个自动举例的环节便于展示
                        example()
                    elif input_check(the_str):  # 主体计算判别部分
                        seq = input_handle(the_str)
                        seq = seq_simplify(seq)
                        if seq_check(seq):
                            print(main_cal(seq))
                    else:
                        print("输入有问题呐，人家又没有搞自然语言处理，很笨的只会按照示例计算，请重新输入：")

                os.system('pause')  # 系统暂停，防闪退

        elif Menu == 12:
            # coding=gbk
            from tkinter import Tk, Menu, messagebox, Text, END
            from re import match, findall
            from numpy.linalg import inv, solve
            from numpy import zeros, array, dot
            from os.path import exists


            def Show_Info():
                if exists("注意事项.txt"):
                    pass
                else:  # 下面就是在文本中输入的内容
                    f = open("注意事项.txt", 'x+')
                    f.write("本exe文件有以下基本功能:\n")
                    f.write("1.求可逆矩阵,注意事项:\n")
                    f.write("1.求可逆矩阵,注意事项:\n")
                    f.write("求可逆矩阵只需要输入一个矩阵就好，输入示例\n")
                    f.write("[1 2 3\n")
                    f.write("1 2 3\n")
                    f.write("1 2 3]\n")
                    f.write("注意中括号必须使用英文字符[ ],不能使用中文字符【 】相邻的两个数用一个空格隔开\n")
                    f.write("2.求矩阵的点积，需要输入两个矩阵，矩阵的输入方法和上述一样中间用大写的的“X”隔开，输入示例：\n")
                    f.write("[1 2 3\n")
                    f.write("1 2 3\n")
                    f.write("1 2 3]\n")
                    f.write("X\n")
                    f.write("[1 2 3\n")
                    f.write("1 2 3\n")
                    f.write("1 2 3]\n")
                    f.write(
                        "3.求多元一次式的解，在这个过程中只需要未知数的系数即可(要带符号)等号和加减号不需要写，输出示例：\n")
                    f.write("如果想求X+Y=0,3X+2Y=9就这样输入\n")
                    f.write("1 1 0\n")
                    f.write("3 2 9\n")
                    f.write("相邻数字用一个空格隔开\n")
                    f.write("输出是这样的[9 -9]即X=9,Y=-9未知数与上面的未知数对齐\n")
                    f.write("4.求转置矩阵和求可逆矩阵输入相同\n")
                    f.write("5.求矩阵的和和求矩阵的点积相同知识将'X'变成'+'即可\n")
                    f.write(
                        "另外注意如果输出这样的[1. 2.]表示输出结果是[1.0 2.0]e是自然常数e后面的数是它的指数如果是负数则是负指数")
                    messagebox.showinfo(title="提示", message="已在同目录下写下文档“注意事项.txt”请先在文档中查看")


            def Martix_dot():
                global t1  # 声明变量
                global t2
                t2.delete(0.0, END)  # 删除文本框上一次的旧的不需要的内容
                L = t1.get(0.0, END)  # 得到文本框中的内容
                P2 = []  # 下面就是得到可以运算矩阵的过程
                P1 = []
                Content1 = []
                Content2 = []
                Q = L.split('X')
                P1, P2 = Q[0], Q[1]
                P1 = P1.split('\n')
                P2 = P2.split('\n')
                for x in range(len(P1)):
                    K1 = findall('[0-9]{1,}', P1[x])
                    if len(K1) > 0:
                        Content1.append(K1)
                A1 = zeros((len(Content1), len(Content1[0])), int)
                for x in range(len(Content1)):
                    for y in range(len(Content1[0])):
                        A1[x][y] = Content1[x][y]
                for x in range(len(P2)):
                    K2 = findall('[0-9]{1,}', P2[x])  # 找到所有的数字形成一个列表
                    if len(K2) > 0:
                        Content2.append(K2)
                A2 = zeros((len(Content2), len(Content2[0])), int)
                for x in range(len(Content2)):
                    for y in range(len(Content2[0])):
                        A2[x][y] = Content2[x][y]
                try:
                    t2.insert(0.0, dot(A1, A2))  # 在文本框中输入结果
                except:
                    t2.insert(0.0, "输入有误")


            def Invertible_matrix():
                global t1
                global t2
                t2.delete(0.0, END)
                L = t1.get(0.0, END)
                P = L.split('\n')
                Conten = []
                for x in range(len(P)):
                    K = findall('[0-9]{1,}', P[x])
                    if len(K) > 0:
                        Conten.append(K)
                A = zeros((len(Conten), len(Conten[0])), int)
                for x in range(len(Conten)):
                    for y in range(len(Conten[0])):
                        A[x][y] = Conten[x][y]
                try:
                    t2.insert(0.0, inv(A))
                except:
                    t2.insert(0.0, "输入有误")


            def Polynomial():
                global t1
                global t2
                t2.delete(0.0, END)
                L = t1.get(0.0, END)
                P = L.split('\n')
                Conten = []
                for x in P:
                    if len(x) > 0:
                        Conten.append(x.split())
                print(Conten)
                A = zeros((len(Conten), len(Conten[0]) - 1))
                for x in range(len(Conten)):
                    for y in range(len(Conten[0]) - 1):
                        A[x][y] = int(Conten[x][y])
                B = []
                for x in range(len(Conten)):
                    B.append(int(Conten[x][len(Conten[0]) - 1]))
                t2.insert(0.0, solve(A, B))


            def T():
                global t1  # 声明全局变量
                global t2  # 声明全局变量
                t2.delete(0.0, END)  # 删除文本框中的字符串
                L = t1.get(0.0, END)  # 得到文本框中的字符串
                P = L.split('\n')
                Conten = []
                for x in range(len(P)):
                    K = findall('[0-9]{1,}', P[x])  # 找到所有的数字
                    if len(K) > 0:
                        Conten.append(K)
                A = zeros((len(Conten), len(Conten[0])), int)
                for x in range(len(Conten)):
                    for y in range(len(Conten[0])):
                        A[x][y] = Conten[x][y]
                try:
                    t2.insert(0.0, A.T)
                except:
                    t2.insert(0.0, "输入有误")


            def plus():
                global t1
                global t2
                t2.delete(0.0, END)
                L = t1.get(0.0, END)
                P1 = []
                P2 = []
                Content1 = []
                Content2 = []
                Q = L.split('+')
                P1, P2 = Q[0], Q[1]
                P1 = P1.split('\n')
                P2 = P2.split('\n')
                for x in range(len(P1)):
                    K1 = findall('[0-9]{1,}', P1[x])
                    if len(K1) > 0:
                        Content1.append(K1)
                A1 = zeros((len(Content1), len(Content1[0])), int)
                for x in range(len(Content1)):
                    for y in range(len(Content1[0])):
                        A1[x][y] = Content1[x][y]
                for x in range(len(P2)):
                    K2 = findall('[0-9]{1,}', P2[x])
                    if len(K2) > 0:
                        Content2.append(K2)
                A2 = zeros((len(Content2), len(Content2[0])), int)
                for x in range(len(Content2)):
                    for y in range(len(Content2[0])):
                        A2[x][y] = Content2[x][y]
                try:
                    t2.insert(0.0, A1 + A2)
                except:
                    t2.insert(0.0, "输入有误")


            Mywindow = Tk()  # 创建GUI窗口

            Mywindow.title("简单矩阵处理器")  # GUI窗口的名字

            Mywindow.geometry("800x450+500+250")  # GUI窗口的大小

            Mywindow.minsize(400, 400)  # GUI窗口的最小值

            t1 = Text(Mywindow, width=180, height=11, font=('Calibri 12  italic'))  # 创建一个文本框

            t1.grid(row=0, column=0)  # grid和pack()只能使用一个，都是文本框的"放置函数"

            t1.insert(0.0,
                      "请先点击“帮助”查看矩阵简单处理器的使用方法，并且在输入完之后再点击输出结果，并从中选取计算方式")  # 在第一个文本框中插入字符串

            t2 = Text(Mywindow, width=180, height=20, font=('Calibri 12  italic'))  # 创建第二个文本框

            t2.grid(row=20, column=0)

            t2.insert(0.0, "在此处输出结果")

            Menu_All = Menu(Mywindow)  # 创建总菜单

            MENU1 = Menu(Menu_All, tearoff=0)  # 创建主菜单

            MENU1.add_command(label="求可逆矩阵", command=lambda: Invertible_matrix())  # 创建副菜单

            MENU1.add_command(label="求矩阵的点积", command=lambda: Martix_dot())  # 创建副菜单

            MENU1.add_command(label="求多元一项式的解", command=lambda: Polynomial())  # 创建副菜单

            MENU1.add_command(label="求转置矩阵", command=lambda: T())  # 创建副菜单

            MENU1.add_command(label="求两个矩阵的加法", command=lambda: plus())  # 创建副菜单

            Menu_All.add_cascade(label="输出结果", menu=MENU1, font=('Calibri 12 '))  # 创建副菜单

            MENU2 = Menu(Menu_All, tearoff=0)  # 创建主菜单

            MENU2.add_command(label="输入注意事项", command=lambda: Show_Info())  # 创建副菜单

            Menu_All.add_cascade(label='帮助', menu=MENU2, font=('Calibri 12 '))  # 总菜单显示

            Mywindow.config(menu=Menu_All)  # 显示主菜单

            Mywindow.mainloop()  # 循环



    except ValueError:  # 如果捕获到输入错误就提示
        print("Error:你输入的不是数字请重新输入")
        f = open('Error.txt', 'a+')
        time = datetime.datetime.now()  # 获取当前时间
        time = str(time)  # 转换为字符串
        f.write(time)  # 写入时间
        f.write("错误代码：000\n")
        f.close()

    except NameError:  # 捕获名称错误
        print("程序出现异常请反馈给程序员"
              "错误代码：001")
        f = open('Error.txt', 'a+')
        time = datetime.datetime.now()
        time = str(time)
        f.write(time)
        f.write("错误代码：001\n")
        f.close()

    except SyntaxError:  # 捕获语法错误
        print("程序出现异常请反馈给程序员"
              "错误代码：002")
        f = open('Error.txt', 'a+')
        time = datetime.datetime.now()
        time = str(time)
        f.write(time)
        f.write("错误代码：002\n")
        f.close()
