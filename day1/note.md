# Day1 学习笔记：Python环境搭建 + 核心数据类型与字符串操作

## 今日学习目标

1. 完成Python+conda环境搭建，配置国内镜像源
2. 掌握变量定义规范与7种核心数据类型
3. 掌握字符串的索引、切片与常用操作
4. 知识点复盘与习题完成

---

## 一、环境搭建全流程

### 1. 核心软件安装

#### （1）Miniconda安装（Python3.10，AI开发最稳定版）

- 下载地址：清华大学镜像站 https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/
- 版本选择：`Miniconda3-py310_*`，对应你的操作系统（Windows/macOS/Linux）
- 安装注意：Windows勾选「Add Miniconda3 to my PATH environment variable」

#### （2）安装验证

打开终端（CMD），输入以下命令，输出版本号即安装成功：

```bash
conda --version
python --version
```

#### （3）配置国内镜像源（解决下载慢 / 超时问题）

终端依次执行以下命令，配置清华源：

```bash
# conda镜像源配置
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

# pip镜像源全局配置
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### （4）IDE 与工具安装

1. IDE：推荐 PyCharm 社区版（免费，新手友好），安装后配置 Python 解释器为上述 conda 环境的 Python3.10
2. Git：下载地址 https://git-scm.com/downloads 安装后终端输入 `git --version` 验证成功

---

## 二、Python 基础入门

### 1. 第一个 Python 程序

```python
print("Hello AI World!")
```

- `print()`：Python 内置输出函数，用于控制台打印内容
- 核心规则：代码严格区分大小写，所有标点必须是**英文半角**，否则会报错

### 2. 变量

#### （1）变量定义

变量是存储数据的容器，定义格式：`变量名 = 数据值`

```python
job = "AI应用开发工程师"
study_days = 90
daily_hours = 4.0
is_learn = True
```

#### （2）强制命名规范

1. 只能由字母、数字、下划线组成，**不能以数字开头**
2. 不能使用 Python 内置关键字（如 if、for、class 等）
3. 严格区分大小写（`Name` 和 `name` 是两个完全不同的变量）
4. 见名知意，推荐下划线命名法（如`user_name`、`student_score`）

#### （3）变量特性

- 变量可重复赋值，新值会覆盖旧值
- 支持多变量同时赋值：`a, b, c = 10, 20, 30`
- 用内置函数 `type()` 可查看变量的数据类型

## 三、7 种核心数据类型

| 数据类型        | 核心特点                                | 示例                        |
|-------------|-------------------------------------|---------------------------|
| 整数 `int`    | 不带小数点的数字，正负均可                       | `100`、`-20`、`0`           |
| 浮点数 `float` | 带小数点的数字                             | `3.14`、`-0.5`、`4.0`       |
| 字符串 `str`   | 用单 / 双 / 三引号包裹的文本                   | `"AI开发"`、`'Python'`       |
| 布尔值 `bool`  | 仅两个固定值，首字母必须大写                      | `True`、`False`            |
| 列表 `list`   | 用 `[]` 包裹，有序、可修改、支持混合类型             | `["张三", 20, 95.5]`        |
| 元组 `tuple`  | 用 `()` 包裹，有序、不可修改（只读）               | `("男", "女", "未知")`        |
| 字典 `dict`   | 用 `{}` 包裹，键值对 `key:value` 结构，key 唯一 | `{"name":"李四", "age":22}` |
| 集合 `set`    | 用 `{}` 包裹，无序、自动去重                   | `{1,2,3,3,2,1} → {1,2,3}` |

---

## 四、字符串核心操作

### 1. 字符串索引

- 索引：字符串中每个字符的位置编号，分为正向 / 反向索引
- 正向索引：从左到右，从 **0** 开始递增
- 反向索引：从右到左，从 **-1** 开始递减
- 示例：字符串 `s = "Python"`，`s[0] = 'P'`，`s[-1] = 'n'`

### 2. 字符串切片

- 作用：截取字符串中的指定片段
- 语法：`字符串[起始索引:结束索引:步长]`
- 核心规则：
    1. 左闭右开：包含起始索引的字符，**不包含**结束索引的字符
    2. 起始索引省略，默认从 0 开始；结束索引省略，默认到字符串末尾
    3. 步长省略，默认是 1；步长为负数，反向截取
- 示例：`s = "PythonAI"`，`s[0:6] = "Python"`，`s[::-1] = "IAnohtyP"`

### 3. 字符串常用内置方法

| 方法                  | 核心作用            | 示例                                            |
|---------------------|-----------------|-----------------------------------------------|
| `upper()`           | 所有字符转大写         | `"python".upper() → "PYTHON"`                 |
| `lower()`           | 所有字符转小写         | `"PYTHON".lower() → "python"`                 |
| `strip()`           | 去除字符串首尾的空白字符    | `" hello ".strip() → "hello"`                 |
| `replace(old, new)` | 替换指定内容          | `"hello".replace("l","x") → "hexxo"`          |
| `split(分隔符)`        | 按分隔符拆分字符串，返回列表	 | `"a,b,c".split(",") → ["a","b","c"]`          |
| `join(可迭代对象)`       | 用字符串连接序列元素      | `"-".join(["2024","01","01"]) → "2024-01-01"` |
| `len()`             | 内置函数，获取字符串长度	   | `len("python") → 6`                           |

---

## 五、今日易错点总结

1. 变量命名违规：数字开头、使用关键字、中英文标点混用
2. 字符串引号交叉混用：如 `'hello world"` 会直接报错
3. 索引越界：索引超出字符串长度范围，会报 `IndexError`
4. 切片左闭右开规则记错，导致截取内容少一位
5. 布尔值首字母小写：`true/false` 不是 Python 合法布尔值
6. 空集合定义错误：用 `{}` 定义会生成空字典，必须用 `set()`