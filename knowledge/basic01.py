#   python 的 # 用来进行单行注释  用 ''' （"""） 进行多行注释
'''
基本数据类型：
1. boolean  —— True  、 False  （首字母大写 ; 非0表示True，0表示False ; bool（）中有内容为True，无内容为False）
2. 复数 —— 用j进行表示。例如，36j
3. 字符串 —— 单引号 or 双引号 ,需要成对出现
4. 原始字符串  —— 在字符串前加r，表示该字符串为"原始字符串" ，所见即所得。不需要给字符串中的内容进行转义
5. 可以用type(xxx)函数进行变量的类型查看
6. ord(xx) 可以用来得到元素的ASIIC码值
'''
# 得到结论为1
int(True);
# 与 'let\'s go'  得到同样的结果
"let's go"

'''
转移字符 （基础的几个）： 将一个字符变成转移字符时就是给它前面加上\  ---与java用法保持一致
\n  换行    \r  回车   \'   单引号
'''
str = 'let\'s go';


"""
字符串的运算
1. 拼接  +      "hello" + "world"  --->   helloworld
2. 多次  *    "hello" * 3  ---> hellohellohello
3. 任意元素  [n]     "hello"[0]   ---> h     "hello"[-1]  ---> o   (输入正数代表角标为n的元素，输入负数代表从后往前数第n个元素)
4. 获取子串 [n:m]   'hello' [0:2]  --->he (代表第0个元素到第1个(m-1)元素)   'hello' [0:-1]  ---> hell  (代表从第0个元素到倒数第2个元素)
                                      'hello world'[6 : 11]   ==   'hello world'[6 : 20 ]   ==   'hello world'[6 : ]  ==  'hello world'[ -5 : ]   == 'world'
"""

