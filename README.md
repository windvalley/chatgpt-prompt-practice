# chatgpt-notebook

可以按你的习惯在终端使用`ipython`或在浏览器中使用 `jupyter notebook` 来运行代码.

## ipython

### 安装

```py
pip3 install ipython
pip3 install openai
pip3 install python-dotenv
```

### 运行

直接在终端输入:

```sh
cd ~/github/chatgpt-notebook
ipython
```

### Tips

1. 通过在代码行尾, 使用 ` \` + `enter`键来换行, 实现输入多行代码,
   类似于`jupyter notebook`直接通过`enter`键来换行.
   注意换行后还要再按`enter`键输入一个空行才可以继续输入代码行,
   否则运行代码将报错.

## jupyter notebook

### 安装

```py
pip3 install jupyter
pip3 install openai
pip3 install python-dotenv
```

### Tips

1. 相比 `ipython` 的优势: 历史输入输出有保存到 notebook 文件, 方便回顾历史.

### 运行

```sh
cd ~/github/chatgpt-notebook
jupyter notebook

# 或指定使用的工作目录
jupyter notebook --notebook-dir=~/github/chatgpt-notebook
```

在弹出的浏览器页面中使用`jupyter notebook`.

## 配置 chatgpt

1. 将你从`openai.com`获取的 API KEY 存放到工作目录的 `.env` 文件中

```sh
cd ~/github/chatgpt-notebook
echo 'OPENAI_API_KEY = "sk-mywzQ7Pc1ijBWVQTMpacT3BlbkF8YaLJdn8SaXcrT9alfTk6"' > .env
```

2. 每次使用前复制如下代码到`ipython`或`jupyter notebook`终端上

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

```sh
head=f"""
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
