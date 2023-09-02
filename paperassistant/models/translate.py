# coding=utf-8

import torch
from seamless_communication.models.inference import Translator as Translator_model


class Translator:
    def __init__(self, model_path) -> None:
        self.model_path = model_path
        self.model = self._load()

    def _load(self):
        # Initialize a Translator object with a multitask model, vocoder on the GPU.
        return Translator_model(self.model_path, vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"), dtype=torch.float32)

    def T2TT(self, input_text):
        translated_text, _, _ = self.model.predict(
            input_text, "t2tt", "cmn", src_lang="eng")
        return translated_text
