# Day4 示例代码：函数基础 + 参数体系 + 作用域 + 高阶函数

from functools import reduce

# ===================== 1. 函数基础示例 =====================
print("=" * 20 + " 函数基础示例 " + "=" * 20)


# 1.1 函数定义与调用
def add(a, b):
    """
    计算两个数的和
    :param a: 第一个数
    :param b: 第二个数
    :return: 两个数的和
    """
    result = a + b
    return result


sum_result = add(3, 5)
print(f"add(3, 5)结果：{sum_result}")
print(f"函数文档：{add.__doc__}")
print()


# 1.2 函数返回值
def print_hello():
    print("Hello, world!")


result = print_hello()
print(f"无返回值函数结果：{result}")


def calculate(a, b):
    sum_ab = a + b
    diff_ab = a - b
    product_ab = a * b
    return sum_ab, diff_ab, product_ab


sum_ab, diff_ab, product_ab = calculate(10, 5)
print(f"多返回值解包：{sum_ab}, {diff_ab}, {product_ab}")

# ===================== 2. 函数参数体系示例 =====================
print("=" * 20 + " 函数参数体系示例 " + "=" * 20)


# 2.1 位置参数
def greet(name, age):
    print(f"位置参数示例：你好，我是{name}，今年{age}岁")


greet("张三", 20)
print()


# 2.2 默认参数
def greeting(name, age=18):
    print(f"默认参数示例：你好，我是{name}，今年{age}岁")


greeting("李四")
greeting("王五", 22)
print()


# 2.3 关键字参数
def greet(name, age, city):
    print(f"关键字参数示例：你好，我是{name}，今年{age}岁，来自{city}")


greet("赵六", city="北京", age=21)
print()


# 2.4 不定长位置参数*args
def sum_all(*args):
    """计算任意多个数的和"""
    total = 0
    for num in args:
        total += num
    return total


print("*args示例：sum_all(1,2,3,4,5) =", sum_all(1, 2, 3, 4, 5))
print()


# 2.5 不定长关键字参数**kwargs
def print_info(**kwargs):
    """打印任意多个关键字参数"""
    print("**kwargs示例：")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="小明", age=20, major="计算机")
print()

# ===================== 3. 函数作用域示例 =====================
print("=" * 20 + " 函数作用域示例 " + "=" * 20)

# 3.1 局部变量与全局变量
global_var = "我是全局变量"


def test_scope():
    local_var = "我是局部变量"
    print("函数内部访问局部变量：", local_var)
    print("函数内部访问全局变量：", global_var)


test_scope()
# print(local_var)  # 错误，不能访问局部变量
print()

# 3.2 global关键字
count = 0


def increment():
    global count
    count += 1


increment()
print("global关键字示例：count =", count)
print()


# 3.3 nonlocal关键字
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
        print("inner函数中的x：", x)

    inner()
    print("outer函数中的x：", x)


print("nonlocal关键字示例：")
outer()
print()

# ===================== 4. 匿名函数lambda示例 =====================
print("=" * 20 + " 匿名函数lambda示例 " + "=" * 20)

# 基础lambda
add_lambda = lambda a, b: a + b
print("lambda加法：add_lambda(3,5) =", add_lambda(3, 5))

# lambda作为参数
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print("lambda作为map参数：", squared)
print()

# ===================== 5. 三大高阶函数示例 =====================
print("=" * 20 + " 三大高阶函数示例 " + "=" * 20)

# 5.1 map函数
print("map函数示例：")
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print("平方：", squared)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, list1, list2))
print("两个列表相加：", sum_list)
print()

# 5.2 filter函数
print("filter函数示例：")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("筛选偶数：", even_nums)

words = ["python", "ai", "java", "data", "ml"]
long_words = list(filter(lambda x: len(x) > 3, words))
print("筛选长度大于3的单词：", long_words)
print()

# 5.3 reduce函数
print("reduce函数示例：")
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print("乘积：", product)

product_with_init = reduce(lambda x, y: x * y, nums, 10)
print("带初始值的乘积：", product_with_init)
print()

# ===================== 6. 闭包基础示例 =====================
print("=" * 20 + " 闭包基础示例 " + "=" * 20)


def outer(x):
    def inner(y):
        return x + y

    return inner


add5 = outer(5)
add10 = outer(10)

print("add5(3) =", add5(3))
print("add10(3) =", add10(3))
print()

print("=" * 20 + " Day4示例代码运行结束 " + "=" * 20)
