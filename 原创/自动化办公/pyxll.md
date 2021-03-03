## 什么是PyXLL？

PyXLL是一个Excel加载项，使开发人员可以使用Python代码扩展Excel的功能。

PyXLL使Python成为Excel工作表的高效，灵活的后端，并允许您使用熟悉的Excel用户界面与信息基础结构的其他部分进行交互。

使用PyXLL，您的Python代码可以使用任何常见的Python发行版（例如Anaconda，Enthought的Canopy或任何其他从2.3到3.9的CPython发行版）在Excel中运行。

由于PyXLL运行您自己的完整Python发行版，因此您可以访问所有第三方Python软件包，例如NumPy，Pandas和SciPy，并可以从Excel中调用它们。

用例示例包括：

- 调用现有的Python代码以在Excel中执行计算
- 在VBA中进行太慢或繁琐的数据处理和分析
- 从数据库等外部系统中提取数据
- 查询大型数据集以在Excel中显示摘要级别的数据
- 向Excel用户公开内部或第三方库



## 它是如何工作的？

PyXLL根据其[config文件中](https://www.pyxll.com/docs/userguide/config/index.html)的规范在Excel中运行Python代码 ，您可以在其中配置Python的运行方式以及PyXLL应该加载的模块。当PyXLL启动时，它会加载这些模块并公开某些已经用PyXLL装饰器标记的功能。

例如，可以用Python编写用于计算第n个斐波那契数的Excel用户定义函数（UDF），如下所示：

```
from pyxll import xl_func

@xl_func
def fib(n):
    "Naiive Fibonacci implementation."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

该[`xl_func`](https://www.pyxll.com/docs/api/decorators.html#pyxll.xl_func)-decorated功能`fib`由PyXLL检测并暴露于Excel作为用户定义的函数。

![用Python实现的Excel中的斐波那契函数。](https://www.pyxll.com/_images/fib1.png)

Excel类型会根据可选的函数签名自动转换为Python类型。在没有简单转换的地方（例如，从方法返回任意类实例时），PyXLL将Python对象引用存储为Excel中的单元格值。当使用对该单元格的引用调用另一个函数时，PyXLL会检索该对象并将其传递给该方法。PyXLL会跟踪引用对象的单元格，以便一旦Excel不再引用该对象，便可以在Python中取消引用。



## 开始之前

现有用户可能想研究[PyXLL 5的新增功能](https://www.pyxll.com/docs/whatsnew.html#whatsnew5)。从早期版本升级的内容应为“从早期版本升级的[重要说明](https://www.pyxll.com/docs/whatsnew.html#upgrading)”。如果您喜欢边看边学，也许您会喜欢我们的[视频指南和教程](https://www.pyxll.com/docs/videos/index.html#videos)。

请注意，您不能混合使用32位和64位版本的Excel，Python和PyXLL –它们都必须相同。

根据[安装说明](https://www.pyxll.com/docs/userguide/installation/index.html#installing-pyxll)安装外接程序，并确保在必要时更新配置文件。有关通过Anaconda或Miniconda安装的特定说明，请参阅 [将PyXLL与Anaconda一起使用](https://www.pyxll.com/docs/userguide/installation/anaconda.html)。

一旦安装了PyXLL，您将可以尝试下载中包含的示例工作簿。下载中还包括示例工作簿中使用的所有代码。

请注意，所有错误都会写入日志文件，因此，如果您遇到困难，请始终在日志文件中查找问题所在，如果有疑问，请[与我们联系](https://www.pyxll.com/contact.html#contact)。



## 下一步

在[安装完PyXLL之后，](https://www.pyxll.com/docs/userguide/installation/index.html#installing-pyxll)下面的练习将向您展示如何编写您的第一个Python用户定义函数。



### 安装PyXLL 

首先，请按照[初次](https://www.pyxll.com/docs/userguide/installation/firsttime.html#first-time-install)安装PyXLL的说明进行操作。

您可以使用PyXLL的[命令行工具](https://www.pyxll.com/docs/userguide/installation/cli.html#cli)将PyXLL加载项安装到Excel中：

```
>> pip install pyxll
>> pyxll install
```



### 在Excel中调用Python函数

PyXLL的主要功能之一是能够从Excel工作簿中的公式调用Python函数。

首先从创建一个新的Python模块并编写一个简单的Python函数开始。要将功能公开给Excel，您要做的就是将[`xl_func`](https://www.pyxll.com/docs/api/decorators.html#pyxll.xl_func)装饰器应用到它。

```
from pyxll import xl_func

@xl_func
def hello(name):
    return "Hello, %s" % name
```

保存模块并再次编辑*pyxll.cfg*文件，以将新模块添加到要加载的模块列表中，并将包含模块的目录添加到pythonpath中。

```
[PYXLL]
modules = <add the name of your new module here>

[PYTHON]
pythonpath = <add the folder containing your Python module here>
```

转至*加载项*在Excel菜单并选择*PyXLL - >刷新*。这会导致PyXLL重新加载config和Python模块，从而允许发现新的和更新的模块。

现在，在工作表中，您会发现可以使用新的Python函数键入公式：

```
=hello("me")
```

使用PyCharm，Eclipse还是Visual Studio？

通过将它们作为调试器附加到正在运行的PyXLL，您可以使用Eclipse，PyCharm，Visual Studio和其他IDE交互式调试在PyXLL中运行的Python代码。有关详细信息，请参见我们的博客文章“[调试Python Excel加载项”](https://www.pyxll.com/blog/debugging-your-python-excel-add-in/)。

如果您在代码中犯了任何错误，或者函数返回了错误，则可以检查日志文件以找出错误所在，对代码进行必要的更改，然后重新加载PyXLL。

![用Python编写的简单Excel函数。](https://www.pyxll.com/_images/quickstart-func3.png)



### 其他资源

该[文档](https://www.pyxll.com/docs/userguide/index.html#userguide)说明了如何使用PyXLL的所有功能，并包含完整的API参考。在下载中包含的示例中也很好地展示了PyXLL的功能。这些是开始更多地了解PyXLL可以做什么的好地方。

可以在[PyXLL的GitHub页面](https://github.com/pyxll)上找到更多示例代码。

如果您有特定的尝试要解决，而找不到文档中的示例或帮助，请[与我们联系](https://www.pyxll.com/contact.html#contact)，我们将尽最大努力为您提供帮助。