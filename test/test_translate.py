# coding=utf-8

from paperassistant.models import Translator

trans = Translator("seamlessM4T_large")

eng_t = "Large Language Models (LLMs), like LLaMA, have exhibited remarkable performances across various tasks."

result = trans.T2TT(eng_t)

print(result)