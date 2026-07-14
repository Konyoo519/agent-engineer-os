""""调用 DeepSeek API，发送消息，拿回文本回复。"""

from openai import OpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def chat(messages: list[dict]) -> str:
    """"发送消息给 DeepSeek，返回它的文本回复。"""
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=messages,
    )
    return response.choices[0].message.content
