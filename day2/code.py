# Day2 示例代码：分支结构 + 循环结构 + 列表推导式

# ===================== 1. 分支结构示例 =====================
print("=" * 20 + " 分支结构示例 " + "=" * 20)

# 1.1 单分支结构
age = 20
if age >= 18:
    print("已成年，具备完全民事行为能力")
print()

# 1.2 双分支结构
score = 75
if score >= 60:
    print("考试及格")
else:
    print("考试不及格")
print()

# 1.3 多分支结构
score = 88
print("多分支示例：成绩等级判定")
if score >= 90:
    print("等级：A")
elif score >= 80:
    print("等级：B")
elif score >= 60:
    print("等级：C")
else:
    print("等级：D")
print()

# 1.4 嵌套分支结构
age = 22
has_id = True
print("嵌套分支示例：入场核验")
if age >= 18:
    print("年龄符合要求")
    if has_id:
        print("身份核验通过，允许进入")
    else:
        print("未携带有效证件，禁止进入")
else:
    print("年龄不符合要求，禁止进入")
print()

# 1.5 三元表达式
score = 75
result = "及格" if score >= 60 else "不及格"
print(result)
print()

# ===================== 2. while循环示例 =====================
print("=" * 20 + " while循环示例 " + "=" * 20)

# 2.1 1-100累加求和
sum_num = 0
i = 1
while i <= 100:
    sum_num += i
    i += 1

print(f"1-100累加和：{sum_num}")
print()

# 2.2 斐波那契数列生成（前10个）
print("前10个斐波那契数：", end="")
a, b = 1, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

print("\n")

# ===================== 3. for循环与range()示例 =====================
print("=" * 20 + " for循环与range()示例 " + "=" * 20)

# 3.1 range()三种用法
print("range(5)生成的序列：", end="")
for i in range(5):
    print(i, end=" ")
print()

print("range(2,6)生成的序列：", end="")
for i in range(2, 6):
    print(i, end=" ")
print()

print("range(1,10,2)生成的序列：", end="")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")

# 3.2 遍历字符串
s = "PythonAI"
print("遍历字符串PythonAI：")
for char in s:
    print(char, end=" ")
print("\n")

# 3.3 遍历列表计算平均分
score_list = [90, 85, 78, 92, 88]
sum_score = 0
for score in score_list:
    sum_score += score

avg_score = sum_score / len(score_list)
print(f"学生成绩列表：{score_list}")
print(f"平均分：{avg_score:.2f}")

# ===================== 4. 循环控制关键字示例 =====================
print("=" * 20 + " 循环控制关键字示例 " + "=" * 20)

# 4.1 break关键字
print("break示例：查找第一个大于90的数")
num_list = [85, 78, 92, 88, 95]
for num in num_list:
    if num > 90:
        print(f"找到目标数：{num}，终止循环")
        break
    print(f"当前遍历：{num}")
print()

# 4.2 continue关键字
print("continue示例：1-10只打印奇数")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

# 4.3 循环else子句
print("循环else示例1：无break，正常结束")
num_list = [1, 3, 5, 7, 9]
for num in num_list:
    if num < 0:
        print("找到负数")
        break
else:
    print("列表全为正数，循环正常结束，执行else")

print("循环else示例2：有break，终止循环")
num_list = [1, -3, 5, 7, 9]
for num in num_list:
    if num < 0:
        print("找到负数，终止循环")
        break
else:
    print("列表全为正数")
print()

# ===================== 5. 循环嵌套示例 =====================
print("=" * 20 + " 循环嵌套示例 " + "=" * 20)

# 5.1 九九乘法表
print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()
print()

# 5.2 5行正三角星号
print("5行正三角星号：")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()

# ===================== 6. 列表推导式示例 =====================
print("=" * 20 + " 列表推导式示例 " + "=" * 20)

# 6.1 基础列表推导式：1-10的平方
square_list = [i ** 2 for i in range(1, 11)]
print(f"1-10的平方列表：{square_list}")

# 6.2 带条件筛选：1-20 偶数的平方
even_square = [i ** 2 for i in range(1, 21) if i % 2 == 0]
print(f"1-20偶数的平方列表：{even_square}")

# 6.3 双条件列表推导式：偶数保留，奇数替换为-1
num_list = [i if i % 2 == 0 else -1 for i in range(1, 11)]
print(f"双条件处理列表：{num_list}")

# 6.4 嵌套循环列表推导式：两两组合
a = [1, 2, 3]
b = ["x", "y"]
combine = [f"{i}{j}" for i in a for j in b]
print(f"列表元素两两组合：{combine}")
print()

print("=" * 20 + " Day2示例代码运行结束 " + "=" * 20)
