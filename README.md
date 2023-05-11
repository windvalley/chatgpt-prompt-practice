# chatgpt-prompt-practice

学习 prompt 工程技能, 提高工作效率.

## 快速开始

### 配置 API KEY

> 前提:
>
> - 你可以魔法上网
> - 有 chatgpt api key
> - 系统上有 python3 环境

```sh
$ git clone --depth 1 https://github.com/windvalley/chatgpt-prompt-practice.git

# NOTE: 本文档之后的所有操作均在此目录下进行
$ cd chatgpt-prompt-practice

# 这里的sk-开头的字符串即是你的api key, NOTE: 这里是假的key, 需要你自己去申请.
$ echo 'OPENAI_API_KEY="sk-mywzQ7Pc1ijBWVQTMpacT3BlbkF8YaLJdn8SaXcrT9alfTk6"' > .env
```

### 使用 ipython 或 jupyter notebook

可以按你的习惯在终端使用`ipython`或在浏览器中使用 `jupyter notebook` 来运行代码.

二者选其一即可.

#### 使用 ipython

```sh
# 安装
$ pip3 install ipython
$ pip3 install openai
$ pip3 install -U python-dotenv

# 运行
$ ipython

# 在ipython终端运行env.py文件, 加载openai相关环境和配置,
# 为之后使用chatgpt提供相关配置和函数.
In [1]: %run env.py
```

Tips:

1. 通过在代码行尾, 使用 ` \` + `enter`键来换行, 实现输入多行代码,
   类似于`jupyter notebook`直接通过`enter`键来换行.
   注意换行后还要再按`enter`键输入一个空行才可以继续输入代码行,
   否则运行代码将报错.

#### 使用 jupyter notebook

```sh
# 安装
$ pip3 install jupyter
$ pip3 install openai
$ pip3 install -U python-dotenv

# 运行如下命令行, 会弹出默认浏览器运行 http://localhost:8888/tree,
# 新建notebook, 后续操作类似ipython.
$ jupyter notebook

# 在notebook界面, 运行env.py文件, 为之后使用chatgpt提供相关配置和函数.
In [  ]: %run env.py
```

Tips:

1. 相比 `ipython` 的优势:

- 历史输入输出有保存到 notebook 文件, 方便回顾历史;
- 可以渲染 html、markdown 等源码

  ```python
  # 表格是以 HTML 格式呈现的，加载出来
  from IPython.display import display, HTML

  display(HTML(response))
  ```

### 提问示例

运行`ipython`或`jupyter notebook`, 执行完 `%run env.py` 后, 再按以下模版输入内容并运行, 将得到模型的回答.

```python
text = f"""
我希望你充当 IT 专家。我会向您提供有关我的技术问题所需的所有信息，而您的职责是解决我的问题。你应该使用你的项目管理知识，敏捷开发知识来解决我的问题。在您的回答中使用适合所有级别的人的智能、简单和易于理解的语言将很有帮助。用要点逐步解释您的解决方案很有帮助。我希望您回复解决方案，而不是写任何解释。我的第一个问题是:
"""

prompt = f"""
'''{text}'''
nvim报错:
Error executing lua callback: ...m/HEAD-2ef9d2a_1/share/nvim/runtime/lua/vim/lsp/sync.lua:66: i
ndex out of range
stack traceback:
        [C]: in function 'str_utfindex'
"""

response = get_completion(prompt)
print(response)
```

## 提示工程

### 模型局限性

LLM 偶尔会给出虚假知识(幻觉), 会生成一些看似真实实则编造的知识, 这是模型已知的一个弱点.

暂时的解决策略是先要求模型找到文本中的任何相关引用，然后要求它使用这些引用来回答问题，这种追溯源文档的方法通常对减少幻觉非常有帮助。

### 提示原则

#### 原则 1. 编写清晰、具体的指令

更长的提示实际上更清晰且提供了更多上下文，这实际上可能导致更详细更相关的输出。

策略:

- 使用分隔符清晰地表示输入的不同部分，分隔符可以是：\`\`\`，""，<>，<tag>，<\tag>等

  ```python
  text = f"""
  some detail text
  """
  prompt = f"""
  具体让chatgpt如何做的话术.
  '''{text}'''
  """
  ```

- 要求一个结构化的输出，可以是 Json、HTML 等格式

- 要求模型检查是否满足条件, 不满足该如何处理

- 提供少量示例, 让模型模仿你的示例

#### 原则 2. 给模型时间去思考

您可以指示模型花更多时间思考问题，这意味着它在任务上花费了更多的计算资源。

策略:

- 指定完成任务所需的步骤

- 指导模型在下结论之前找出一个自己的解法. 意思是先让模型推导出一个自己的解法, 再和你给出的解法进行比较, 最后再给出结论.

### 迭代式提示

只要您有一个好的迭代过程来不断改进您的 Prompt，那么你就能够得到一个适合任务的 Prompt。

在编写 Prompt 以使用 LLM 开发应用程序时:

- 首先, 您有一个关于要完成的任务的想法，可以尝试编写第一个 Prompt，满足上一章说过的两个原则：清晰明确，并且给模型足够的时间思考。

- 然后您可以运行它并查看结果。

- 如果第一次效果不好，那么迭代的过程就是找出为什么指令不够清晰或为什么没有给算法足够的时间思考，以便改进想法、改进提示等等.

- 循环多次，直到找到适合您的应用程序的 Prompt。

### 文本概括

目前 LLM 在文本概括任务上展现了强大的水准.

举例:

```python
prompt = f"""
你的任务是从电子商务网站上生成一个产品评论的简短摘要。

请对三个单引号之间的评论文本进行概括，最多30个词汇，并且聚焦在产品价格和质量上。

评论: '''{prod_review_zh}'''
"""
```

策略:

- 限制输出文本长度
- 关键角度侧重
- 关键信息提取, 如果想过滤掉不想要的信息, 则用关键字`提取`代替`概括`

### 推断

可以看作是模型接收文本作为输入并执行某种分析的过程。

```python
prompt = f"""
以下用三个单引号分隔的产品评论的情感是什么？

评论文本: '''{lamp_review_zh}'''
"""
```

```python
prompt = f"""
以下用三个反引号分隔的产品评论的情感是什么？

用一个单词回答：「正面」或「负面」。

评论文本: '''{lamp_review_zh}'''
"""
```

### 文本转换

LLM 非常擅长将输入转换成不同的格式，例如多语种文本翻译、拼写及语法纠正、语气调整、格式转换等。

1. 翻译+输出语气

   ````python
   text = f"""
   Would you like to order a pillow?
   """
   prompt = f"""
   请将以下文本翻译成中文，分别展示成正式与非正式两种语气:
   ```{text}```
   """
   response = get_completion(prompt)
   print(response)
   ````

2. 语气/风格调整

   ````python
   text = f"""
   小老弟，我小羊，上回你说咱部门要采购的显示器是多少寸来着？
   """
   prompt = f"""
   将以下文本翻译成商务信函的格式:
   ```{text}```
   """
   response = get_completion(prompt)
   print(response)
   ````

3. ChatGPT 非常擅长不同格式之间的转换，例如 JSON 到 HTML、XML、Markdown 等

   ```python
   data_json = { "resturant employees" :[
       {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
       {"name":"Bob", "email":"bob32@gmail.com"},
       {"name":"Jai", "email":"jai87@gmail.com"}
   ]}
   prompt = f"""
   将以下Python字典从JSON转换为HTML表格，保留表格标题和列名：{data_json}
   """
   response = get_completion(prompt)
   print(response)

   # 渲染(不适用于ipython, 适用于jupyter notebook)
   from IPython.display import display, Markdown, Latex, HTML, JSON
   display(HTML(response))
   ```

4. 拼写及语法纠正

   输入原始文本，输出纠正后的文本，并基于 Redlines 输出纠错过程。

   ````python
   # 如未安装redlines，需先安装
   !pip3 install redlines

   text = f"""
   Got this for my daughter for her birthday cuz she keeps taking \
   mine from my room.  Yes, adults also like pandas too.  She takes \
   it everywhere with her, and it's super soft and cute.  One of the \
   ears is a bit lower than the other, and I don't think that was \
   designed to be asymmetrical. It's a bit small for what I paid for it \
   though. I think there might be other options that are bigger for \
   the same price.  It arrived a day earlier than expected, so I got \
   to play with it myself before I gave it to my daughter.
   """
   prompt = f"校对并更正以下商品评论：```{text}```"
   response = get_completion(prompt)
   print(response)

   from redlines import Redlines
   from IPython.display import display, Markdown

   diff = Redlines(text,response)
   display(Markdown(diff.output_markdown))
   ````

5. 综合样例：文本翻译+拼写纠正+风格调整+格式转换

   ````python
   text = f"""
   Got this for my daughter for her birthday cuz she keeps taking \
   mine from my room.  Yes, adults also like pandas too.  She takes \
   it everywhere with her, and it's super soft and cute.  One of the \
   ears is a bit lower than the other, and I don't think that was \
   designed to be asymmetrical. It's a bit small for what I paid for it \
   though. I think there might be other options that are bigger for \
   the same price.  It arrived a day earlier than expected, so I got \
   to play with it myself before I gave it to my daughter.
   """
   prompt = f"""
   针对以下三个反引号之间的英文评论文本，
   首先进行拼写及语法纠错，
   然后将其转化成中文，
   再将其转化成优质淘宝评论的风格，从各种角度出发，分别说明产品的优点与缺点，并进行总结。
   润色一下描述，使评论更具有吸引力。
   输出结果格式为：
   【优点】xxx
   【缺点】xxx
   【总结】xxx
   注意，只需填写xxx部分，并分段输出。
   将结果输出成Markdown格式。
   ```{text}```
   """
   response = get_completion(prompt)

   from IPython.display import display, Markdown
   display(Markdown(response))
   ````

### 文本扩展

扩展是将短文本，例如一组说明或主题列表，输入到大型语言模型中，让模型生成更长的文本，例如基于某个主题的电子邮件或论文。

温度系数如何使用:

- 可以将温度视为模型探索或随机性的程度。在构建需要可预测响应的应用程序时，我建议使用温度为零。
- 如果您尝试以更具创意的方式使用模型，可能需要更广泛地输出不同的结果，那么您可能需要使用更高的温度。您几乎可以将其视为在更高的温度下，助手更易分心，但也许更有创造力。

  ```python
  # 将温度参数从0调整为0.7
  response = get_completion(prompt, t=0.7)
  print(response)
  ```

### 聊天机器人

可以使用 LLM 来构建一个定制的聊天机器人，只需要很少的工作量。

由于涉及到图型界面, 所以必须用 `jupyter notebook` 来演示:

```python
# 安装GUI
In [  ]: !pip install panel

# 加载聊天机器人
In [  ]: %run chat_robot.py

# 运行对话框, 并进行对话查看效果
In [  ]: dashboard
```

具体实现方式请参考 [chat_robot.py](chat_robot.py) 脚本, 可以通过修改 `context` 变量改变系统消息内容, 来确定你要实现什么样的聊天机器人.

## 参考文档

- https://github.com/datawhalechina/prompt-engineering-for-developers
- https://github.com/datawhalechina/hugging-llm
- https://github.com/rockbenben/ChatGPT-Shortcut
