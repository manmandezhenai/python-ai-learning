# Day2 练习题：分支结构 + 循环结构 + 列表推导式

# ===================== 练习题1：多分支成绩判定 =====================
# 题目：输入一个0-100的考试分数，完成以下判定
# 1. 分数大于100或小于0，打印"分数输入无效"
# 2. 90分及以上，打印"优秀"
# 3. 80-89分，打印"良好"
# 4. 60-79分，打印"及格"
# 5. 60分以下，打印"不及格"
# 要求：用if-elif-else多分支实现
# 请在此处编写代码：

score = int(input("请输入你的分数："))
if score < 0 or score > 100:
    print("分数输入无效")
else:
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
print()

# ===================== 练习题2：循环累加与统计 =====================
# 题目：计算1-100以内，所有能被3整除且不能被5整除的数字的和，以及符合条件的数字个数
# 要求：分别用for循环和while循环两种方式实现
# 请在此处编写代码：

# for 循环实现
sum_for = 0
count_for = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 != 0:
        sum_for += i
        count_for += 1

print("for循环实现：")
print(f"符合条件的数字和：{sum_for}")
print(f"符合条件的数字个数：{count_for}")
print()

# while 循环实现
sum_while = 0
count_while = 0
i = 1
while i <= 100:
    if i % 3 == 0 or i % 5 != 0:
        sum_while += i
        count_while += 1
    i += 1

print("while循环实现：")
print(f"符合条件的数字和：{sum_while}")
print(f"符合条件的数字个数：{count_while}")
print()

# ===================== 练习题3：九九乘法表拓展 =====================
# 题目：打印倒序的九九乘法表（从9×9=81开始，到1×9=9结束，逐行递减）
# 要求：用循环嵌套实现，格式对齐，无语法错误
# 请在此处编写代码：

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()
print()

# ===================== 练习题4：列表推导式实战 =====================
# 题目：用列表推导式完成以下需求，禁止用传统for循环+append
# 1. 生成1-50以内，所有能被7整除的数字的列表
# 2. 给定列表words = ["python", "AI", "java", "data", "hello", "world"]，筛选出长度大于4的单词，转为全大写
# 3. 给定列表nums = [1, -2, 3, -4, 5, -6, 7, -8]，将正数乘以2，负数保持不变，生成新列表
# 请在此处编写代码：

list1 = [i for i in range(1, 51) if i % 7 == 0]
print(list1)

words = ["python", "AI", "java", "data", "hello", "world"]
list2 = [word.upper() for word in words if len(word) > 4]
print(list2)

nums = [1, -2, 3, -4, 5, -6, 7, -8]
list3 = [num * 2 if num > 0 else num for num in nums]
print(list3)
print()

# ===================== 练习题5：LeetCode 704. 二分查找（简化版） =====================
# 题目：给定一个升序排列的整数数组nums，和一个目标值target，判断target是否存在于数组中
# 要求：用for循环遍历实现，存在打印"找到目标值"，不存在打印"目标值不存在"，用break优化循环
# 示例：nums = [-1,0,3,5,9,12], target=9 → 找到目标值；target=2 → 目标值不存在
# 请在此处编写代码：

nums = [-1, 0, 3, 5, 9, 12]
target = 9
for num in nums:
    if num == target:
        print("找到目标值")
        break
else:
    print("目标值不存在")
print()

# ===================== 练习题6：LeetCode 1. 两数之和（简化版） =====================
# 题目：给定一个整数数组nums和一个目标值target，判断数组中是否存在两个数，它们的和等于target
# 要求：用嵌套for循环实现，存在打印"存在符合条件的两个数"，不存在打印"不存在符合条件的两个数"
# 示例：nums = [2,7,11,15], target=9 → 存在；target=20 → 不存在
# 请在此处编写代码：

nums = [2, 7, 11, 15]
target = 9
has_result = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            has_result = True
            break

if has_result:
    print("存在符合条件的两个数")
else:
    print("不存在符合条件的两个数")
print()

# ===================== 练习题7：LeetCode 26. 删除有序数组中的重复项（简化版） =====================
# 题目：给定一个升序排列的数组nums，去除数组中的重复元素，生成一个无重复的新列表
# 要求：用for循环+if判断实现，不能用set()去重
# 示例：nums = [1,1,2,2,3,3,4] → 新列表 [1,2,3,4]
# 请在此处编写代码：

nums = [1, 1, 2, 2, 3, 3, 4]
new_nums = []
for num in nums:
    if num not in new_nums:
        new_nums.append(num)

print(f"去重后的列表：{new_nums}")
print()

# ===================== 练习题8：LeetCode 9. 回文数 =====================
# 题目：给你一个整数x，判断x是否是回文数。回文数是指正序和倒序读都是一样的整数
# 要求：不能将整数转为字符串，用while循环+数学运算实现
# 示例：121 → 是回文数；-121 → 不是；10 → 不是
# 请在此处编写代码：

x = 121
# 负数和末尾为0的非0数一定不是回文数
if x < 0 or (x % 10 == 0 and x != 0):
    print("不是回文数")
else:
    reverse_num = 0
    original_x = x
    while x > 0:
        # 取最后一位数字
        last_num = x % 10
        reverse_num = reverse_num * 10 + last_num
        # 去掉最后一位数字
        x = x // 10
    if reverse_num == original_x:
        print("是回文数")
    else:
        print("不是回文数")
print()

# ===================== 练习题9：LeetCode 1480. 一维数组的动态和 =====================
# 题目：给你一个数组nums，数组的动态和计算公式为：runningSum[i] = sum(nums[0]…nums[i])
# 要求：用for循环实现，生成动态和数组
# 示例：nums = [1,2,3,4] → 动态和 [1,3,6,10]
# 请在此处编写代码：

nums = [1, 2, 3, 4]
running_sum = []
current_sum = 0
for num in nums:
    current_sum += num
    running_sum.append(current_sum)

print(f"动态和数组：{running_sum}")
print()

# ===================== 练习题10：综合实战：斐波那契数列筛选 =====================
# 题目：生成100以内的所有斐波那契数，筛选出其中的偶数，计算它们的和
# 要求：用while循环生成数列，用列表推导式完成筛选与求和
# 请在此处编写代码：

fib_list = []
a, b = 1, 1
while a <= 100:
    fib_list.append(a)
    a, b = b, a + b

# 筛选偶数并求和
even_fib = [num for num in fib_list if num % 2 == 0]
sum_even = sum(even_fib)
print(f"100以内的斐波那契数：{fib_list}")
print(f"其中的偶数：{even_fib}")
print(f"偶数的和：{sum_even}")
