# Day3 示例代码：四大核心容器深入 + 深拷贝浅拷贝 + 容器通用操作

import copy

# ===================== 1. 列表常用方法示例 =====================
print("=" * 20 + " 列表常用方法示例 " + "=" * 20)

list_demo = [1, 2, 3]
print(f"原列表：{list_demo}")

# append vs extend
list_demo.append([4, 5])
print(f"append([4, 5])后：{list_demo}")
list_demo.extend([6, 7])
print(f"extend([6, 7])后：{list_demo}")

# insert
list_demo.insert(1, 100)
print(f"insert(1,100)后：{list_demo}")

# pop vs remove
popped = list_demo.pop()
print(f"pop()后：{list_demo}，被删除的元素：{popped}")
list_demo.remove(100)
print(f"remove(100)后：{list_demo}")

# index & count
print(f"元素3的索引：{list_demo.index(3)}")
print(f"元素2出现的次数：{list_demo.count(2)}")

# sort vs sorted
nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)
print(f"原列表：{nums}，sorted()后：{sorted_nums}")
nums.sort(reverse=True)
print(f"sort(reverse=True)后：{nums}")

# reverse
nums.reverse()
print(f"reverse()后：{nums}")

# clear
nums.clear()
print(f"clear()后：{nums}")
print()

# ===================== 2. 字典常用方法示例 =====================
print("=" * 20 + " 字典常用方法示例 " + "=" * 20)

dict_demo = {"name": "张三", "age": 20, "score": 90}
print(f"原列表：{dict_demo}")

# get方法（推荐）
print(f"获取 name：{dict_demo.get('name')}")
print(f"获取不存在的 gender：{dict_demo.get('gender', '未知')}")

# keys/values/items
print(f"所有键：{list(dict_demo.keys())}")
print(f"所有值：{list(dict_demo.values())}")
print(f"所有键值对：{list(dict_demo.items())}")

# update
dict_demo.update({"age": 21, "gender": "男"})
print(f"update后：{dict_demo}")

# pop
popped = dict_demo.pop("score")
print(f"pop('score')后：{dict_demo}，被删除的值：{popped}")

# popitem
popped_item = dict_demo.popitem()
print(f"popitem()后：{dict_demo}，被删除的键值对：{popped_item}")

# clear
dict_demo.clear()
print(f"clear()后：{dict_demo}")
print()

# ===================== 3. 集合常用方法示例 =====================
print("=" * 20 + " 集合常用方法示例 " + "=" * 20)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"set1：{set1}")
print(f"set2：{set2}")

# add
set1.add(5)
print(f"add(5)后set1：{set1}")

# remove vs discard
set1.remove(5)
print(f"remove(5)后set1：{set1}")
set1.discard(100)  # 不存在不报错
print(f"discard(100)后set1：{set1}")

# 集合运算
print(f"并集：{set1.union(set2)}")
print(f"交集：{set1.intersection(set2)}")
print(f"差集：{set1.difference(set2)}")
print(f"set1是否是set2的子集：{set1.issubset(set2)}")

# pop
popped = set1.pop()
print(f"pop()后set1：{set1}，被删除的元素：{popped}")

# clear
set1.clear()
print(f"clear()后set1：{set1}")
print()

# ===================== 4. 元组特性示例 =====================
print("=" * 20 + " 元组特性示例 " + "=" * 20)

# 单元素元组
t1 = (1)
t2 = (1,)
print(f"(1)的类型：{type(t1)}")
print(f"(1,)的类型：{type(t2)}")

# 元组不可变特性
t = (1, 2, [3, 4])
print(f"原元组：{t}")
t[2].append(5)  # 合法，修改嵌套列表的内容
print(f"修改嵌套列表后：{t}")
# t[2] = [5, 6]   # TypeError: 'tuple' object does not support item assignment

# 元组方法
print(f"元素2出现的次数：{t.count(2)}")
print(f"元素2的索引：{t.index(2)}")
print()

# ===================== 5. 深拷贝与浅拷贝示例 =====================
print("=" * 20 + " 深拷贝与浅拷贝示例 " + "=" * 20)

original = [1, 2, [3, 4]]
print(f"原对象：{original}")

# 赋值
a = original
a[0] = 100
a[2].append(5)
print(f"赋值后原对象：{original}")

# 浅拷贝
original = [1, 2, [3, 4]]
b = copy.copy(original)
b[0] = 200
b[2].append(6)
print(f"浅拷贝后原对象：{original}")

# 深拷贝
original = [1, 2, [3, 4]]
c = copy.deepcopy(original)
c[0] = 300
c[2].append(7)
print(f"深拷贝后原对象：{original}")
print()

# ===================== 6. 容器通用操作示例 =====================
print("=" * 20 + " 容器通用操作示例 " + "=" * 20)

# 6.1 遍历
print("带索引遍历列表：")
for index, item in enumerate(["a", "b", "c"]):
    print(f"索引{index}：{item}")

print("\n遍历字典键值对：")
for key, value in {"name": "李四", "age": 22}.items():
    print(f"{key}：{value}")

# 6.2 筛选
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_nums = [num for num in nums if num % 2 == 0]
print(f"\n筛选偶数：{evens_nums}")

# 6.3 排序
print("\n自定义排序：按字符串长度排序")
words = ["python", "ai", "java", "data", "machine"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

print("\n字典按值降序排序：")
score_dict = {"张三": 85, "李四": 92, "王五": 78}
sorted_score = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_score)

# 6.4 合并
list1 = [1, 2]
list2 = [3, 4]
print(f"\n列表合并：{list1 + list2}")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(f"字典合并：{dict1 | dict2}")

set1 = {1, 2}
set2 = {2, 3}
print(f"集合合并：{set1 | set2}")
print()

print("=" * 20 + " Day3示例代码运行结束 " + "=" * 20)
