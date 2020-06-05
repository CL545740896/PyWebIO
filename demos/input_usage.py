"""
输入演示
^^^^^^^^^^^
演示PyWebIO支持的各种输入形式

:demo_host:`Demo地址 </?pywebio_api=input_usage>`  `源码 <https://github.com/wang0618/PyWebIO/blob/master/demos/input_usage.py>`_
"""
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *


def main():
    set_auto_scroll_bottom(False)
    set_title("PyWebIO输入演示")

    put_markdown("""# PyWebIO 输入演示
    
    在[这里](https://github.com/wang0618/PyWebIO/blob/master/demos/input_usage.py)可以获取本Demo的源码。
    
    PyWebIO的输入函数都定义在 `pywebio.input` 模块中，可以使用 `from pywebio.input import *` 引入。

    ### 基本输入
    首先是一些基本类型的输入

    #### 文本输入
    ```python
    name = input("What's your name?")
    ```
    """, lstrip=True)
    put_text("这样一行代码的效果如下：",)
    name = input("What's your name?")
    put_markdown("`name = %r`" % name)

    # 其他类型的输入
    put_markdown("""PyWebIO的输入函数是同步的，在表单被提交之前，输入函数不会返回。
    #### 其他类型的输入:
    ```python
    # 密码输入
    password = input("Input password", type=PASSWORD)
    
    # 下拉选择框
    gift = select('Which gift you want?', ['keyboard', 'ipad'])
    
    # CheckBox
    agree = checkbox("用户协议", options=['I agree to terms and conditions'])
    
    # Text Area
    text = textarea('Text Area', rows=3, placeholder='Some text')
    
    # 文件上传
    img = file_upload("Select a image:", accept="image/*")
    ```
    """, lstrip=True)
    password = input("Input password", type=PASSWORD)
    put_markdown("`password = %r`" % password)
    gift = select('Which gift you want?', ['keyboard', 'ipad'])
    put_markdown("`gift = %r`" % gift)
    agree = checkbox("用户协议", options=['I agree to terms and conditions'])
    put_markdown("`agree = %r`" % agree)
    text = textarea('Text Area', rows=3, placeholder='Some text')
    put_markdown("`text = %r`" % text)
    img = file_upload("Select a image:", accept="image/*", help_text='可以直接选择"提交"')
    put_markdown("`img = %r`" % img)

    # 输入选项
    put_markdown("""#### 输入选项
    输入函数可指定的参数非常丰富：
    ```python
    input('This is label', type=TEXT, placeholder='This is placeholder', 
          help_text='This is help text', required=True, 
          datalist=['candidate1', 'candidate2', 'candidate2'])
    ```
    """, strip_indent=4)
    input('This is label', type=TEXT, placeholder='This is placeholder',
          help_text='This is help text', required=True,
          datalist=['candidate1', 'candidate2', 'candidate2'])

    # 校验函数
    put_markdown("""我们可以为输入指定校验函数，校验函数校验通过时返回None，否则返回错误消息:
    ```python
    def check_age(p):  # 检验函数校验通过时返回None，否则返回错误消息
        if p < 10:
            return 'Too young!!'
        if p > 60:
            return 'Too old!!'

    age = input("How old are you?", type=NUMBER, valid_func=check_age)
    ```
    """, strip_indent=4)

    def check_age(p):  # 检验函数校验通过时返回None，否则返回错误消息
        if p < 10:
            return 'Too young!!'
        if p > 60:
            return 'Too old!!'

    age = input("How old are you?", type=NUMBER, valid_func=check_age, help_text='尝试输入一些非法值，比如"8"、"65"')
    put_markdown('`age = %r`' % age)

    # Codemirror
    put_markdown(r"""PyWebIO 的 `textarea()` 输入函数还支持使用 [Codemirror](https://codemirror.net/) 实现代码风格的编辑区，只需使用 `code` 参数传入Codemirror支持的选项即可(最简单的情况是直接传入` code={}` 或 `code=True`):
    ```python
    code = textarea('Code Edit', code={
        'mode': "python",  # 编辑区代码语言
        'theme': 'darcula',  # 编辑区darcula主题
    }, value='import something\n# Write your python code')
    ```
        """, strip_indent=4)

    code = textarea('Code Edit', code={
        'mode': "python",  # 编辑区代码语言
        'theme': 'darcula',  # 编辑区darcula主题, Visit https://codemirror.net/demo/theme.html#cobalt to get more themes
    }, value='import something\n# Write your python code')

    put_markdown("Your code:\n```python\n%s\n```" % code)

    # 输入组
    put_markdown(r"""### 输入组
    `input_group()` 接受单项输入组成的列表作为参数，输入组中需要在每一项输入函数中提供 `name` 参数来用于在结果中标识不同输入项。输入组中同样支持设置校验函数，其接受整个表单数据作为参数。

    ```python
    def check_form(data):  # 检验函数校验通过时返回None，否则返回 (input name,错误消息)
        if len(data['name']) > 6:
            return ('name', '名字太长！')
        if data['age'] <= 0:
            return ('age', '年龄不能为负数！')

    data = input_group("Basic info", [
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER, valid_func=check_age)
    ], valid_func=check_form)
    ```
    """, strip_indent=4)

    def check_form(data):  # 检验函数校验通过时返回None，否则返回 (input name,错误消息)
        if len(data['name']) > 6:
            return ('name', '名字太长！')
        if data['age'] <= 0:
            return ('age', '年龄不能为负数！')

    data = input_group("Basic info", [
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER, valid_func=check_age)
    ], valid_func=check_form)

    put_markdown("`data = %r`" % data)


if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
