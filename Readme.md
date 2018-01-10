
# Python基础

[TOC]

## 认识Python

### 第一个Python程序
> 可以直接在终端中进行，或者用编辑器：

```python
print ("HelloWorld!")
```

### 注释
> `#`标识的单行注释；`""`标识的是多行注释；  
> Python推荐编码模式：
> ```python
> #-*- coding:utf-8 -*-
> ```

### 变量以及类型
> 存储数据的容器：**变量**; 
> 包含：  
1. Numbers: `int`, `long`, `float`, `complex(j)`;
2. Bools: `True`, `False` ;
3. Str: `String`, `List`, `Tunple`, `Set`
4. `dict`  
  
>　可以通过type(Val)查看变量类型

### 标识符和关键字
> **标识符:**指自定义符号和名称，如变量名、函数名等；  
> **关键字：**python自带的特殊功能的标识符，可以用以下方式查看：  
> ```python
> import keyword
> keyword.kwlist
> ```

### 输入和输出
> **换行输出：**`print(\n)`，**格式化输出：**`print("%s,%d"%(x1,x2))`; `print()`函数默认输出结束换行，可加参数`end = ' '`改变；   
> **输入：**`input()`，默认接收为字符串



