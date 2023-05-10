#!/usr/bin/env python3

import os
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


# 每次对话都是独立的
def get_completion(prompt, m="gpt-3.5-turbo", t=0):
    '''
    prompt: 对应的提示
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    temperature: 温度系数
    '''
    messages = [
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(
        model=m,
        messages=messages,
        temperature=t,
    )

    return response.choices[0].message["content"]


# 连续对话
def get_completion_from_messages(messages, m="gpt-3.5-turbo", t=0):
    response = openai.ChatCompletion.create(
        model=m,
        messages=messages,
        temperature=t,
    )

    return response.choices[0].message["content"]
