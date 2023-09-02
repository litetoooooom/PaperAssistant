# coding=utf-8
import torch
from transformers import (AutoModelForCausalLM, AutoTokenizer)
from transformers.generation.utils import GenerationConfig


class LLM:
    def __init__(self, model_path) -> None:
        self.model_path = model_path

        self.model, self.tokenizer = self._load()

    def _load(self):
        model = AutoModelForCausalLM.from_pretrained(
            self.model_path, device_map="auto", torch_dtype=torch.float16, trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, use_fast=False, trust_remote_code=True)
        model.generation_config = GenerationConfig.from_pretrained(self.model_path)
        return model, tokenizer

    def summary(self, input):
        messages = []
        prompt = f"用中文总结下面这段话：\n\n{input}"
        messages.append({"role": "user", "content": prompt})
        response = self.model.chat(self.tokenizer, messages)
        return response
