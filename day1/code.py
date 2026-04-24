# Day1 示例代码：Python核心数据类型与字符串操作

# ===================== 1. 第一个Python程序 =====================
print("=" * 20 + " 第一个Python程序 " + "=" * 20)
print("Hello AI World!")
print()  # 空行，用于控制台输出分隔

# ===================== 2. 变量定义与基础操作 =====================
print("=" * 20 + " 变量定义与类型查看 " + "=" * 20)
# 变量定义
name = "AI应用开发工程师"
study_days = 90
daily_hours = 4.0
is_learn = True

# 打印变量值与类型
print(f"岗位：{name}，类型：{type(name)}")
print(f"学习周期：{study_days} 天，类型：{type(study_days)}")
print(f"每日学习时长：{daily_hours} 小时，类型：{type(daily_hours)}")
print(f"是否正在学习：{is_learn}，类型：{type(is_learn)}")
print()

# 变量重新赋值
study_days = 89
print(f"修改后的剩余学习天数：{study_days} 天")

# 多变量同时赋值
a, b, c = 10, 20, 30
print(f"多变量赋值：a = {a}, b = {b}, c = {c}")
print()

# ===================== 3. 核心数据类型示例 =====================
print("=" * 20 + " 核心数据类型示例 " + "=" * 20)

# 3.1 数值类型与基础运算
int_num = 100
float_num = 3.14
print(f"整数：{int_num}，类型：{type(int_num)}")
print(f"浮点数：{float_num}，类型：{type(float_num)}")
# 基础数值运算
print(f"加法：10 + 5 = {10 + 5}")
print(f"减法：10 - 5 = {10 - 5}")
print(f"乘法：10 * 5 = {10 * 5}")
print(f"除法：10 / 5 = {10 / 5}")  # 除法结果永远是浮点数
print(f"整除：10 // 3 = {10 // 3}")
print(f"取余：10 % 3 = {10 % 3}")
print(f"幂运算：2 ** 3 = {2 ** 3}")
print()

# 3.2 字符串类型
single_quote_str = '单引号字符串'
double_quote_str = "双引号字符串"
multi_line_str = '''三引号
多行字符串
支持换行'''
print(f"单引号字符串：{single_quote_str}")
print(f"双引号字符串：{double_quote_str}")
print(f"多行字符串：\n{multi_line_str}")
print()

# 3.3 布尔类型
bool_true = True
bool_false = False
print(f"布尔值True：{bool_true}，类型：{type(bool_true)}")
print(f"布尔值False：{bool_false}，类型：{type(bool_false)}")
print()

# 3.4 列表类型
list_example = ["张三", 21, 95.5, True]
print(f"列表：{list_example}，类型：{type(list_example)}")
print(f"列表第一个元素：{list_example[0]}")
print()

# 3.5 元组类型
tuple_example = ("男", "女", "未知")
print(f"元组：{tuple_example}，类型：{type(tuple_example)}")
print(f"元组第二个元素：{tuple_example[1]}")
print()

# 3.6 字典类型
dict_example = {
    "name": "李四",
    "age": 22,
    "score": 98.0,
    "is_student": True
}

print(f"字典：{dict_example}，类型：{type(dict_example)}")
print(f"字典中name对应的值：{dict_example['name']}")
print()

# 3.7 集合类型
set_example = {1, 2, 3, 3, 2, 1, 4, 5}
print(f"集合（自动去重）：{set_example}，类型：{type(set_example)}")
empty_set = set()  # 空集合定义
print(f"空集合：{empty_set}，类型：{type(empty_set)}")
print()

# ===================== 4. 字符串索引与切片 =====================
print("=" * 20 + " 字符串索引与切片 " + "=" * 20)
s = "PythonAI"
print(f"原字符串：{s}")
print(f"字符串长度：{len(s)}")
print()

# 索引操作
print(f"正向索引0（第一个字符）：{s[0]}")
print(f"正向索引5：{s[5]}")
print(f"反向索引-1（最后一个字符）：{s[-1]}")
print(f"反向索引-3：{s[-3]}")
print()

# 切片操作
print(f"切片[0:6]：{s[0:6]}")
print(f"切片[:6]：{s[:6]}")  # 省略起始索引（默认从 0 开始）
print(f"切片[6:]：{s[6:]}")  # 省略结束索引（默认到末尾）
print(f"切片[::2]：{s[::2]}")
print(f"切片[::-1]：{s[::-1]}")
print()

# ===================== 5. 字符串常用方法 =====================
print("=" * 20 + " 字符串常用方法 " + "=" * 20)
demo_str = "  Hello Python AI  "
print(f"原字符串：{demo_str}")

# 大小写转换
print(f"转大写：{demo_str.upper()}")
print(f"转大写：{demo_str.lower()}")

# 去除首尾空白
print(f"去除首尾空白：{demo_str.strip()}")

# 内容替换
print(f"替换Python为Java：{demo_str.replace('Python', 'Java')}")

# 字符串拆分
split_str = "张三,李四,王五,赵六"
print(f"原字符串：{split_str}")
print(f"按逗号拆分：{split_str.split(',')}")

# 字符串连接
join_list = ["2024", "01", "01"]
print(f"原列表：{join_list}")
print(f"用 - 连接：{'-'.join(join_list)}")
print()

print("=" * 20 + " Day1示例代码运行结束 " + "=" * 20)
