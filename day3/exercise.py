# Day3 练习题：四大核心容器深入 + 深拷贝浅拷贝 + 容器通用操作

# ===================== 练习题1：列表常用方法综合 =====================
# 题目：给定列表nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]，完成以下操作
# 1. 在列表末尾添加元素7
# 2. 在索引2的位置插入元素8
# 3. 删除第一个出现的元素1
# 4. 删除索引5的元素
# 5. 统计元素5出现的次数
# 6. 将列表升序排序
# 7. 反转列表
# 请在此处编写代码：

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"原列表：{nums}")
nums.append(7)
nums.insert(2, 8)
nums.remove(1)
nums.pop(5)
print(f"增 / 删后的列表：{nums}")
print(f"统计元素5出现的次数：{nums.count(5)}")
nums.sort()
print(f"列表升序排序：{nums}")
nums.reverse()
print(f"反转列表：{nums}")
print()

# ===================== 练习题2：字典增删改查综合 =====================
# 题目：给定学生信息字典student = {"name": "小明", "age": 19, "major": "计算机", "score": 88}
# 1. 获取学生的姓名和专业，用get方法
# 2. 修改学生的分数为92
# 3. 添加新的键值对："gender": "男"
# 4. 删除键"age"
# 5. 打印所有的键和所有的值
# 请在此处编写代码：

student = {"name": "小明", "age": 19, "major": "计算机", "score": 88}
print(f"原字典：{student}")
print(f"获取学生的姓名：{student.get('name')}")
print(f"获取学生的专业：{student.get('major')}")
student["score"] = 92
student["gender"] = "男"
student.pop("age")
print(f"增 / 改 / 删后的字典：{student}")
for key, value in student.items():
    print(f"{key}: {value}")
print()

# ===================== 练习题3：集合去重与运算 =====================
# 题目：给定两个列表list1 = [1, 2, 3, 4, 5, 3, 2, 1]，list2 = [4, 5, 6, 7, 8, 5, 4]
# 1. 将两个列表转换为集合，去除重复元素
# 2. 求两个集合的并集、交集、差集（list1有list2没有的元素）
# 3. 判断元素3是否在并集中
# 请在此处编写代码：

list1 = [1, 2, 3, 4, 5, 3, 2, 1]
list2 = [4, 5, 6, 7, 8, 5, 4]

set1 = set(list1)
set2 = set(list2)

print(f"list1去重：{set1}")
print(f"list2去重：{set2}")

print(f"并集：{set1.union(set2)}")
print(f"交集：{set1.intersection(set2)}")
print(f"差集：{set1.difference(set2)}")
print(f"元素3是否在并集中：{3 in set1.union(set2)}")
print()

# ===================== 练习题4：元组特性与转换 =====================
# 题目：完成以下操作
# 1. 定义一个包含3个元素的元组，存储你的姓名、年龄、性别
# 2. 将元组转换为列表，修改年龄为比原来大1岁
# 3. 将修改后的列表转换回元组
# 4. 打印最终的元组
# 请在此处编写代码：

t = ("张三", 20, "男")
print(f"原元组：{t}")
l = list(t)
l[1] = 21
new_t = tuple(l)
print(f"修改后的元组：{new_t}")
print()

# ===================== 练习题5：深拷贝与浅拷贝判断 =====================
# 题目：给定嵌套列表original = [[1,2], [3,4], [5,6]]
# 1. 分别用赋值、浅拷贝、深拷贝创建三个新对象a、b、c
# 2. 修改a[0][0] = 100，打印original
# 3. 修改b[1][1] = 200，打印original
# 4. 修改c[2][1] = 300，打印original
# 5. 观察并记录每次修改后original的变化，理解三种拷贝的区别
# 请在此处编写代码：

import copy

original = [[1, 2], [3, 4], [5, 6]]
print(f"原对象：{original}")

# 赋值
a = original
a[0][0] = 100
print(f"修改a后original：{original}")

# 浅拷贝
b = copy.copy(original)
b[1][1] = 200
print(f"修改b后original：{original}")

c = copy.deepcopy(original)
c[2][1] = 300
print(f"修改c后original：{original}")
print()

# ===================== 练习题6：容器遍历与统计 =====================
# 题目：给定列表words = ["apple", "banana", "orange", "apple", "grape", "banana", "apple"]
# 1. 遍历列表，统计每个单词出现的次数，用字典存储结果
# 2. 打印统计结果，格式：apple: 3次
# 请在此处编写代码：

words = ["apple", "banana", "orange", "apple", "grape", "banana", "apple"]
count_dict = {}
for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for key, value in count_dict.items():
    print(f"{key}: {value}次")
print()

# ===================== 练习题7：自定义排序 =====================
# 题目：给定学生成绩列表students = [
#     {"name": "张三", "score": 85, "age": 20},
#     {"name": "李四", "score": 92, "age": 19},
#     {"name": "王五", "score": 85, "age": 21},
#     {"name": "赵六", "score": 78, "age": 20}
# ]
# 1. 按分数降序排序
# 2. 如果分数相同，按年龄升序排序
# 3. 打印排序后的列表
# 请在此处编写代码：

students = [
    {"name": "张三", "score": 85, "age": 20},
    {"name": "李四", "score": 92, "age": 19},
    {"name": "王五", "score": 85, "age": 21},
    {"name": "赵六", "score": 78, "age": 20}
]

# 先按分数降序，再按年龄升序
sorted_students = sorted(students, key=lambda x: (-x["score"], x["age"]))  # 按分数 降序 排序（加负号实现从高到低）
print("排序后的学生：")
for student in sorted_students:
    print(student)
print()

# ===================== 练习题8：字典合并与去重 =====================
# 题目：给定两个字典dict1 = {"a": 1, "b": 2, "c": 3}，dict2 = {"b": 4, "c": 5, "d": 6}
# 1. 合并两个字典，相同键的值取dict2的值
# 2. 合并两个字典，相同键的值取两个值的和
# 请在此处编写代码：

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}

# 相同键的值取dict2的值
merged1 = dict1 | dict2
print(f"合并方式1：{merged1}")

# 相同键的值取两个值的和
merged2 = {}
for key in dict1.keys() | dict2.keys():
    merged2[key] = dict1.get(key, 0) + dict2.get(key, 0)
print("合并方式2：", merged2)
print()

# ===================== 练习题9：嵌套字典数据提取 =====================
# 题目：给定嵌套字典data = {
#     "class": "计算机1班",
#     "students": [
#         {"name": "张三", "score": {"math": 90, "english": 85, "chinese": 88}},
#         {"name": "李四", "score": {"math": 95, "english": 92, "chinese": 89}},
#         {"name": "王五", "score": {"math": 88, "english": 78, "chinese": 92}}
#     ]
# }
# 1. 提取班级名称
# 2. 提取李四的数学成绩
# 3. 计算所有学生的语文平均分
# 请在此处编写代码：

data = {
    "class": "计算机1班",
    "students": [
        {"name": "张三", "score": {"math": 90, "english": 85, "chinese": 88}},
        {"name": "李四", "score": {"math": 95, "english": 92, "chinese": 89}},
        {"name": "王五", "score": {"math": 88, "english": 78, "chinese": 92}}
    ]
}

print(f"提取班级名称：{data['class']}")
print(f"提取李四的数学成绩：{data['students'][1]['score']['math']}")

chinese_sum = 0
for stu in data["students"]:
    chinese_sum += stu["score"]["chinese"]

avg = chinese_sum / len(data["students"])
print(f"语文平均分：{round(avg, 2)}")
print()

# ===================== 练习题10：综合实战：学生成绩管理 =====================
# 题目：实现一个简单的学生成绩管理功能，完成以下需求
# 1. 定义一个空列表students，用于存储学生信息（每个学生是一个字典，包含name和score）
# 2. 添加3个学生：张三(85)、李四(92)、王五(78)
# 3. 修改张三的成绩为90
# 4. 删除王五的信息
# 5. 按成绩降序排序所有学生
# 6. 打印排序后的学生信息，格式：姓名：XXX，成绩：XXX
# 请在此处编写代码：

students = []

students.append({"name": "张三", "score": 85})
students.append({"name": "李四", "score": 92})
students.append({"name": "王五", "score": 78})
print(f"添加后的列表：{students}")

# 修改张三的成绩为90
for student in students:
    if student["name"] == "张三":
        student["score"] = 90
        break

# 删除王五的信息
for student in students:
    if student["name"] == "王五":
        students.remove(student)
        break

# 按成绩降序排序所有学生
students_sorted = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"按成绩降序排序所有学生：{students_sorted}")

# 打印排序后的学生信息，格式：姓名：XXX，成绩：XXX
for stu in students:
    print(f"姓名：{stu['name']}，成绩：{stu['score']}")