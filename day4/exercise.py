# Day4 练习题：函数基础 + 参数体系 + 作用域 + 高阶函数

# ===================== 练习题1：函数定义与参数 =====================
# 题目：定义一个函数，计算矩形的面积和周长
# 要求：
# 1. 函数接收两个参数：长和宽
# 2. 返回两个值：面积和周长
# 3. 添加文档字符串说明函数功能、参数和返回值
# 请在此处编写代码：

def rectangle(length, width):
    """计算矩形的面积和周长
    参数：
        length: 矩形的长
        width: 矩形的宽
    返回值：
        tuple: (面积, 周长)
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


area, perimeter = rectangle(5, 3)
print(f"面积：{area}")
print(f"周长：{perimeter}")
print()


# ===================== 练习题2：默认参数与不定长参数 =====================
# 题目：定义一个函数，计算任意多个数的平均值
# 要求：
# 1. 支持接收任意多个数值参数
# 2. 添加一个默认参数round_digits=2，用于指定结果保留的小数位数
# 3. 如果没有传入任何参数，返回0
# 请在此处编写代码：

def average(*args, round_digits=2):
    """计算任意多个数的平均值
    参数：
        *args: 任意多个数值参数
        round_digits: 结果保留的小数位数，默认2位
    返回值：
        float: 平均值，没有参数返回0
    """
    if not args:
        return 0
    total = sum(args)
    avg = total / len(args)
    return round(avg, round_digits)


print(average(1, 2, 3, 4, 5))
print(average(1.5, 2.5, 3.5, round_digits=1))
print(average())
print()


# ===================== 练习题3：关键字参数与**kwargs =====================
# 题目：定义一个函数，打印学生信息
# 要求：
# 1. 必须接收name和age两个位置参数
# 2. 支持接收任意多个其他关键字参数（如gender、major、score等）
# 3. 先打印姓名和年龄，再打印其他所有信息
# 请在此处编写代码：

def print_student(name, age, **kwargs):
    """打印学生信息
    参数：
        name: 学生姓名
        age: 学生年龄
        **kwargs: 其他学生信息
    """
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print_student("小明", 20, gender="男", major="计算机", score=92)
print()

# ===================== 练习题4：函数作用域 =====================
# 题目：分析以下代码的输出结果，并解释原因
# 要求：
# 1. 先预测输出结果，再运行代码验证
# 2. 用注释解释每一步的输出原因
x = 10


def func1():
    x = 20
    print("func1中的x：", x)


def func2():
    global x
    x = 30
    print("func2中的x：", x)


def func3():
    print("func3中的x：", x)


func1()
func3()
func2()
func3()
print()

# ===================== 练习题5：lambda与map =====================
# 题目：给定列表nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 要求：
# 1. 使用map和lambda将列表中每个元素乘以3
# 2. 使用map和lambda将列表中每个元素转换为字符串
# 3. 将结果转换为列表并打印
# 请在此处编写代码：

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tripled = list(map(lambda x: x * 3, nums))
print("乘以3：", tripled)
str_nums = list(map(lambda x: str(x), nums))
print("转换为字符串：", str_nums)
print()

# ===================== 练习题6：filter筛选 =====================
# 题目：给定列表words = ["apple", "banana", "orange", "grape", "pear", "kiwi"]
# 要求：
# 1. 使用filter和lambda筛选出以字母"a"开头的单词
# 2. 使用filter和lambda筛选出长度大于5的单词
# 3. 将结果转换为列表并打印
# 请在此处编写代码：

words = ["apple", "banana", "orange", "grape", "pear", "kiwi"]
a_words = list(filter(lambda x: x[0] == "a", words))
print(a_words)
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)
print()

# ===================== 练习题7：reduce累积 =====================
# 题目：给定列表nums = [2, 4, 6, 8, 10]
# 要求：
# 1. 使用reduce和lambda计算列表所有元素的和
# 2. 使用reduce和lambda计算列表所有元素的最大值
# 3. 打印计算结果
# 请在此处编写代码：

from functools import reduce

nums = [2, 4, 6, 8, 10]
sum_nums = reduce(lambda x, y: x + y, nums)
print(sum_nums)
max_num = reduce(lambda x, y: x if x > y else y, nums)
print(max_num)
print()

# ===================== 练习题8：高阶函数组合使用 =====================
# 题目：给定列表nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 要求：
# 1. 先使用filter筛选出所有奇数
# 2. 再使用map将每个奇数平方
# 3. 最后使用reduce计算所有平方值的和
# 4. 一行代码完成所有操作
# 请在此处编写代码：

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, nums)))
print("奇数平方和：", result)
print()

# ===================== 练习题9：闭包实战 =====================
# 题目：实现一个计数器闭包
# 要求：
# 1. 定义一个外层函数counter()，返回一个内层函数
# 2. 每次调用内层函数，计数器加1，并返回当前计数值
# 3. 多个计数器实例之间互不影响

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


c1 = counter()
print(c1())
print(c1())
c2 = counter()
print(c2())
print()


# ===================== 练习题10：综合实战：数据处理函数封装 =====================
# 题目：封装一个数据处理函数，完成以下功能
# 1. 接收一个数字列表作为参数
# 2. 筛选出列表中大于0的数字
# 3. 对筛选后的数字取平方根
# 4. 计算所有平方根的平均值，保留3位小数
# 5. 返回平均值
# 要求：使用map、filter、reduce组合实现
# 请在此处编写代码：

def process_data(nums):
    """数据处理函数：筛选正数→取平方根→计算平均值
    参数：
        nums: 数字列表
    返回值：
        float: 平方根的平均值，保留3位小数
    """

    # 筛选正数
    positive_nums =  filter(lambda x: x > 0, nums)

    # 取平方根
    sqrt_nums = map(lambda x: x ** 2, positive_nums)

    # 转换为列表以便计算长度和总和
    sqrt_list = list(sqrt_nums)
    if not sqrt_list:
        return 0.0
    # 计算总和
    total = reduce(lambda x, y: x + y, sqrt_list)
    # 计算平均值
    avg = total / len(sqrt_list)
    return round(avg, 3)

nums = [1, -2, 4, -8, 9, 16, -25]
print("数据处理结果：", process_data(nums))