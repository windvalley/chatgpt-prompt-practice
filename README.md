# chatgpt-prompt-practice

## 环境准备

可以按你的习惯在终端使用`ipython`或在浏览器中使用 `jupyter notebook` 来运行代码.

### ipython

#### 安装

```py
pip3 install ipython
pip3 install openai
pip3 install -U python-dotenv
```

#### 运行

直接在终端输入:

```sh
cd ~/github/chatgpt-notebook
ipython
```

#### Tips

1. 通过在代码行尾, 使用 ` \` + `enter`键来换行, 实现输入多行代码,
   类似于`jupyter notebook`直接通过`enter`键来换行.
   注意换行后还要再按`enter`键输入一个空行才可以继续输入代码行,
   否则运行代码将报错.

### jupyter notebook

#### 安装

```py
pip3 install jupyter
pip3 install openai
pip3 install -U python-dotenv
```

#### 运行

```sh
cd ~/github/chatgpt-notebook
jupyter notebook

# 或指定使用的工作目录
jupyter notebook --notebook-dir=~/github/chatgpt-notebook
```

在弹出的浏览器页面中使用`jupyter notebook`.

#### Tips

1. 相比 `ipython` 的优势:

- 历史输入输出有保存到 notebook 文件, 方便回顾历史;
- 可以渲染 html、markdown 等源码

  ```python
  # 表格是以 HTML 格式呈现的，加载出来
  from IPython.display import display, HTML

  display(HTML(response))
  ```

## 配置 chatgpt

1. 将你从`openai.com`获取的 API KEY 存放到工作目录的 `.env` 文件中

```sh
cd ~/github/chatgpt-notebook
echo 'OPENAI_API_KEY = "sk-mywzQ7Pc1ijBWVQTMpacT3BlbkF8YaLJdn8SaXcrT9alfTk6"' > .env
```

2. 每次使用前复制如下代码到`ipython`终端或`jupyter notebook`界面上

```python
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]
```

3. 提问举例

```python
text = f"""
我希望你充当 IT 专家。我会向您提供有关我的技术问题所需的所有信息，而您的职责是解决我的问题。你应该使用你的项目管理知识，敏捷开发知识来解决我的问题。在您的回答中使用适合所有级别的人的智能、简单和易于理解的语言将很有帮助。用要点逐步解释您的解决方案很有帮助。我希望您回复解决方案，而不是写任何解释。我的第一个问题是:
"""

prompt = f"""
'''{head}'''
nvim报错:
Error executing lua callback: ...m/HEAD-2ef9d2a_1/share/nvim/runtime/lua/vim/lsp/sync.lua:66: i
ndex out of range
stack traceback:
        [C]: in function 'str_utfindex'
"""

res = get_completion(prompt)
print(res)
```

## 提示工程

### 模型局限性

偶尔会给出虚假知识(幻觉), 会生成一些看似真实实则编造的知识, 这是模型已知的一个弱点.

暂时的解决策略是先要求模型找到文本中的任何相关引用，然后要求它使用这些引用来回答问题，这种追溯源文档的方法通常对减少幻觉非常有帮助。

### 提示原则

1. 编写清晰、具体的指令

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

2. 给模型时间去思考

您可以指示模型花更多时间思考问题，这意味着它在任务上花费了更多的计算资源。

策略:

- 指定完成任务所需的步骤

- 指导模型在下结论之前找出一个自己的解法

  意思是先让模型推导出一个自己的解法, 再和你给出的解法进行比较, 最后再给出结论.

### 迭代式提示

只要您有一个好的迭代过程来不断改进您的 Prompt，那么你就能够得到一个适合任务的 Prompt。

在编写 Prompt 以使用 LLM 开发应用程序时:

- 首先, 您有一个关于要完成的任务的想法，可以尝试编写第一个 Prompt，满足上一章说过的两个原则：清晰明确，并且给系统足够的时间思考。

- 然后您可以运行它并查看结果。

- 如果第一次效果不好，那么迭代的过程就是找出为什么指令不够清晰或为什么没有给算法足够的时间思考，以便改进想法、改进提示等等.

- 循环多次，直到找到适合您的应用程序的 Prompt。

### 文本概括


